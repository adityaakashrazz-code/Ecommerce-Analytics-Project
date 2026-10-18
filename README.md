# End-to-End E-Commerce Data Analytics Pipeline

## 📌 Project Overview
This project is a complete end-to-end data analytics pipeline using real-world E-Commerce data (Olist). The goal of this project is to extract raw CSV data, clean anomalies using Python, load it into a relational database, and perform advanced SQL querying to extract actionable business insights regarding revenue trends and customer distribution.

## 🛠️ Tech Stack Used
* **Programming Language:** Python
* **Libraries:** Pandas (Data manipulation & cleaning)
* **Database:** SQLite (Relational database management)
* **SQL Skills:** Joins, Common Table Expressions (CTEs), Window Functions, Aggregations
* **Concepts:** ETL (Extract, Transform, Load), Data Normalization, Data Quality Assurance

## 🚀 Pipeline Workflow

### Phase 1: Data Extraction & Cleaning (`data_cleaning.py`)
* Imported raw order and customer datasets.
* Investigated null values in delivery dates and applied business logic to filter out canceled/processing orders.
* Handled data anomalies (e.g., dropping rows marked as 'delivered' but missing timestamps).
* Type-casted string columns to proper Python `datetime` objects.

### Phase 2: Database Schema & Loading (`load_to_sql.py`)
* Built a local SQLite database (`ecommerce.db`).
* Engineered an automated process to load the cleaned Pandas DataFrames into SQL tables, replacing them dynamically if they already exist.

### Phase 3: Core SQL Analytics (`sql_queries.py`)
* Mapped Primary and Foreign keys (`customer_id`) to join the `orders` and `customers` tables.
* Identified the top 5 cities driving the highest volume of successfully delivered orders.

### Phase 4: Advanced SQL & Financial Metrics (`advanced_sql.py`)
* Utilized **Common Table Expressions (CTEs)** to aggregate monthly revenue data.
* Implemented **Window Functions** `SUM() OVER (ORDER BY...)` to calculate the running total of revenue over time.
* Exported the final aggregated views into a clean CSV format, ready for BI dashboard integration (Power BI / Tableau).

## 📊 Key Business Insights
1. **Geographic Dominance:** Sao Paulo is the overwhelming market leader for delivered orders, followed by Rio de Janeiro and Belo Horizonte. 
2. **Revenue Growth:** The Window Function analysis revealed a consistent Month-over-Month increase in revenue, tracking the company's financial growth seamlessly.
3. **Data Integrity:** Discovered and filtered out logistical anomalies where orders were marked 'delivered' without valid timestamp records, ensuring 100% accuracy in final revenue reporting.
