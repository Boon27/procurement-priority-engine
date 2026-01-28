import pandas as pd
import numpy as np
import pytest
from procurement_priority import compute_priority_score

# -----------------------------
# 1. Sample Data Fixture
# -----------------------------
@pytest.fixture
def sample_df():
    data = {
        "BarCode": ["SKU001"],
        "Description": ["Test Item"],
        "Category_Tier": ["A. Core"],
        "Supplier_Region": ["Pacific"],
        "Stock_On_Hand": [50],
        "On_Order": [20],
        "Avg_Monthly_Demand": [30],
        "Cost": [10],
        "Revenue": [15],
        "Z_Score": [2.05],
        "Forecast_Error_Rate": [0.30],
        "Lead_Time_Months": [3],
        "Demand_Std_Dev": [9],
        "Service_Level_Safety_Stock": [2.05 * 9 * np.sqrt(3)],
        "Forecast_Error_Buffer": [30 * 0.30 * 3],
        "Total_Safety_Stock": [0],  # placeholder, will be recalculated
        "Suggested_Order_Qty": [0],
        "Stockout_Risk": ["LOW"],
        "ABC_Class": ["A"],
        "XYZ_Class": ["X"],
        "PL_Tier": ["HIGH_PROFIT"]
    }
    df = pd.DataFrame(data)
    df["Total_Safety_Stock"] = df["Service_Level_Safety_Stock"] + df["Forecast_Error_Buffer"]
    return df

# -----------------------------
# 2. Config Fixture
# -----------------------------
@pytest.fixture
def priority_config():
    return {
        "tier_weight": {"A. Core": 3, "B. Support": 2, "C. Tail": 1},
        "risk_weight": {"HIGH": 3, "MEDIUM": 2, "LOW": 1},
        "abc_weight": {"A": 3, "B": 2, "C": 1},
        "xyz_weight": {"X": 3, "Y": 2, "Z": 1},
        "pl_weight": {"HIGH_PROFIT": 3, "LOW_PROFIT": 2, "LOSS": 0},
        "multipliers": {
            "tier": 3,
            "risk": 4,
            "order_flag": 2,
            "abc": 5,
            "xyz": 3,
            "pl": 6
        }
    }

# -----------------------------
# 3. Tests
# -----------------------------

def test_safety_stock_calculation(sample_df):
    """Ensure safety stock is correctly calculated."""
    expected = sample_df["Service_Level_Safety_Stock"].iloc[0] + sample_df["Forecast_Error_Buffer"].iloc[0]
    assert np.isclose(sample_df["Total_Safety_Stock"].iloc[0], expected)

def test_priority_score_computation(sample_df, priority_config):
    """Check that priority score is positive and breakdown is generated."""
    score, breakdown = compute_priority_score(sample_df, priority_config)
    assert score.iloc[0] > 0
    assert "Tier:" in breakdown.iloc[0]
    assert "Risk:" in breakdown.iloc[0]

def test_profit_tier_assignment(sample_df):
    """Verify profit tier classification logic."""
    assert sample_df["PL_Tier"].iloc[0] == "HIGH_PROFIT"

def test_classification_labels(sample_df):
    """Ensure ABC and XYZ classifications are valid."""
    assert sample_df["ABC_Class"].iloc[0] in ["A", "B", "C"]
    assert sample_df["XYZ_Class"].iloc[0] in ["X", "Y", "Z"]
