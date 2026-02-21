from flask import Flask,render_template
import mysql.connector


app = Flask(__name__)


db = mysql.connector.connect(host='localhost', user='test', password='test', database='eshop_database')

@app.route('/')
def select():
    
    
    cursor = db.cursor()
    query5 = "SELECT ProductCategory_Description,Brand_Name,Product_Name,Description,Primary_Color,Secondary_Color,Product_Size,Vertical_Dimension,Horizontal_Dimension,Model_year,Shop_Name FROM product_categories INNER JOIN products ON product_categories.Product_CategoryID = products.Product_CategoryID INNER JOIN product_variation ON products.ProductID = product_variation.ProductID INNER JOIN product_variation_has_product_options ON product_variation.Product_VariationID = product_variation_has_product_options.Product_VariationID INNER JOIN product_options ON product_variation_has_product_options.Product_OptionsID = product_options.Product_OptionsID INNER JOIN product_color ON product_options.Product_ColorID = product_color.Product_ColorID INNER JOIN product_dimensions ON product_options.Product_DimensionsID = product_dimensions.Product_DimensionsID INNER JOIN brands ON products.BrandID = brands.BrandID INNER JOIN product_options_has_shops ON product_options.Product_OptionsID = product_options_has_shops.Product_OptionsID INNER JOIN shops ON product_options_has_shops.ShopID = shops.ShopID WHERE Product_Name = 'Keyboard'"
    cursor.execute(query5)
    data5 = cursor.fetchall()
    
    return  render_template("Query6.html", query5 = query5,data5=data5)


if __name__ == "__main__":
    app.run( port = 4950 ,debug=True)