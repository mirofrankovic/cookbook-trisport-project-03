# Miro does Snack - Cookbook for triathlon athleetes today | Code Institute - Milestone project 03

In this project I should be able to show that I can create a web application using [Python3](https://www.python.org/download/releases/3.0/) and [Flask](https://flask.palletsprojects.com/en/1.1.x/) which works with cloud **MongoDB Atlas** database.

## Code Institute Brief

**CREATE AN ONLINE COOKBOOK**

* Create a web application that allows users to store and easily access cooking recipes

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

I am an athlete and I like meals with good nutritions, I search around the web first to get a general idea of the design and data required for this project.

Therefore, I decided to create a cooking website which will be used by all users especially for athleetes who are busy with study, work, 
extra curricular activities, coming up with quick meals before, during or after workout.

The idea is to show the new meal and provide a recomendation with amout of proteins and carbohydrates for an athlete. 

I designed the site so that users can share recipes and rate them accordingly.

**REQUIREMENTS**

Based on my research and brief given by Code Institute, I created the below requirements for this project.

**Database**
* Create schema based on structure of the recipe/s found
* Create schema for user
* Create different collections for all above

**Users**

User should be able to edit / delete only his own recipe/s.

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

The layout used the [Materialize CSS Parallax template](https://materializecss.com/templates/parallax-template/preview.html) which I modified to suit my own requirements.

## Features

In this section I will describe the front-end features of my project:

**1. Navbar**

* Consists of the PREPARE FOR YOUR RACE logo which also returns the user to the "Home" page of the application.
  My navbar also has links to "All Recipes", "Your Suggestion", "Contact Us", "Dashboard", "Login". The navbar will appear in all pages with the same functions for all links.
         
**2. Home**

* Consists of one background image along with some information on contacting the webmaster and a link to the contact us page of the site. 
    
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

* Once logged in the user will be presented with their dashboard which provides a count of their recipes, along with 4 data charts depicting the number of favourite meal type, favourite sport type, favourite race day and meal associated for the vegan.

**9. Contact_Us**

* Delivers the user to the contact page. This page displays a blank form, which allows users to contact the website developers to offer feedback and suggestions (not currently wired up to an email address as this is not a real business). 
  Their are also 4 social media buttons so that the user may interact on social networks.

**10. Social_Links**

* Provides users with links to the website social media pages.

**11. 404**

* Allow user to get back to `404.html` after 404 error.

**12. Footer**

**Helper**

`Search`

* `Search`
Construct a query based on user input/s and return it's results.
All methods which sending quires to MongoDB Atlas can return `None` if no documents are found.
* `find_one_by_id()`
    Return single document for given `_id`
* `pagination()`
    Return dictionary containing data for pagination 
* `__len__()`
    Return number of documents in given collection

# GETTING STARTED / DEPLOYMENT

* If you wish to run this site locally, please clone or download this repo. You can then run index.html or open index.html in your browser.
* If you wish to deploy a live version of this site, then you will need to create your own GitHub repo. Navigate to settings and enable GitHub Pages by setting the Source to master branch.

## Technologies Used

* [Gitpod](https://gitpod.io/workspaces/)
   This project used Gitpod, an online integrated development environment, to construct the code end to end.

* [Bootstrap](https://getbootstrap.com/)
   This project used Bootstrap, a library of website themes. The [Materialize CSS Parallax template](https://materializecss.com/templates/parallax-template/preview.html), was used for this project.

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
   This project uses Flask, a Python micro-framework. It is classified as a microframework because it does not require particular tools or libraries.

* [mLab](https://mlab.com/)
   This project uses mLab, a fully managed cloud database service that hosts MongoDB databases. mLab runs on cloud providers Amazon, Google, and Microsoft Azure, and has partnered with platform-as-a-service providers. The developer used an mLab sandbox DB, which is for learning and prototyping. 
   Json value pairs were added into the mLab document to align with the recipe wireframe.

* [MongoDB](https://www.mongodb.com/)
   This project uses MongoDB Atlas, a free and open-source cross-platform document-oriented database program.
   Classified as a NoSQL database program, MongoDB uses JSON-like documents with schemata.

* [Jinga](https://jinja.palletsprojects.com/en/2.11.x/)
   This project uses Jinja, a template engine for Python, jinja code is included within the curly brackets

* [Python](https://www.python.org/)
   This project uses Python, an interpreted high-level programming language for general-purpose programming and used to write the logic of this game, which is included within `.py` files.

* [HTML](https://en.wikipedia.org/wiki/HTML)
   This project uses HTML, the standard mark-up language used to build website layout, which is included within the `.html` files.

* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
   This project uses CSS, a style sheet language, used to add styling to a website. The `.css` file was added to this project, to add additional styling on top of the Bootstrap template.

* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
   This project uses JavaScript, an object-oriented programming language used to create interactive effects within web browsers. JavaScript within this project was included with the Bootstrap template.

* [Dc](https://dc-js.github.io/dc.js/)
    This `dc.js` is a javascript charting library with native [crossfilter](http://crossfilter.github.io/crossfilter/) support, allowing highly efficient exploration on large multi-dimensional datasets.
    It leverages [d3](https://d3js.org/) to render charts in CSS-friendly SVG format. Charts rendered using `dc.js` are data driven and reactive and therefore provide instant feedback to user interaction.

* [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools/)
   This project uses Chrome Dev Tools, a set of web developer tools, to continuously test and inspect that the web pages are rendering as intended within the browser.

* [GitHub](https://github.com/)
   This project uses GitHub, a web hosting service, for version control and final project backup.

* [Heroku](https://www.heroku.com/home)
   This project uses Heroku, a web hosting service that supports Python applications, for final project deployment.

* [Font Awesome](https://fontawesome.com/)
   This project uses Font Awesome, vector icons and social logos on the website.

* [Materialize CSS](https://materializecss.com/)
   Created and designed by Google, Material Design is a design language that combines the classic principles of successful design along with innovation and technology. 
   Google's goal is to develop a system of design that allows for a unified user experience across all their products on any platform.

## Testing

# Manual Testing

* Add Recipe Page:

1. Go to the "Add Recipe" page.
2. Try to submit the empty form and verify that the recipe will not submit without a RECIPE NAME.
3. Try to submit the form without description and verify that the recipe will not submit without a RECIPE DESCRIPTION.

* Responsive Testing

The app was tested on Samsung S8, Apple iPhone 6, Apple iPad Air 2 and also using the Google Chrome inspect feature to test for repsonsiveness and any errors that occurred.
The main issue which was found was the sidevar/ navbar not resizing.

# Deployment

The following section describes the process to deploy this project to Heroku.

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

## Credits

# Content

* The recipes came from the [BBC FOOD](https://www.bbc.co.uk/food/diets/healthy) website.

# Media

* The photos used in this site were obtained from the [BBC FOOD](https://www.bbc.co.uk/food/diets/healthy) website.

# Acknowledgements

* I received inspiration for this project from [BBC FOOD](https://www.bbc.co.uk/food/diets/healthy) website with the combination of [Nutritionist Resource](https://www.nutritionist-resource.org.uk/) website.

# In Conclusion

* I would like to thank my mentor Guido Cecilio Garcia Bernal and the Code Institute for their support. 
