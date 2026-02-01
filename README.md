# 📊 Vendor Performance & Inventory Analytics Pipeline
**An End-to-End Data Engineering & Business Intelligence Project**

---

## 🚀 Project Overview
This project addresses the challenges of managing large-scale inventory data by building a robust **ETL (Extract, Transform, Load) Pipeline**. Using a dataset of over **1 Million records**, I implemented an automated system to ingest, clean, and visualize supply chain metrics.

The primary goal was to identify high-performing vendors and optimize stock levels to improve business profitability.

## 🛠️ Tech Stack
- **Languages:** Python (Pandas, SQLAlchemy, SciPy)
- **Database:** SQLite3 (Relational Data Warehousing)
- **BI Tool:** Power BI (Advanced DAX & Interactive Dashboards)
- **Environment:** Jupyter Notebook & VS Code

---

## 🏗️ Technical Architecture
1. **Data Ingestion (`ingestion_db.py`):**
   - Implemented a **Batch Processing** strategy using a `chunksize=100,000` to handle large CSV files without memory crashes.
   - Built an automated logging system to track data ingestion health.
2. **Feature Engineering & Cleaning:**
   - Merged complex datasets (Sales, Purchases, Freight) to calculate KPIs like **Profit Margin %**, **Stock Turnover**, and **Vendor Contribution**.
   - Performed statistical validation using T-Tests (SciPy) to ensure data accuracy.
3. **Data Visualization:**
   - Developed an executive-level **Power BI Dashboard** to track real-time business health.

---


---

## 📂 Repository Structure
| File | Description |
| :--- | :--- |
| `ingestion_db.py` | Python script for automated batch data ingestion into SQL. |
| `get_vendor_summary.py` | Core logic for data transformation and KPI calculation. |
| `Exploratory Data Analysis.ipynb` | Statistical EDA and data quality checks. |
| `Vendor Performance Analysis.ipynb` | Final data preparation and business logic. |

---

## 💡 Key Business Impact
- **Efficiency:** Reduced manual data preparation time by **90%**.
- **Insights:** Isolated low-performing brands with <15% turnover for immediate clearance.
- **Scalability:** The pipeline can easily scale to handle millions of new records monthly.

---

## 🤝 Let's Connect!
I am an aspiring Data Analyst passionate about turning raw data into strategic business decisions. Feel free to reach out for collaborations or opportunities!

- **Name:** Yukta Soni
- **Email:** Yukta11jee@gmail.com
- **LinkedIn:** https://www.linkedin.com/in/yukta-soni-0591a2295?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
- **GitHub:** [github.com/Soni-yukta](https://github.com/Soni-yukta)

---
