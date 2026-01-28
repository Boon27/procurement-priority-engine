# Procurement Priority Engine – Architecture

## 📌 Overview
This document explains the architecture and workflow of the Procurement Priority Engine.  
It highlights the **data pipeline, business logic, and governance framework** that drive procurement prioritization.

---

## 🔄 Workflow Steps

### 1. Input Data
- Source: `inventory_input.csv`
- Key fields: SKU identifiers, demand, cost, revenue, supplier region, category tier.
- Purpose: Provide baseline operational and financial data for each SKU.

---

### 2. Config Tables
- Externalized YAML configs:
  - `service_policy.yaml` → Service levels & Z-scores.
  - `priority_config.yaml` → Scoring weights & multipliers.
  - `lead_time_map.yaml` → Regional lead times.
- Purpose: Ensure **governance-ready, auditable, and flexible** parameter management.

---

### 3. Lead Time Rules
- Map supplier region to lead time (months).
- Used to calculate **lead time demand** and safety stock requirements.

---

### 4. Service Level Policy
- Apply Z-scores based on category tier.
- Ensures **service-level differentiation** (Core vs Support vs Tail).

---

### 5. Forecast Error Assumption
- Default: 30% error rate (can be replaced with SKU-level MAPE).
- Purpose: Account for demand uncertainty in safety stock calculations.

---

### 6. Core Inventory Calculations
- Effective Stock = Stock on Hand + On Order.
- Lead Time Demand = Avg Monthly Demand × Lead Time Months.

---

### 7. Safety Stock
- Service-Level Safety Stock = Z × Demand Std Dev × √Lead Time.
- Forecast Error Buffer = Demand × Error Rate × Lead Time.
- Total Safety Stock = Service-Level + Forecast Buffer.

---

### 8. Dynamic Min–Max Policy
- Dynamic Min = Lead Time Demand + Safety Stock.
- Dynamic Max = Dynamic Min + (2 × Avg Monthly Demand).
- Purpose: Create **adaptive reorder thresholds**.

---

### 9. Stock-Out Risk
- Projected Stock at Arrival = Effective Stock – Lead Time Demand.
- Risk classification: HIGH / MEDIUM / LOW.

---

### 10. Order Decision Logic
- If Effective Stock < Dynamic Min → Order Required.
- Suggested Order Qty = Dynamic Max – Effective Stock.

---

### 11. Profitability Logic
- COGS_12mo = Cost × Demand × 12.
- Revenue_12mo = Revenue × Demand × 12.
- Realistic Profit = (Revenue – Cost) × Fulfillable Units.
- Profit Tier: HIGH_PROFIT / LOW_PROFIT / LOSS.

---

### 12. ABC Classification
- Based on cumulative profit contribution.
- A = Top 80%, B = Next 15%, C = Remaining 5%.

---

### 13. XYZ Classification
- Based on demand variability (Coefficient of Variation).
- X = Stable demand, Y = moderate variability, Z = highly variable.

---

### 14. Combined Matrix
- Concatenate ABC + XYZ → e.g., AX, BY, CZ.
- Purpose: Capture both **profit contribution and demand variability**.

---

### 15. Priority Scoring
- Weighted score using config multipliers:
  - Tier, Risk, Order Flag, ABC, XYZ, Profitability.
- Breakdown string for **auditability**:
  - Example: `Tier:3|Risk:2|Order:1|ABC:3|XYZ:2|PL:3`.

---

### 16. Final Output
- Export `procurement_priority_output.csv`.
- Sorted by **Priority Score** (descending).
- Fields include stock levels, risk, order qty, classifications, profitability, and score breakdown.

---

## 🛠️ Governance Features
- **Config-driven architecture** → YAML files externalize policies.
- **Auditability** → Score breakdown shows how each factor contributes.
- **Flexibility** → Easy to adapt for new regions, tiers, or business rules.
- **Enterprise alignment** → Inspired by SAP IBP and Azure Supply Chain AI.

---

## 📈 Visual Workflow (Text Diagram)

