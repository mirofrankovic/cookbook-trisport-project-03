import os
from flask import Flask, render_template, url_for, redirect, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook_trisport'
app.config["MONGO_URI"] = 'mongodb://mirof:Vanilia123@ds159185.mlab.com:59185/cookbook_trisport'


mongo = PyMongo(app)




@app.route('/')
@app.route('/get_race')
def get_race():
    return render_template('getrace.html',
                          recipes = mongo.db.recipes.find())
                          
@app.route('/get_recipes') # images for my recepies
def get_recipes():
    return render_template('recipes.html',
                          recipes = mongo.db.recipes.find())
                          
                          
                          
@app.route('/add_recipe')
def add_recipe():
    
    
    return render_template('add_recipe.html',
                           author_name=mongo.db.author_name.find(),
                           meal_type=mongo.db.meal_type.find(),
                           sport_type=mongo.db.sport_type.find(),
                           race_day=mongo.db.race_day.find()
                          )
                          
                          
                          
                          
                          
@app.route('/contact_us')
def contact_us():
    return render_template("contactus.html")
                          
                          
                           
                           
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)