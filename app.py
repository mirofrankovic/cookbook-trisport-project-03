import pymongo 
import os
from flask import Flask, render_template, url_for, redirect, session, request, flash, jsonify
import json
from pymongo import MongoClient
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson import json_util
from bson.json_util import dumps

from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app=Flask(__name__)
app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI") 
app.secret_key = os.environ.get("SECRET_KEY")



MONGODB_URI = os.getenv('MONGO_URI')
DBS_NAME = "cookbook_trisport"
COLLECTION_NAME = "recipes"


mongo = PyMongo(app)             #constructor method


forms_collection = mongo.db.forms

 



@app.route('/')
@app.route('/get_ready')
def get_ready():
    return render_template('getready.html', recipes=mongo.db.recipes.find(), forms=mongo.db.forms.find()) #supply recipes collection
    
    
@app.route('/preparation')
def get_prepared():
    return render_template('preparation.html', recipes=mongo.db.recipes.find())# will be the second page with pre-race-post race meal to choose with static images
    
                          
                          
@app.route('/get_recipes', methods=['GET']) # images for my recepies and see all my recipes after adding them
def get_recipes():
    return render_template('recipes.html', recipes=mongo.db.recipes.find())
    

    
@app.route('/find_recipes')
def find_recipes_json():
    recipes = mongo.db.recipes.find()
    json_recipes = []
    for recipe in recipes:
        json_recipes.append(recipe)
    json_recipes = json.dumps(json_recipes, default=json_util.default)
    return json_recipes
    
    
    
@app.route('/recipedescription/<recipe_id>')
def recipedescription(recipe_id):
    this_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('recipedescription.html', recipe=this_recipe)
                          

@app.route('/add_recipe')  #only for display my recipes in my form
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
    if request.url.startswith('http://'):
        request.url = request.url.replace('http://', 'https://', 1)
    print('url when add_recipe: ', request.url)

    return render_template('add_recipe.html',
                          recipe={},
                          author_name=mongo.db.author_name.find(),
                          meal_type=mongo.db.meal_type.find(),
                          sport_type=mongo.db.sport_type.find(),
                          image_recipe=mongo.db.image_recipe.find(),
                          race_day=mongo.db.race_day.find(),
                          vegan_meal=mongo.db.vegan_meal.find(),
                          servings=mongo.db.servings.find(),
                          recipes=mongo.db.recipes.find(),
                          proteins_unit=mongo.db.proteins_unit.find(),
                          carbohydrates_unit=mongo.db.carbohydrates_unit.find(),
                          calories_name=mongo.db.calories_name.find()
                          )
                          
                          
    
                          
                          
@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])    #edit_recipe to my database
def insert_my_recipe(recipe_id):
     this_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
     return render_template('edit_recipe.html', recipe=this_recipe)
#     recipes=recipes_collection.find()
#     if request.method == "POST":
#         recipe_data = request.form.to_dict()
#         data = Recipe(recipe_data)           #helper.classes
#         data = data._dict_
#         data['visibility'] = False
#         recipes_collection.update({'_id': ObjectId(recipe_id)}, data["recipe"])
#         recipe = data["recipe"]


@app.route('/updated_edit_recipe/<recipe_id>', methods=['POST'])
def updated_edit_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.insert_one(request.json),
    {
        'author_name': request.form.get['author_name'],
        'recipe_name': request.form.get['recipe_name'],
        'meal_type_name': request.form.get['meal_type_name'],
        'sport_type_name': request.form.get['sport_type_name'],
        'race_day_name': request.form.get['race_day_name'],
        'description': request.form.get['description'],
        'image_recipe': request.form.get['image_recipe'],
        'vegan_type_meal': request.form.get['vegan_type_meal'],
        'servings': request.form.get['servings'],
        'proteins_unit': request.form.get['proteins_unit'],
        'carbohydrates_unit': request.form.get['carbohydrates_unit'],
        'calories_name': request.form.get['calories_name']
    }
    return redirect(url_for('my_recipes'))


@app.route('/get_my_form')
def get_my_form():
    if request.url.startswith('http://'):
        request.url = request.url.replace('http://', 'https://', 1)
    print('url when add_recipe: ', request.url)

    return render_template('add_recipe.html',
                          recipe={},
                          author_name=mongo.db.author_name.find(),
                          meal_type=mongo.db.meal_type.find(),
                          sport_type=mongo.db.sport_type.find(),
                          race_day=mongo.db.race_day.find(),
                          vegan_meal=mongo.db.vegan_meal.find(),
                          servings=mongo.db.servings.find())
                         
    



