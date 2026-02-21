# E-Shop Database — MySQL + Faker Data Generation + Flask JOIN Queries

Undergraduate project that designs and demonstrates an **e-commerce relational database** and a small analytics-style UI.

This repo includes:
- A **MySQL schema** (forward engineered from Workbench)
- A **Python data generator** (Faker) that populates the tables with synthetic data
- A **Flask app** that runs **6 multi-table JOIN queries** and renders results as HTML tables

## What this project demonstrates
- Relational modelling (entities, PK/FK relationships)
- Synthetic data generation for testing (Faker + randomized FK references)
- SQL joins across a realistic e-commerce schema
- Simple query/report pages (Flask + Jinja templates)

## Repository structure
- `sql/schema_workbench.sql` — schema creation script (exported from Workbench)
- `src/populate_db.py` — populate the DB with synthetic data
- `src/app.py` — Flask app with `/query/1` … `/query/6`
- `src/queries.py` — SQL strings used by the Flask pages
- `templates/` — HTML templates
- `docs/` — coursework artifacts + setup notes

## Schema setup (choose one)

### Option A — MySQL Workbench model (recommended)
If you have the `.mwb` model file, open it in **MySQL Workbench** and use:
**Database → Forward Engineer**.

> Note: the schema name must match what your Python scripts connect to.
> Your scripts default to `eshop_database` (configurable via `MYSQL_DATABASE`).

### Option B — Run the SQL schema script
1. Create a database in MySQL (example: `eshop_database`)
2. Run: `sql/schema_workbench.sql` (Workbench or phpMyAdmin)

⚠️ Important: the SQL script currently creates a schema named `ESHOP_Database`.
You have two easy options:
- **Set** `MYSQL_DATABASE=ESHOP_Database` in your `.env`, **or**
- Edit `sql/schema_workbench.sql` and rename the schema to `eshop_database`.

## Configuration
Create a local `.env` file in the repo root (do not commit it):

```env
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=eshop_database
MYSQL_USER=test
MYSQL_PASSWORD=test

## Install & Run
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

