# Miro does Snack - Cookbook for triathlon athleetes today | Code Institute - Milestone project 03

![imageForProjec](https://user-images.githubusercontent.com/28025554/99586951-4f9c7980-29e0-11eb-9274-b4083a5e4d75.PNG)

In this project I should be able to show that I can create a web application using [Python 3](https://www.python.org/download/releases/3.0/) and [Flask](https://flask.palletsprojects.com/en/1.1.x/) which works with cloud **MongoDB Atlas** database.

## Code Institute Brief

**CREATE AN ONLINE COOKBOOK**

* Create a web application that allows users to store and easily access cooking recipes.  The purpose of this project is to "Create a web application that allows users to store and easily access cooking recipes",
  using the CRUD operations of Create, Read, Update, and Delete for their recipes.

* Put some effort into designing a database schema based on recipes.This application will access into designing a database schema based on recipes, and any other related properties and entities 
  (e.g. views, upvotes, recipe authors…).

* The brief was to create a web application that allows users to store and easily access cooking recipes.
  The recipes are to be stored in a database which can be filtered by a user on the website using the categories.
  It is a **(data-driven)** application, and the target audience is any user targeted towards athletes working out for their competition.

* In addition we create the backend code to retrieve a list of recipes, filtered based on various criteria (e.g. pre race meal, race meal, post race meal etc…)
  and order them based on some reasonable aspect (e.g. number of sport type, race day type meal). Create a frontend page to display these,
  and to show some summary statistics around the list (e.g. number of runners, cyclist, swimmers..). Optionally, add support for pagination, when the number of results is large.
  Create a detailed view for each recipes, that would just show all attributes for that recipe, and the full picture of athletes favouraite meals.
  Allow for editing and deleting of the recipe records, either on separate pages, or built into the list/detail pages.

## UX

I am an athlete and I like meals with good nutritions. I always wanted to know which meal is good to eat before race to load more energy day before my race
or during the race and the most importantly what to eat after race for recovery. I search around the web first to get a general idea of the design and data required for this project.

Therefore, I decided to create a cooking website which will be used by all users especially for athleetes who are busy with study, work, 
extra curricular activities, coming up with quick meals before, during or after workout. The purpose of this project is to create a structure of all meals by athletes prepering for training or for a race.
Therefore, specify meals by type of sport or specific requirementsn consuming a specific meal before, during or after race or training. 

The idea is to show the new meal and provide a recomendation with amout of proteins, carbohydrates etc. for an athlete. 

I designed the site so that users can share recipes and rate them accordingly. User only with created account can rate the recipe and is allowed to edit/delete recipe/s only in his/her own profile.

**REQUIREMENTS**

Based on my research and brief given by Code Institute, I created the below requirements for this project.

**Database**
* Create schema based on structure of the recipe/s found
* Create schema for user
* Create different collections for all above

**User Stories**

* View all recipes as a Guest.
* View the recipes from any device (mobile, tablet, desktop).
* See recipes from other users to get new ideas.
* Search any specific recipe by different category.
* Easily see all of the recipes I have submitted.
* Create profile, login and add my recipes.[Creatre]
* Get the instruction to make a dish from this site.[Read]
* Easily see all of the recipes I have submitted.
* User should be able to edit[Edit] / delete[Delete] only his own recipe/s.
* Be able to see the visual dashboard / graphs of the recipes by category. 

**Pages**

Create 6-7 pages for this project.

**In order for the target audience to achieve these things when visiting my website, I incorporated the following:**

* As an athlete, prepering for the next season, I would like to know what to eat to keep myself fit during the winter preparation.
* As an athlete, preparing for the race, I would like to learn what to eat a couple days before my race day.
* As an athlete, competing during the race day, I would like to know how to keep myself full loaded with my nutritions.
* As an athlete, finishing my race, I would like to know what to eat afther my race for my recovery.

## Demo

A demo of this site is available [here](https://cookbook-trisport-project-03.herokuapp.com/)

This app is hosted by GitHub Pages, a static site hosting service which supports client-side code.

## Layout

**Framework**

* The layout used the [Materialize CSS Parallax template](https://materializecss.com/templates/parallax-template/preview.html) which I modified to suit my own requirements.
* [Flask 1.0.2](https://palletsprojects.com/p/flask/) is the micro web framework that runs the application.
* [jQuery 3.4.1](https://code.jquery.com/jquery/)Used to manipulate the DOM, for example buttons, and showing / hiding elements.
* [Crossfilter](https://square.github.io/crossfilter/) to manage the data that lie behind charts.

**Database**

For the database, I choose MongoDB and this was a great oppertunity to get experience using NoSQL database MongoDB.

The database is made up of the following collections.

**forms**
```
id: <ObjectId()>
meal_type_name:<string>
sport_type_name:<string>
vegan_type_name:<string>
race_day_name:<string>
```
**meal_type**
```
id: <ObjectId()>
meal_type_name:<string>
```
**race_day**
```
id: <ObjectId()>
race_day_name:<string>
```
**sport_type**
```
id: <ObjectId()>
sport_type_name:<string>
```
**vegan_meal**
```
id: <ObjectId()>
vegan_type_name:<string>
```
**recipes**
```
id: <ObjectId()>
author_name:<string>
recipe_name:<string>
meal_type_name:<string>
sport_type_name:<string>
race_day_name:<string>
description:<string>
image_recipe:<string>
vegan_type_meal:<string>
due_date:<string>
likes:<int32>
```
**servings**
```
id: <ObjectId()>
proteins_unit:<string>
carbohydrates_unit:<string>
calories_name:<string>
```
**users**
```
id: <ObjectId()>
author_name:<string>
password:<string>
likes:<Array>
```

## Features

In this section I will describe the front-end features of my project:

**1. Navbar**

* Consists of the PREPARE FOR YOUR RACE logo which also returns the user to the "Home" page of the application.
  My navbar also has links to **All Recipes**, **Dashboard**, **Login**. After LoggedIn, the user will be able to find his/her **Profile** file and also will be able to **Logout** from the profile page.
  The navbar will appear in all pages with the same functions for all links.
         
**2. Home Page**

* Consists of one background image along with some information for a new user to create a user profile to share recipes with other users. 
    
**3. All_Recipes**

* Directs the user to the "All Recipes" page which displays ALL recipes from ALL users which have been entered on the site. 
  The user can then filter or browse through the recipes. The can view more information on each recipe by selectign the "See Recipe Description" link which delivers the user to the "Recipe Detail" page. 

**4. Recipe_Detail**

* Provides users with the recipe details containg a recipe name, description, image (if available), flavour, meal type, race day, sport type, nutrition wise type of meal, author and date posted.

**5. My_Recipes**

* Provides the user with the recipes that they have added themselves. The user's recipes can be edited and deleted by using the buttons displayed under the recipes.

**6. Login**

* When is the account created the user will be prompted to create a new profile to the application so that they can add recipes to the database.

**7. Register**

* When first selected the user will be prompted to create a username and password to create a new account to the application.

**8. Dashboard**

* Once logged in the user will be presented with their dashboard which provides a count of their recipes, along with 4 data **charts** depicting the number of favourite meal type, favourite sport type, favourite race day and meal associated for the vegan.

**9. Contact_Us**

* Delivers the user to the contact page. This page displays a blank form, which allows users to contact the website developers to offer feedback and suggestions (not currently wired up to an email address as this is not a real business). 
  Their are also 4 social media buttons so that the user may interact on social networks.

**10. Social_Links**

* Provides users with links to the website social media pages.

**11. 404**

* Allow user to get back to `404.html` after 404 error.

**12. Footer**

* Consists the contact form and social links with additional copyright information.

**Search recipe**

`Search`

* `Search`
Construct a query based on user input/s and return it's results.
All methods which sending quires to MongoDB Atlas can return `None` if no documents are found.
-   `find_one_by_id()`
    Return single document for given `_id`.
-  `pagination()`
    Return dictionary containing data for pagination. 
-  `__len__()`
    Return number of documents in given collection.

-   `Recipes(Search)` If a user would like to search for something specific with the name, they have a search button on the all recipe page.
-   `search_term` 
Stage which add the formated filters selected by user.
-   `search_form_button`
Return dictionary of filters in form of key and list of values. Example: `{'raceDay': ['pre race', 'race', 'post race'], 'veganMeal': ['yes', 'no']}` 

* `Database`
Used to update tags for edit_recipe.html.
-   `update()` Search for existing tags and return them in form of in form of key and list of values.

* `Charts`
Construct data for dashboard.html and return them.

-   `show_meal_type_graph()` Construct graph data which shows User's vs. Database recipes in total in form of chart.
-   `dc.barChart("#meal_type-graph")` Construct graph data which shows User's vs. Database recipes in total for selected tag in form of chart.

**CRUD operations of Create, Read, Update, and Delete for their recipes.**

* **Add a Recipe**
[**C**RUD] **C**reate or 'add' a new recipe.

Logged in users can add their recipes. For selective fields,user can select the options from drop down.
All the fields of the form is well explained with the 'placeholder' to make it easy for the user.

* **View Recipe**
[C**R**UD] **R**ead or 'review' recipes, either from the home page, or the user recipes page.

The logged in user can like the recipe one time. If the user viewing is the user who submitted, they will have additional options edit and delete. 
Delete button allow the user to completely remove the recipe from the database.

* **Update Recipe**
[CR**U**D] **U**pdate or 'edit' their own user recipes on this page.

The edit recipe form is identical in layout to the add recipe form, and very similar in functionality. 
User can either save or cancel the changes by clicking the appropriate buttons.

* **Delete Recipe**
[CRU**D**] **D**elete or 'remove' a user's own recipes.

If the user clicks the delete button, a popup modal will appear asking for confirmation. If the user still choose to delete,
the recipe will be permanently deleted.

* **User's Profile**

Each user has their own account page, there they can view all the recipes they have added and can go for edit recipe from there aswell.

* **Flashed Messages**

The app uses the flask flash method to communicate important events to the user and make it user friendly.


# Getting Started / Deployment

* If you wish to run this site locally, please clone or download this repo. You can then run index.html or open index.html in your browser.
* If you wish to deploy a live version of this site, then you will need to create your own GitHub repo. Navigate to settings and enable GitHub Pages by setting the Source to master branch.

## Technologies Used

**Languages**

* [HTML](https://en.wikipedia.org/wiki/HTML)
   This project uses HTML, the standard mark-up language used to build website layout, which is included within the `.html` files.

* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
   This project uses CSS, a style sheet language, used to add styling to a website. The `.css` file was added to this project, to add additional styling on top of the Bootstrap template.

* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
   This project uses JavaScript, an object-oriented programming language used to create interactive effects within web browsers. JavaScript within this project was included with the Bootstrap template.

* [Python 3](https://www.python.org/)
   This project uses Python, an interpreted high-level programming language for general-purpose programming and used to write the logic of this game, which is included within `.py` files.

**Libraries**

* [Font Awesome](https://fontawesome.com/)
   This project uses Font Awesome, vector icons and social logos on the website.

* [Materialize CSS](https://materializecss.com/)
   Created and designed by Google, Material Design is a design language that combines the classic principles of successful design along with innovation and technology. 
   Google's goal is to develop a system of design that allows for a unified user experience across all their products on any platform.

* [Google Fonts](https://fonts.google.com/)
   Provided the fonts used throughout the project.

* [jQuery](https://jquery.com/)   
   Used as the primary JavaScript functionality.

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
   This project uses Flask, a Python micro-framework. It is classified as a microframework because it does not require particular tools or libraries.

* [Jinga](https://jinja.palletsprojects.com/en/2.11.x/)
   This project uses Jinja, a template engine for Python, jinja code is included within the curly brackets.

* [PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
   2.3.0 was used to enable the python application to access the Mongo database.

* [Bootstrap](https://getbootstrap.com/)
   This project used Bootstrap, a library of website themes. The [Materialize CSS Parallax template](https://materializecss.com/templates/parallax-template/preview.html), was used for this project.

* [Dc](https://dc-js.github.io/dc.js/)
    This `dc.js` is a javascript charting library with native [crossfilter](http://crossfilter.github.io/crossfilter/) support, allowing highly efficient exploration on large multi-dimensional datasets.
    It leverages [d3](https://d3js.org/) to render charts in CSS-friendly SVG format. Charts rendered using `dc.js` are data driven and reactive and therefore provide instant feedback to user interaction.

* [Crossfilter](http://crossfilter.github.io/crossfilter/)
   Is a **JavaScript** library for exploring large multivariate datasets in the browser.

**Hosting**

* [Heroku](https://www.heroku.com/home)
   This project uses Heroku, a web hosting service that supports Python applications, for final project deployment.

**Tools**

* [Gitpod](https://www.gitpod.io/docs/)
  Open-source tech. This project used Gitpod, an online integrated development environment, to construct the code end to end.

* [MongoDB Atlas](https://www.mongodb.com/)
   This project uses MongoDB Atlas, a free and open-source cross-platform document-oriented database program.
   Classified as a NoSQL database program, MongoDB uses JSON-like documents with schemata.  

* [GitHub](https://github.com/)
   This project uses GitHub, a web hosting service, for version control and final project backup.   

* [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools/)
   This project uses Chrome Dev Tools, a set of web developer tools, to continuously test and inspect that the web pages are rendering as intended within the browser.

* [Am I Responsive](http://ami.responsivedesign.is/#)

# Testing

Most of the testing was manual testing during the development of the site with additional testing completed at the end, before this write up.

Also, created my own profile and was adding recipes with various categories to test
my charts in terms of counting recipes and puting in right meal_type, sport_type, race_day or vegan meal.

## Manual Testing

* **Front End**

* [W3C Markup Validation Service](https://validator.w3.org/)
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
* [JSHint](https://jshint.com/)

* **Back End**

* [PEP8 Online](http://pep8online.com/) Was used to validate Python.

* Add Recipe Page:
1. Go to the "Add Recipe" page.
2. Try to submit the empty form and verify that the recipe will not submit without a RECIPE NAME.
3. Try to submit the form without description and verify that the recipe will not submit without a RECIPE DESCRIPTION.

* Responsive Testing

The app was tested on Apple iPhone 6, Apple iPad Air 2 and also using the Google Chrome inspect feature to test for repsonsiveness and any errors that occurred.
The main issue which was found was the sidevar/ navbar not resizing.

# Deployment

* [Python 3](https://www.python.org/) and [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/) was used to build the application.
1. Created [requirements.txt](https://github.com/mirofrankovic/cookbook-trisport-project-03/blob/master/requirements.txt) that Heroku knows which packages are required for the application to run and install them.
2. Created [Procfile](https://github.com/mirofrankovic/cookbook-trisport-project-03/blob/master/Procfile) that Heroku knows what kind of application is this.

The following section describes the process to deploy this project to **Heroku**.

1. Ensure all required technologies are installed locally, as per the `requirements.txt` file.
2. Login to Heroku, using 'heroku login' command. Input Heroku login details.
3. Create new Heroku app, using 'heroku apps:create appname' command.
4. Push project to Heroku, using 'push -u heroku master' command.
5. Create scale, using 'heroku ps:scale web=1' command.
6. Login to Heroku and select newly created app.
7. Select settings. Select ‘Reveal Config'. Add IP 0.0.0.0 and PORT 5000.
8. From 'More' menu on the top right, select 'Restart all dynos'.
9. View app: In settings, select Domain URL, NOT Git URL to view your hosted application.
10. Deployed via [Heroku](https://cookbook-trisport-project-03.herokuapp.com/)
Free cloud hosting platform which simplify the deployment process.

* **Deploy**
* Connected the app to GitHub project.
* Enabled automatic deploys from master branch.
* Deployed the branch manually.

## What to do to run our project locally.

Please note that the project can not be run locally without database user name and password.

Due to the security reasons I do not publish any of those and therefore the project can not be really run locally.

1. Download and install [Python 3](https://www.python.org/).
2. Clone or download the project. In case, you downloaded the project manually you must unpack it after.
3. Open your **Command line (CLI)** inside the project root or navigate to it.
4. [Create virtual environment (venv)](https://docs.python.org/3/tutorial/venv.html) (by your choice it is optional)
Activate venv source `venv/bin/activate` where `"venv"` is the name of your virtual environment.
5. Install required packages via **CLI**.
`pip install -r requirements.txt`
6. Set **venv** variables.
* `IP 0.0.0.0`
* PORT `5000`
* MONGO_URI such as `mongodb://<dbuser>:<dbpassword>@ds225442.mlab.com:25442/<dbname>`
* SECRET_KEY `my_secret_key`
* DEVELOPMENT (optional)
7. Run the application
* `python app.py`
8. The application should now run on your localhost:5000.

# Credits
## Content

* The recipes came from the [BBC FOOD](https://www.bbc.co.uk/food/diets/healthy) website.

## Media

* The photos used in this site were obtained from the [BBC FOOD](https://www.bbc.co.uk/food/diets/healthy) website.

## Acknowledgements

**Tutorials**

[https://www.tutorialspoint.com](https://www.tutorialspoint.com/index.htm)

[https://stackoverflow.com](https://stackoverflow.com/)

* I received inspiration for this project from [BBC FOOD](https://www.bbc.co.uk/food/diets/healthy) website with the combination of [Nutritionist Resource](https://www.nutritionist-resource.org.uk/) website.

## In Conclusion

* I would like to thank my mentor Guido Cecilio Garcia Bernal and the Code Institute for their support. 
