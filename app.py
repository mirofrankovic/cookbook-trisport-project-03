import math
import pymongo
import os
from flask import Flask, render_template, url_for, redirect, session, request, flash, jsonify, abort
import json
from pymongo import MongoClient
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson import json_util
from bson.json_util import dumps
from bson.errors import InvalidId

from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

MONGODB_URI = os.getenv('MONGO_URI')
DBS_NAME = "cookbook_trisport"
COLLECTION_NAME = "recipes"

# -----Pagination and sorting params variables ----- #
PAGE_SIZE = 3
KEY_PAGE_SIZE = 'page_size'
KEY_PAGE_NUMBER = 'page_number'
KEY_TOTAL = 'total'
KEY_PAGE_COUNT = 'page_count'
KEY_ENTITIES = 'items'
KEY_NEXT = 'next_uri'
KEY_PREV = 'prev_uri'
KEY_SEARCH_TERM = 'search_term'
KEY_ORDER_BY = 'order_by'
KEY_ORDER = 'order'

mongo = PyMongo(app)  # constructor method

forms_collection = mongo.db.forms

def get_paginated_items(entity, query={}, **params):  # function
    page_size = int(params.get(KEY_PAGE_SIZE, PAGE_SIZE))
    page_number = int(params.get(KEY_PAGE_NUMBER, 1))
    order_by = params.get(KEY_ORDER_BY, '_id')
    order = params.get(KEY_ORDER, 'asc')
    order = pymongo.ASCENDING if order == 'asc' else pymongo.DESCENDING

    # If statement to avoid any pagination issues
    if page_number < 1:
        page_number = 1
    offset = (page_number - 1) * page_size
    items = []

    # Updated section allow user to paginate a filtered/sorted "query"
    search_term = params.get(KEY_SEARCH_TERM, '')
    if bool(query):
        items = entity.find(query).sort(order_by, order).skip(
            offset).limit(page_size)
    else:
        if search_term != '':
            entity.create_index([("$**", 'text')])
            result = entity.find({'$text': {'$search': search_term}})
            items = result.sort(order_by, order).skip(offset).limit(page_size)
        else:
            items = entity.find().sort(
                order_by, order
            ).skip(offset).limit(page_size)

    total_items = items.count()

    if page_size > total_items:
        page_size = total_items
    if page_number < 1:
        page_number = 1
    if page_size:
        page_count = math.ceil(total_items / page_size)
    else:
        page_count = 0
    if page_number > page_count:
        page_number = page_count
    next_uri = {
        KEY_PAGE_SIZE: page_size,
        KEY_PAGE_NUMBER: page_number + 1
    } if page_number < page_count else None
    prev_uri = {
        KEY_PAGE_SIZE: page_size,
        KEY_PAGE_NUMBER: page_number - 1
    } if page_number > 1 else None

    return {
        KEY_TOTAL: total_items,
        KEY_PAGE_SIZE: page_size,
        KEY_PAGE_COUNT: page_count,
        KEY_PAGE_NUMBER: page_number,
        KEY_NEXT: next_uri,
        KEY_PREV: prev_uri,
        KEY_SEARCH_TERM: search_term,
        KEY_ORDER_BY: order_by,
        KEY_ORDER: order,
        KEY_ENTITIES: items
    }

@app.route('/')
@app.route('/get_ready')
def get_ready():
    # supply recipes collection
    return render_template('getready.html', recipes=mongo.db.recipes.find(), forms=mongo.db.forms.find())

# images for my recepies and see all my recipes after adding them
@app.route('/get_recipes', methods=['GET', 'POST'])
def get_recipes():
    if request.method == 'GET':
        params = request.args.to_dict()  
    else:
        params = request.form.to_dict()
    # print(params)
    paginated_recipes = get_paginated_items(mongo.db.recipes, **params)
    return render_template('recipes.html', paginated_recipes=paginated_recipes)

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get("query")
    paginated_recipes = get_paginated_items(
        mongo.db.recipes, {"$text": {"$search": query}})
    return render_template("recipes.html", paginated_recipes=paginated_recipes)

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
    try:
        this_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    except InvalidId as e:
        abort(404, 'Recipe not found!')
    else:
        if this_recipe is None:
            abort(404, 'Recipe not found!')
    return render_template('recipedescription.html', recipe=this_recipe)

@app.route('/add_recipe')  
def add_recipe():
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
                           calories_name=mongo.db.calories_name.find(),
                           due_date=mongo.db.due_date.find()
                           )
