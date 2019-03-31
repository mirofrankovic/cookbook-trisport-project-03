import pymongo 
import os
from flask import Flask, render_template, url_for, redirect, session, request
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
                          recipes = mongo.db.recipes.find()) #supply recipes collection
                          
@app.route('/get_recipes') # images for my recepies
def get_recipes():
    return render_template('recipes.html',
                          recipes = mongo.db.recipes.find())
                          
                          
                          
@app.route('/add_recipe')
def add_recipe():
    
# {
#    "_id": {
#       "$oid": "5c9bbf7ee7179a0e408e3177"
#    },
#    "author_name": "",
#    "recipe_name": "",
#    "meal_type_name": "",
#    "sport_type_name": "",
#    "race_day_name": "",
#    "description": "",
#    "image_recipe": "",
#    "vegan_type_meal": "",
#    "due_date": ""
#}   
    return render_template('add_recipe.html',
                           author_name=mongo.db.author_name.find(),
                           meal_type=mongo.db.meal_type.find(),
                           sport_type=mongo.db.sport_type.find(),
                           race_day=mongo.db.race_day.find()
                          )
                          
                          
@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    
    if request.method == 'POST':
         session['username'] = request.form["username"]
         
         
    
    
    return render_template('login.html',
                           username=session['username']
                           )
                          
                          


@app.route('/contact_us')
def contact_us():
    return render_template("contactus.html")
                          
                          
                           
                           
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)