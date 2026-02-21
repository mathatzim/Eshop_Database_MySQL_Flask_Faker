# E‑Shop Database — Data Generation + SQL Queries (MySQL + Flask)

Undergraduate project that designs and demonstrates an **online store (e‑commerce) relational database**.

It includes:
- a **MySQL Workbench model** (`.mwb`) for the schema
- a Python script that **populates tables with realistic synthetic data** using **Faker**
- a small **Flask app** that runs **6 multi-table JOIN queries** and renders the outputs as HTML tables

## What this project demonstrates
- Relational modelling (entities, PK/FK relationships)
- Data generation for testing (Faker + randomised FK references)
- SQL JOINs across a realistic e‑commerce schema
- Simple “analytics-style” query pages (Flask + Jinja templates)

## Files
- `docs/ESHOP DATABASE MODEL(WEDNESDAY).mwb` — schema model (open with MySQL Workbench)
- `src/populate_db.py` — populate the database with synthetic data
- `src/app.py` — Flask app with `/query/1` … `/query/6`
- `src/queries.py` — SQL strings used by the app
- `templates/` — HTML templates for each query page
- `docs/Contemporary Problem PROPOSAL.docx` and `docs/Contemporary Problem Analysis Presentation.pptx` — coursework artefacts
- `src/legacy/` — original submission scripts (kept for reference)

## Setup (high level)
1. Create the MySQL schema (recommended):
   - Open the `.mwb` model in **MySQL Workbench**
   - Forward engineer it to a database named `eshop_database`
2. Create a MySQL user (or reuse your own) with permissions on that database.
3. Populate data using `src/populate_db.py`.
4. Run the Flask app and visit the query routes.

## Configuration
This repo reads connection settings from environment variables:

- `MYSQL_HOST` (default: `localhost`)
- `MYSQL_PORT` (default: `3306`)
- `MYSQL_DATABASE` (default: `eshop_database`)
- `MYSQL_USER` (default: `test`)
- `MYSQL_PASSWORD` (default: `test`)

You can create a local `.env` file (not committed) with those values.

## Run (example)
```bash
pip install -r requirements.txt

# Populate synthetic data
python -m src.populate_db

# Run the query UI
python -m src.app
```

Then open:
- `http://127.0.0.1:5000/` (index)
- `http://127.0.0.1:5000/query/1` … `http://127.0.0.1:5000/query/6`

## The 6 query pages (summary)
- Query 1: Product + variation + customer product comments
- Query 2: Order details joined to products and shop
- Query 3: Customer order items (customer ↔ orders ↔ items ↔ product)
- Query 4: Shop comments joined to shops and customers
- Query 5: Full product catalogue view (category/brand/options/dimensions/shop)
- Query 6: Same as Query 5 filtered to a specific product name (example: `'Keyboard'`)

