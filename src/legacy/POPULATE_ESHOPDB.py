from faker import Faker
import mysql.connector
import faker_commerce
import random


db = mysql.connector.connect(
    host='localhost', user='test', password='test', database='eshop_database'
)

cursor = db.cursor()
faker_gen = Faker()
faker_gen.add_provider(faker_commerce.Provider)

query = "INSERT INTO brands(Brand_name) VALUES (%s)" 

for i in range(25):
  values = (faker_gen.word(),)
  
  cursor.execute(query, values)

db.commit()

print(cursor.rowcount)

#///////////////////////////////////////////////////
query1 = "INSERT INTO product_categories(ProductCategory_Description) VALUES (%s)" 

for i in range(25):
  values1 = (faker_gen.ecommerce_category(), )
  
  cursor.execute(query1, values1)

db.commit()

print(cursor.rowcount)

#////////////////////////////////////////////////////
query2 = "INSERT INTO products(Discontinued, Product_Name, Product_categoryID, BrandID) VALUES (%s, %s, %s, %s)" 

for i in range(25):
  values2 = (faker_gen.boolean(),faker_gen.ecommerce_name(),random.randint(1, 25) , random.randint(1,25) )
  
  cursor.execute(query2, values2)

db.commit()

print(cursor.rowcount)

#//////////////////////////////////////////////////
query3 = "INSERT INTO shops(Shop_Name, Country, City, Address, Phone, Shop_Email) VALUES (%s, %s, %s, %s, %s, %s)"

for i in range(25):
  values3 = (faker_gen.company(),faker_gen.country(),faker_gen.city(),faker_gen.address(),faker_gen.phone_number(),faker_gen.email())
  
  cursor.execute(query3, values3)

db.commit()

print(cursor.rowcount)

#/////////////////////////////////////////////////
query4 = "INSERT INTO product_variation(ProductID, Description) VALUES (%s, %s)"

for i in range(25):
  DESCRIPTIONS = ("Metal","Handmade","Cotton","Professional","Oversized fit","Slim fit","easy to use",
                   "Classic Logo Print","Urban Streetwear Collection","Signature Embroidery",
                   "Adventure Ready","Minimalist Protection","Artistic Expression","Winter Essentials")
  values4 = (random.randint(1, 25),random.choice(DESCRIPTIONS) )
  
  cursor.execute(query4, values4)

db.commit()

print(cursor.rowcount)

#////////////////////////////////////////////////
query5 = "INSERT INTO product_color(Primary_Color, Secondary_Color) VALUES (%s, %s)"

for i in range(25):
    
    values5 = (faker_gen.color_name(),faker_gen.color_name())
    
    cursor.execute(query5, values5)

db.commit()

print(cursor.rowcount)

#///////////////////////////////////////////////
query6 = "INSERT INTO product_dimensions(Product_Size, Vertical_Dimension, Horizontal_Dimension) VALUES (%s, %s, %s)"

for i in range(25):
    SIZES = ("XS","S","M","L","XL","2XL")
    
    values6 = (random.choice(SIZES),(random.randint(10,100)/10 ),(random.randint(10,100)/10 ))
    
    cursor.execute(query6, values6)

db.commit()

print(cursor.rowcount)

#/////////////////////////////////////////////
query7 = "INSERT INTO product_options(Product_DimensionsID, Product_ColorID, Model_year) VALUES (%s, %s, %s)"

for i in range(25):
    
    values7 = (random.randint(1, 25), random.randint(1, 25), faker_gen.year())
    
    cursor.execute(query7, values7)

db.commit()

print(cursor.rowcount)

#//////////////////////////////////////////
query8 = "INSERT INTO product_price(Starting_ProductPrice, Discount_Percentage, Current_ProductPrice) VALUES (%s, %s, %s)"

for i in range(25):
    startP = (faker_gen.ecommerce_price()/100000) 
    perc = (random.randint(10,95) )
    discamount = startP *(perc/100)
    currentP = startP - discamount        
    values8 = (startP, perc, currentP)
    
    
    cursor.execute(query8, values8)

db.commit()

print(cursor.rowcount)

#////////////////////////////////////////
query9 = "INSERT INTO product_options_has_shops(Product_OptionsID, ShopID, Product_PriceID, ProductStock_Number) VALUES (%s, %s, %s, %s)"

for i in range(25):
    
    values9 = (random.randint(1, 25), random.randint(1, 25), random.randint(1, 25), random.randint(0, 2500))
    
    cursor.execute(query9, values9)

db.commit()

print(cursor.rowcount)

#////////////////////////////////////////
query10 = "INSERT INTO customers(Customer_FirstName, Customer_LastName, Customer_Email, Country, City) VALUES (%s, %s, %s, %s, %s)"

for i in range(25):
    
    values10 = (faker_gen.first_name(),faker_gen.last_name(),faker_gen.email(),faker_gen.country(),faker_gen.city())
    
    cursor.execute(query10, values10)

db.commit()

print(cursor.rowcount)

#////////////////////////////////////////
query11 = "INSERT INTO shop_comments(sComment_Content, sComment_Rating, sComment_Date, CustomerID, ShopID) VALUES (%s, %s, %s, %s, %s) "

for i in range(25):
    
    values11 = (faker_gen.text(), random.randint(0,10)/1, faker_gen.date(), random.randint(1, 25), random.randint(1, 25) )
    
    cursor.execute(query11, values11)

db.commit()

print(cursor.rowcount)

#//////////////////////////////////////
query12 = "INSERT INTO product_comments(pComment_Content, pComment_Rating, pComment_Date, CustomerID, Product_VariationID) VALUES (%s, %s, %s, %s, %s)"

for i in range(25):
    
    values12 = (faker_gen.text(), random.randint(0,10)/1, faker_gen.date(), random.randint(1, 25), random.randint(1, 25) )
    
    cursor.execute(query12, values12)

db.commit()

print(cursor.rowcount)

#/////////////////////////////////////
query13 = "INSERT INTO customerorders(OrderDate, Order_country, Order_City, Order_Address, PostalCode, Shipment_Method, Payment_Method, CustomerID, Order_Address2, Customer_Phone, Customer_Phone2, ShopID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

for i in range(25):
    ShipM = ("Standard Shipping","Express Shipping","In-Store Pickup", "Dropshipping")
    PayM = ("Credit Card","Debit Card","Cash on Delivery (COD)","Bank Transfer")
    
    values13 = (faker_gen.date(), faker_gen.country(), faker_gen.city(),faker_gen.address(), random.randint(10000, 99999),random.choice(ShipM), 
                random.choice(PayM), random.randint(1, 25), faker_gen.address(), faker_gen.phone_number(), faker_gen.phone_number(), random.randint(1, 25) )
    
    cursor.execute(query13, values13)

db.commit()

print(cursor.rowcount)

#////////////////////////////////////
query14 = "INSERT INTO orderitems(Customer_OrderID, Ordered_Quantity, Product_VariationID, Product_PriceID) VALUES (%s, %s, %s, %s)"

for i in range(25):
    
    values14 = (random.randint(1, 25), random.randint(1, 250), random.randint(1, 25), random.randint(1, 25))
    
    cursor.execute(query14, values14)

db.commit()

print(cursor.rowcount)

#/////////////////////////////////
query15 = "INSERT INTO product_variation_has_product_options(Product_VariationID, Product_OptionsID) VALUES (%s, %s)"

for i in range(25):
    
    values15 = (random.randint(1, 25), random.randint(1, 25))
    
    cursor.execute(query15, values15)

db.commit()

print(cursor.rowcount)













