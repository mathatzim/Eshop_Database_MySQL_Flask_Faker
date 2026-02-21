# Schema setup

This repository contains a MySQL Workbench model file:

- `ESHOP DATABASE MODEL(WEDNESDAY).mwb`

To create the schema:

1. Open the `.mwb` file in **MySQL Workbench**
2. Use **Database → Forward Engineer** to create tables in a database named `eshop_database` (or your preferred name)
3. Update your connection settings via `.env` (see `.env.example`)

Then you can populate data with:

```bash
python -m src.populate_db
```

If you already have the schema created (e.g., from coursework), you can skip forward engineering and just point the scripts at your existing database.
