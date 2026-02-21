from flask import Flask,render_template
import mysql.connector


app = Flask(__name__)


db = mysql.connector.connect(host='localhost', user='test', password='test', database='eshop_database')

@app.route('/')
def select():
    
    
    cursor = db.cursor()
    query2 = "SELECT Customer_FirstName,Customer_LastName,Product_Name,Description,Ordered_Quantity,OrderDate,Shop_Name FROM customers INNER JOIN customerorders ON customers.CustomerID = customerorders.CustomerID INNER JOIN shops ON customerorders.ShopID = shops.ShopID INNER JOIN orderitems ON customerorders.Customer_OrderID = orderitems.Customer_OrderID INNER JOIN product_variation ON orderitems.Product_VariationID = product_variation.Product_VariationID INNER JOIN products ON product_variation.ProductID = products.ProductID"
    cursor.execute(query2)
    data2 = cursor.fetchall()
    
    return  render_template("Query3.html", query2 = query2,data2=data2)


if __name__ == "__main__":
    app.run( port = 4980 ,debug=True)