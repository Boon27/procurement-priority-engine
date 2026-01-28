# Dashboard Mockup – Procurement Priority Engine

## 📌 Purpose
This dashboard translates the output of the Procurement Priority Engine into **executive-ready visuals**.  
It enables procurement managers and executives to quickly identify:
- Which SKUs require urgent orders
- Where stockout risks are highest
- Which items contribute most to profitability
- How procurement priorities align with service tiers

---

## 📊 Suggested Visuals

### 1. Priority Heatmap
- **X-axis**: ABC Classification (A, B, C)
- **Y-axis**: XYZ Classification (X, Y, Z)
- **Color intensity**: Priority Score
- Purpose: Quickly spot high-priority items (e.g., AX, BY).

---

### 2. Stockout Risk Bar Chart
- Bars grouped by **Stockout Risk** (HIGH, MEDIUM, LOW).
- Height = Number of SKUs in each risk category.
- Purpose: Show overall risk exposure across portfolio.

---

### 3. Profitability Contribution Pie Chart
- Segments = PL Tier (HIGH_PROFIT, LOW_PROFIT, LOSS).
- Size = Share of total profit.
- Purpose: Highlight how capital is allocated across profitable vs. loss-making SKUs.

---

### 4. Suggested Orders Table
- Columns: SKU, Description, Suggested Order Qty, Priority Score, Risk Level.
- Conditional formatting: Highlight SKUs with HIGH risk in red.
- Purpose: Provide actionable procurement list.

---

### 5. Regional Lead Time Map
- Map visualization with supplier regions.
- Bubble size = Lead Time Demand.
- Bubble color = Average Lead Time Months.
- Purpose: Show geographic distribution of procurement risk.

---

## 📈 Executive Summary View
- **KPI Cards**:
  - Total Suggested Order Qty
  - % SKUs at HIGH Risk
  - Total Realistic Profit
- Purpose: Provide at-a-glance metrics for executives.

---

## 🌍 Deployment Options
- **Power BI** → Interactive visuals, drill-down by SKU.
- **Tableau** → Advanced visual storytelling.
- **Excel** → Lightweight version for quick adoption.

---

## 🎯 Business Impact
This dashboard turns raw CSV outputs into **decision-ready insights**:
- Procurement managers can act on **urgent orders**.
- Executives can monitor **profitability vs. risk trade-offs**.
- Organizations can align procurement with **service-level policies** and **working capital goals**.
