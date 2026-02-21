# Schema setup

This repository provides two ways to create the database schema:

## Option A — MySQL Workbench model (recommended)

- Workbench model: `docs/workbench/ESHOP_DATABASE_MODEL.mwb`

Steps:
1. Open the `.mwb` file in **MySQL Workbench**
2. Use **Database → Forward Engineer**
3. Create tables in a database named `eshop_database` (or any name you prefer)
4. Set your connection settings in `.env` (see `.env.example`)

## Option B — Run the generated SQL script

- Forward-engineered SQL: `sql/schema_workbench.sql`

Steps:
1. Create a database in MySQL (example: `eshop_database`)
2. Run `sql/schema_workbench.sql` in MySQL Workbench or phpMyAdmin
3. Set your connection settings in `.env` (see `.env.example`)

## Next step: populate the database

Once the schema exists, populate it with synthetic data:

```bash
python -m src.populate_db
```

Then start the Flask app:

```bash
python -m src.app
```
