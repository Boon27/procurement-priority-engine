# Procurement Priority Engine

## Overview
This project calculates procurement priorities for inventory items using enterprise-style rules:
- Service level policies
- Safety stock and dynamic min–max
- ABC/XYZ classification
- Profitability tiers
- Config-driven priority scoring

## Input
CSV file (`inventory_input.csv`) with columns:
- BarCode, Description, Category_Tier, Supplier_Region
- Stock_On_Hand, On_Order, Avg_Monthly_Demand
- Cost, Revenue

## Output
CSV file (`procurement_priority_output.csv`) with:
- Effective_Stock, Safety_Stock, Dynamic_Min/Max
- Stockout_Risk, Suggested_Order_Qty
- ABC/XYZ classification
- Profit tiers and Priority Score

## Usage
```bash
python procurement_priority.py --input inventory_input.csv --output procurement_priority_output.csv