@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {       
            'author_name': request.form.get('author_name'),
            'recipe_name': request.form.get('recipe_name'),
            'meal_type_name': request.form.get('meal_type_name'),
            'sport_type_name': request.form.get('sport_type_name'),
            'race_day_name': request.form.get('race_day_name'),
            'description': request.form.get('description'),
            'image_recipe': request.form.get('image_recipe'),
            'vegan_type_meal': request.form.get('vegan_type_meal'),
            'servings': request.form.get('servings'),
            'proteins_unit': request.form.get('proteins_unit'),
            'carbohydrates_unit': request.form.get('carbohydrates_unit'),
            'calories_name': request.form.get('calories_name'),
            'due_date' : request.form.get('due_date')

        }
        try:
            mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
            flash("Recipe Successfully Updated!")
        except InvalidId as e:
            abort(404, 'Recipe not found!')
        except Exception as e:
            abort(500, 'Unknown exception found!')
    
    try:
        this_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    except InvalidId as e:
        abort(404, 'Recipe not found!')
    else:
        if this_recipe is None:
            abort(404, 'Recipe not found!')
    
    return render_template('edit_recipe.html', recipe=this_recipe,
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
                           calories_name=mongo.db.calories_name.find(),
                           due_date=mongo.db.due_date.find()
                           )

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
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())  
    return redirect(url_for('get_recipes'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"author_name": request.form.get("author_name").lower()})

        if user_exists:
            if check_password_hash(
                    user_exists["password"], request.form.get("password")):
                session["author"] = request.form.get("author_name").lower()
                flash("Ahoj! {}".format(
                    request.form.get("author_name")))
                return redirect(url_for(
                    "my_recipes", author_name=session["author"]))
            else:
                # invalid password match
                flash("Incorect Author Name or/and Pasword")
                return redirect(url_for("login"))

        else:
            flash("Incorect Author Name or/and Pasword")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_exists = mongo.db.users.find_one(
            {'author_name': request.form.get('author_name').lower()})

        if user_exists:
            flash('Username already exists, please choose a different one.')
            return render_template('register.html', title="Register")

        register = {
            "author_name": request.form.get("author_name").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "likes": []
        }
        mongo.db.users.insert_one(register)
        session["author"] = request.form.get("author_name").lower()
        flash("Athlete Has Registrated Succesfuly!")
        return redirect(url_for("my_recipes", author_name=session["author"]))

    return render_template('register.html', title="Register")

@app.route('/log_out')
def log_out():
    print('logged out')
    session.clear()
    return redirect(url_for('get_ready'))


@app.route('/delete_my_recipe/<recipe_id>')
def delete_my_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted!")
    return redirect(url_for("my_recipes", author_name=session["author"]))

@app.route('/my_recipes/<author_name>', methods=['GET', 'POST'])
def my_recipes(author_name):
    if session.get("author") is None:
        return redirect(url_for('login'))

    if not author_name:
        author_name = session["author"]
    elif author_name != session["author"]:
        return redirect(url_for('login'))

    user = mongo.db.users.find_one({"author_name": author_name})
    if user:
        author_name = user['author_name']
        paginated_recipes = get_paginated_items(mongo.db.recipes,
                                      query={'author_name': author_name},
                                      **request.args.to_dict())
        return render_template('my_recipes.html',
                               author_name=session['author'],
                               paginated_recipes=paginated_recipes)
    else:
        return redirect(url_for('login'))

@app.route('/popular_recipe/<recipe_id>', methods=['GET', 'POST'])
def popular_recipe(recipe_id):
    if request.method == "POST":
        current_user = mongo.db.users.find_one(
            {"author_name": session["author"]})
        user = mongo.db.users

        my_popular = user.find({"$and": [{"author_name": session['author']},
                                         {'likes': recipe_id}]})

    
        if recipe_id not in current_user["likes"]:
            mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)},
                                        {'$inc': {'likes': 1}})

            user.update_one({"author_name": session['author']},
                            {"$push": {"likes": recipe_id}})

        else:

            flash("You have already liked this recipe!")

    return redirect(url_for('recipedescription', recipe_id=recipe_id))

@app.route('/dashboard')
def dashboard():
    forms = forms_collection.find()
    return render_template('dashboard.html')

@app.route('/contact_us')
def contact_us():
    return render_template("contactus.html")

@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = '404'), 404

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
