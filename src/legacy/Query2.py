from flask import Flask,render_template
import mysql.connector


app = Flask(__name__)


db = mysql.connector.connect(host='localhost', user='test', password='test', database='eshop_database')
@app.route('/')
def select():
    
    
    cursor = db.cursor()
    query1 = "SELECT Product_Name,Description,OrderDate,Order_Country,Order_City,Order_Address,PostalCode,Shipment_Method,Payment_Method,Shop_Name FROM orderitems INNER JOIN customerorders ON  orderitems.Customer_OrderID = customerorders.Customer_OrderID INNER JOIN shops ON customerorders.ShopID = shops.ShopID INNER JOIN product_variation ON orderitems.Product_VariationID = product_variation.Product_VariationID INNER JOIN products ON product_variation.ProductID = products.ProductID WHERE orderitems.Customer_OrderID = 24  "
    cursor.execute(query1)
    data1 = cursor.fetchall()
    
    
    return  render_template("Query2.html", query1 = query1, data1 = data1)


if __name__ == "__main__":
    app.run(port = 4990 ,debug=True)