@app.route('/submit_to_database', methods=['POST'])
def submit_to_database():
    print(request.form.to_dict())
    recipes=mongo.db.recipes
    recipes.insert_one(request.form.to_dict())     #or (request.json)
    return redirect(url_for('get_recipes'))
                                                    #return('', 204) # what is 204
    
                          
                          
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # check id author_name exists
        user_exists = mongo.db.users.find_one(
            {"author_name": request.form.get("author_name").lower()})

        if user_exists:
            # ensure hashed password matches user input
            if check_password_hash(
                user_exists["password"], request.form.get("password")): 
                    session["author"] = request.form.get("author_name").lower()
                    flash("Welcome, {}".format(request.form.get("author_name"))) 
            else:
                # invalid password match
                flash("Incorect Author Name or/and Pasword") 
                return redirect(url_for("login"))   

        else:
            # author_name doesn't exist
            flash("Incorect Author Name or/and Pasword") 
            return redirect(url_for("login"))  
                      
        return render_template("login.html")




    
#    logged_in = False
#    if request.method == 'GET' and not 'author_name' in session:     #username
#        return render_template('login.html', logged_in=logged_in)
#    elif request.method == 'GET' and 'author_name' in session:        #username
#        logged_in = True
#        recipes = mongo.db.recipes.find()
#        
#        recipes_dics = {}
#        
#        for i, recipe in enumerate(recipes):
#            recipe.pop('_id', None)
#            recipes_dics[i] = recipe
#            
#        recipes_dics = json.dumps(recipes_dics)
#        
#        return render_template('login.html', 
#                               author_name=session['author_name'],
#                               logged_in=logged_in,
#                               recipes=recipes_dics)
#    if request.method == 'POST':
#        session['author_name'] = request.form["author_name"]
#        logged_in = True
#        recipes=mongo.db.recipes.find()
#        recipes_dics = {}
#        
#        for i, recipe in enumerate(recipes):
#            recipe.pop('_id', None)
#            recipes_dics[i] = recipe
#            
#        recipes_dics = json.dumps(recipes_dics)
#            
#        return render_template('login.html',
#                              author_name=session['author_name'],
#                              logged_in=logged_in,
#                              recipes=recipes_dics)   
                              
    
   
                              
                              
                              
@app.route('/register', methods=['GET', 'POST'])
def register():
     #logging.info('Registering User')
    if request.method == 'POST':
        #session['author_name'] = request.form['author_name'].lower()
        #users = mongo.db.users
        user_exists = mongo.db.users.find_one(
            {'author_name': request.form.get('author_name').lower()})
            
        if user_exists:
            flash('Username already exists, please choose a different one.')
            return render_template('register.html', title="Register")

        register = {
            "author_name": request.form.get("author_name").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }    
        mongo.db.users.insert_one(register)
           # return redirect(url_for('login'))


        #logging.info('User already exist. Skipping new user')
        session["author"] = request.form.get("author_name").lower()
        flash("Athlete Has Registrated Succesfuly!")
        #return render_template('register.html', title="Register")
    

    return render_template('register.html', title="Register")


    

                              
@app.route('/log_out')
def log_out():
    print('logged out')
    session.clear()
    return redirect(url_for('get_ready'))
    
    
@app.route('/delete_my_recipe/<recipe_id>')
def delete_my_recipe(recipe_id):
     mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
     return redirect(url_for('my_recipes'))
        
        
    
    
@app.route('/search_form', methods=['GET', 'POST'])      #render template
def search_form():
    forms = forms_collection.find()
    
    return render_template('search_form.html', forms=mongo.db.forms.find() )
    
        






@app.route('/my_recipes', methods=['GET', 'POST'])
def my_recipes():
    if not 'username' in session:
        return redirect('/log_in')
    else:
        recipes = mongo.db.recipes.find()
        return render_template('my_recipes.html',
                           username=session['username'],
                           recipes=recipes)  
                           
                           
@app.route('/dashboard')
def dashboard():
    forms = forms_collection.find()
    
    return render_template('dashboard.html')
    



@app.route('/contact_us')
def contact_us():
    return render_template("contactus.html")
                          
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)