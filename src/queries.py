from __future__ import annotations

# SQL queries used by the Flask app.
# (Kept as plain strings so they're easy to review and modify.)

QUERY_1 = """SELECT Product_Name,Description,pComment_Content,Customer_FirstName,Customer_LastName
FROM products
INNER JOIN product_variation ON products.ProductID = product_variation.ProductID
INNER JOIN product_comments ON product_variation.Product_VariationID = product_comments.Product_VariationID
INNER JOIN customers ON product_comments.CustomerID = customers.CustomerID"""

QUERY_2 = """SELECT Product_Name,Description,OrderDate,Order_Country,Order_City,Order_Address,PostalCode,Shipment_Method,Payment_Method,Shop_Name
FROM orderitems
INNER JOIN customerorders ON orderitems.Customer_OrderID = customerorders.Customer_OrderID
INNER JOIN product_variation ON orderitems.Product_VariationID = product_variation.Product_VariationID
INNER JOIN products ON product_variation.ProductID = products.ProductID
INNER JOIN shops ON customerorders.ShopID = shops.ShopID"""

QUERY_3 = """SELECT Customer_FirstName,Customer_LastName,Product_Name,Description,Ordered_Quantity,OrderDate,Shop_Name
FROM customers
INNER JOIN customerorders ON customers.CustomerID = customerorders.CustomerID
INNER JOIN orderitems ON customerorders.Customer_OrderID = orderitems.Customer_OrderID
INNER JOIN product_variation ON orderitems.Product_VariationID = product_variation.Product_VariationID
INNER JOIN products ON product_variation.ProductID = products.ProductID
INNER JOIN shops ON customerorders.ShopID = shops.ShopID"""

QUERY_4 = """SELECT Shop_Name,sComment_Content,sComment_Rating,sComment_Date,Customer_FirstName,Customer_LastName
FROM shop_comments
INNER JOIN shops ON shop_comments.ShopID = shops.ShopID
INNER JOIN customers ON shop_comments.CustomerID = customers.CustomerID"""

QUERY_5 = """SELECT ProductCategory_Description,Brand_Name,Product_Name,Description,Primary_Color,Secondary_Color,Product_Size,Vertical_Dimension,Horizontal_Dimension,Model_year,Shop_Name
FROM product_categories
INNER JOIN products ON product_categories.ProductCategory_ID = products.Product_categoryID
INNER JOIN product_variation ON products.ProductID = product_variation.ProductID
INNER JOIN product_variation_has_product_options ON product_variation.Product_VariationID = product_variation_has_product_options.Product_VariationID
INNER JOIN product_options ON product_variation_has_product_options.Product_OptionsID = product_options.Product_OptionsID
INNER JOIN product_color ON product_options.Product_ColorID = product_color.Product_ColorID
INNER JOIN product_dimensions ON product_options.Product_DimensionsID = product_dimensions.Product_DimensionsID
INNER JOIN brands ON products.BrandID = brands.BrandID
INNER JOIN product_options_has_shops ON product_options.Product_OptionsID = product_options_has_shops.Product_OptionsID
INNER JOIN shops ON product_options_has_shops.ShopID = shops.ShopID"""

QUERY_6 = QUERY_5 + " WHERE Product_Name = 'Keyboard'"

ALL_QUERIES = {
    1: QUERY_1,
    2: QUERY_2,
    3: QUERY_3,
    4: QUERY_4,
    5: QUERY_5,
    6: QUERY_6,
}
