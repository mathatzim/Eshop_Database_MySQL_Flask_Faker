from flask import Flask,render_template
import mysql.connector


app = Flask(__name__)


db = mysql.connector.connect(host='localhost', user='test', password='test', database='eshop_database')

@app.route('/')
def select():
    
    
    cursor = db.cursor()
    query3 = "SELECT  Shop_Name,sComment_Content,sComment_Rating,sComment_Date,Customer_FirstName,Customer_LastName FROM shop_comments INNER JOIN shops ON shop_comments.ShopID = shops.ShopID INNER JOIN customers ON shop_comments.CustomerID = customers.CustomerID WHERE shop_comments.CustomerID = 23"
    cursor.execute(query3)
    data3 = cursor.fetchall()
    
    return  render_template("Query4.html", query3 = query3,data3=data3)


if __name__ == "__main__":
    app.run( port = 4970 ,debug=True)