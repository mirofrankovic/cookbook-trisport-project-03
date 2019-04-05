import pymongo 
import os
from flask import Flask, render_template, url_for, redirect, session, request
import json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook_trisport'
app.config["MONGO_URI"] = 'mongodb://mirof:Vanilia123@ds159185.mlab.com:59185/cookbook_trisport'


mongo = PyMongo(app)




@app.route('/')
@app.route('/get_ready')
def get_ready():
    return render_template('getready.html',
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
    return render_template('login.html',
                           author_name=mongo.db.author_name.find(),
                           meal_type=mongo.db.meal_type.find(),
                           sport_type=mongo.db.sport_type.find(),
                           race_day=mongo.db.race_day.find()
                          )
                          
                          
                          
@app.route('/insert_my_recipe/<recipe_id>')    #edit_recipe
def insert_my_recipe(recipe_id):
    this_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('insert_my_recipe.html', recipe=this_recipe)




#@app.route('/update_my_recipe/<recipe_id>', methods=['POST'])
#def update_my_recipe(recipe_id):



@app.route('/submit_to_database', methods=['POST'])
def submit_to_database():
    recipes=mongo.db.recipes
    
    recipes.insert_one(request.json)
    
    return('', 204) # what is 204
    
                          
                          
@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    
    
    loggedin = False
    if request.method == 'GET' and not 'username' in session:
        return render_template('login.html',
                               loggedin=loggedin)
    elif request.method == 'GET' and 'username' in session:
        loggedin = True
        recipes = mongo.db.recipes.find()
        recipes_dics = {}
        
        for i, recipe in enumerate(recipes):
            recipe.pop('_id', None)
            recipes_dics[i] = recipe
            
            recipes_dics = json.dumps(recipes_dics)
            
            
            return render_template('login.html',
                                    username=session['username'],
                                    loggedin=loggedin,
                                    recipes=recipes_dics)
                                    
        if request.method == 'POST':
            session['username'] = request.form["username"]
            loggedin = True
            recipes=mongo.db.recipes.find()
            recipes_dics = {}
            
            for i, recipe in enumerate(recipes):
                recipe.pop('_id', None)
                recipes_dics[i] = recipe
                
            recipes_dics = json.dumps(recipes_dics)  
            
            return render_template('login.html',
                                   username=session['username'],
                                   loggedin=loggedin,
                                   recipes=recipes_dics)
        
        
        
        
      
                          




@app.route('/contact_us')
def contact_us():
    return render_template("contactus.html")
                          
                          
                           
                           
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)