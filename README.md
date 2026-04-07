# E-commerce Data Pipeline (End-to-End)

## 📌 Overview
Built a production-style data engineering pipeline to ingest, validate, transform, and analyze e-commerce transactional data using Python and PostgreSQL.

---

## ⚙️ Architecture

Raw Data (CSV)
    ↓
Python Ingestion
    ↓
PostgreSQL (Raw Tables)
    ↓
Data Validation Layer
    ↓
Transformation Layer (SQL)
    ↓
Analytics Layer (Business Metrics)

---

## 🚀 Features

- End-to-end ETL pipeline
- Incremental data loading (duplicate-safe)
- Data validation checks
- SQL-based transformation layer
- Business analytics generation (Customer LTV)
- Logging for pipeline execution

---

## 🧱 Tech Stack

- Python (Pandas, Psycopg2)
- PostgreSQL
- SQL
- VS Code

---

## 📊 Key Output

- Cleaned transactional dataset
- Customer Lifetime Value (LTV)
- Structured analytics tables

---

## ▶️ How to Run

```bash
python main.py