from __future__ import annotations

import os
import random
from dataclasses import dataclass

import mysql.connector
from faker import Faker
import faker_commerce
from dotenv import load_dotenv


@dataclass
class DBConfig:
    host: str = os.getenv("MYSQL_HOST", "localhost")
    port: int = int(os.getenv("MYSQL_PORT", "3306"))
    database: str = os.getenv("MYSQL_DATABASE", "eshop_database")
    user: str = os.getenv("MYSQL_USER", "test")
    password: str = os.getenv("MYSQL_PASSWORD", "test")


def get_connection(cfg: DBConfig):
    return mysql.connector.connect(
        host=cfg.host,
        port=cfg.port,
        user=cfg.user,
        password=cfg.password,
        database=cfg.database,
    )


def main() -> None:
    """Populate the e-shop database with synthetic data.

    Note: The database schema must already exist (e.g., forward engineered from the .mwb model).
    """
    load_dotenv()  # read local .env if present

    cfg = DBConfig()
    db = get_connection(cfg)
    cursor = db.cursor()

    faker_gen = Faker()
    faker_gen.add_provider(faker_commerce.Provider)

    # Helper to commit + show progress
    def commit(label: str):
        db.commit()
        print(f"Inserted into {label}: {cursor.rowcount}")

    # 1) Brands
    query = "INSERT INTO brands(Brand_name) VALUES (%s)"
    for _ in range(25):
        cursor.execute(query, (faker_gen.word(),))
    commit("brands")

    # 2) Product categories
    query = "INSERT INTO product_categories(ProductCategory_Description) VALUES (%s)"
    for _ in range(25):
        cursor.execute(query, (faker_gen.ecommerce_category(),))
    commit("product_categories")

    # 3) Products (FKs assume IDs 1..25 exist for categories and brands)
    query = "INSERT INTO products(Discontinued, Product_Name, Product_categoryID, BrandID) VALUES (%s, %s, %s, %s)"
    for _ in range(25):
        cursor.execute(
            query,
            (
                faker_gen.boolean(),
                faker_gen.ecommerce_name(),
                random.randint(1, 25),
                random.randint(1, 25),
            ),
        )
    commit("products")

    # 4) Shops
    query = "INSERT INTO shops(Shop_Name, Country, City, Address, Phone, Shop_Email) VALUES (%s, %s, %s, %s, %s, %s)"
    for _ in range(25):
        cursor.execute(
            query,
            (
                faker_gen.company(),
                faker_gen.country(),
                faker_gen.city(),
                faker_gen.address(),
                faker_gen.phone_number(),
                faker_gen.email(),
            ),
        )
    commit("shops")

    # 5) Product variations
    query = "INSERT INTO product_variation(ProductID, Description) VALUES (%s, %s)"
    DESCRIPTIONS = (
        "Metal",
        "Handmade",
        "Cotton",
        "Professional",
        "Oversized fit",
        "Slim fit",
        "easy to use",
        "Classic Logo Print",
        "Urban Streetwear Collection",
        "Signature Embroidery",
        "Adventure Ready",
        "Minimalist Protection",
        "Artistic Expression",
        "Winter Essentials",
    )
    for _ in range(25):
        cursor.execute(query, (random.randint(1, 25), random.choice(DESCRIPTIONS)))
    commit("product_variation")

    # 6) Product colors
    query = "INSERT INTO product_color(Primary_Color, Secondary_Color) VALUES (%s, %s)"
    for _ in range(25):
        cursor.execute(query, (faker_gen.color_name(), faker_gen.color_name()))
    commit("product_color")

    # 7) Product dimensions
    query = "INSERT INTO product_dimensions(Product_Size, Vertical_Dimension, Horizontal_Dimension) VALUES (%s, %s, %s)"
    for _ in range(25):
        cursor.execute(
            query,
            (
                faker_gen.random_element(elements=("S", "M", "L", "XL", "XXL")),
                random.randint(1, 300),
                random.randint(1, 300),
            ),
        )
    commit("product_dimensions")

    # 8) Product options (assumes dimensions and colors IDs 1..25)
    query = "INSERT INTO product_options(Product_DimensionsID, Product_ColorID, Model_year) VALUES (%s, %s, %s)"
    for _ in range(25):
        cursor.execute(query, (random.randint(1, 25), random.randint(1, 25), random.randint(2010, 2026)))
    commit("product_options")

    # 9) Product price
    query = "INSERT INTO product_price(Starting_ProductPrice, Discount_Percentage, Current_ProductPrice) VALUES (%s, %s, %s)"
    for _ in range(25):
        start_price = round(random.uniform(5, 500), 2)
        discount = random.randint(0, 70)
        current_price = round(start_price * (1 - discount / 100), 2)
        cursor.execute(query, (start_price, discount, current_price))
    commit("product_price")

    # 10) Product options in shops (assumes options/prices/shops IDs 1..25)
    query = "INSERT INTO product_options_has_shops(Product_OptionsID, ShopID, Product_PriceID, ProductStock_Number) VALUES (%s, %s, %s, %s)"
    for _ in range(25):
        cursor.execute(query, (random.randint(1, 25), random.randint(1, 25), random.randint(1, 25), random.randint(0, 500)))
    commit("product_options_has_shops")

    # 11) Customers
    query = "INSERT INTO customers(Customer_FirstName, Customer_LastName, Customer_Email, Country, City) VALUES (%s, %s, %s, %s, %s)"
    for _ in range(25):
        cursor.execute(
            query,
            (faker_gen.first_name(), faker_gen.last_name(), faker_gen.email(), faker_gen.country(), faker_gen.city()),
        )
    commit("customers")

    # 12) Shop comments
    query = "INSERT INTO shop_comments(sComment_Content, sComment_Rating, sComment_Date, CustomerID, ShopID) VALUES (%s, %s, %s, %s, %s)"
    for _ in range(25):
        cursor.execute(
            query,
            (
                faker_gen.text(max_nb_chars=120),
                random.randint(1, 5),
                faker_gen.date_between(start_date="-2y", end_date="today"),
                random.randint(1, 25),
                random.randint(1, 25),
            ),
        )
    commit("shop_comments")

    # 13) Product comments (assumes Product_VariationID 1..25)
    query = "INSERT INTO product_comments(pComment_Content, pComment_Rating, pComment_Date, CustomerID, Product_VariationID) VALUES (%s, %s, %s, %s, %s)"
    for _ in range(25):
        cursor.execute(
            query,
            (
                faker_gen.text(max_nb_chars=120),
                random.randint(1, 5),
                faker_gen.date_between(start_date="-2y", end_date="today"),
                random.randint(1, 25),
                random.randint(1, 25),
            ),
        )
    commit("product_comments")

    # 14) Customer orders (assumes ShopID 1..25)
    query = "INSERT INTO customerorders(OrderDate, Order_country, Order_City, Order_Address, PostalCode, Shipment_Method, Payment_Method, CustomerID, Order_Address2, Customer_Phone, Customer_Phone2, ShopID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    SHIPMENT_METHODS = ("Courier", "Post", "Pickup")
    PAYMENT_METHODS = ("Card", "Cash", "PayPal")
    for _ in range(25):
        cursor.execute(
            query,
            (
                faker_gen.date_between(start_date="-1y", end_date="today"),
                faker_gen.country(),
                faker_gen.city(),
                faker_gen.street_address(),
                faker_gen.postcode(),
                random.choice(SHIPMENT_METHODS),
                random.choice(PAYMENT_METHODS),
                random.randint(1, 25),
                faker_gen.secondary_address(),
                faker_gen.phone_number(),
                faker_gen.phone_number(),
                random.randint(1, 25),
            ),
        )
    commit("customerorders")

    # 15) Order items (assumes order IDs 1..25, variation IDs 1..25, price IDs 1..25)
    query = "INSERT INTO orderitems(Customer_OrderID, Ordered_Quantity, Product_VariationID, Product_PriceID) VALUES (%s, %s, %s, %s)"
    for _ in range(50):
        cursor.execute(query, (random.randint(1, 25), random.randint(1, 5), random.randint(1, 25), random.randint(1, 25)))
    commit("orderitems")

    # 16) Variation ↔ options bridge (assumes IDs 1..25)
    query = "INSERT INTO product_variation_has_product_options(Product_VariationID, Product_OptionsID) VALUES (%s, %s)"
    for _ in range(25):
        cursor.execute(query, (random.randint(1, 25), random.randint(1, 25)))
    commit("product_variation_has_product_options")

    cursor.close()
    db.close()
    print("Done.")


if __name__ == "__main__":
    main()
