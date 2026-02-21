from flask import Flask,render_template
import mysql.connector


app = Flask(__name__)


db = mysql.connector.connect(host='localhost', user='test', password='test', database='eshop_database')

@app.route('/')
def select():
    
    
    cursor = db.cursor()
    query = "SELECT Product_Name,Description,pComment_Content,Customer_FirstName,Customer_LastName FROM products INNER JOIN product_variation ON products.ProductID = product_variation.ProductID INNER JOIN product_comments ON product_variation.Product_VariationID = product_comments.Product_VariationID INNER JOIN customers ON product_comments.CustomerID = customers.CustomerID"
    cursor.execute(query)
    data = cursor.fetchall()
    
    
    return  render_template("Query1.html", data = data,query = query)


if __name__ == "__main__":
    app.run( port = 5000 ,debug=True)











