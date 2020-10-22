# Miro does Snack - Cookbook for triathlon athleetes today | Code Institute - Milestone project 03


The brief was to create a web application that allows users to store and easily access cooking recipes.
The recipes are to be stored in a database which can be filtered by a user on the website using the categories.
It is a **(data-driven)** application, and the target audience is any user targeted towards athletes working out for their competition.

This application will access into designing a database schema based on recipes, and any other related properties and entities 
(e.g. views, upvotes, ingredients, recipe authors, allergens, cuisine etc…).

In addition we create the backend code to retrieve a list of recipes, filtered based on various criteria (e.g. allergens, cuisine, etc…)
and order them based on some reasonable aspect (e.g. number of views). Create a frontend page to display these,
and to show some summary statistics around the list (e.g. number of new recipes). Optionally, add support for pagination, when the number of results is large.
Create a detailed view for each recipes, that would just show all attributes for that recipe, and the full preparation instructions.
Allow for editing and deleting of the recipe records, either on separate pages, or built into the list/detail pages.

## UX

This application is for use by all users especially for athleetes who are busy with study, work, school,
extra curricular activities, coming up with quick meals before and after workout.
I designed the site so that users can share recipes and rate them accordingly.

**In order for the target audience to achieve these things when visiting my website, I incorporated the following:**

* As an athlete, prepering for the next season, I would like to know what to eat to keep myself fit during the winter preparation.
* As an athlete, preparing for the race, I would like to learn what to eat a couple days before my race day.
* As an athlete, competing during the race day, I would like to know how to keep myself full loaded with my nutritions.
* As an athlete, finishing my race, I would like to know what to eat afther my race for my recovery.

## DEMO

A demo of this site is available [here](https://----------------)

This app is hosted by GitHub Pages, a static site hosting service which supports client-side code.

## LAYOUT

The layout used the [Materialize CSS Parallax template](https://materializecss.com/templates/parallax-template/preview.html) which I modified to suit my own requirements.

## FEATURES 

In this section I will describe the front-end features of my project:

1. [Navbar]

* Consists of the PREPARE FOR YOUR RACE logo which also returns the user to the "Home" page of the application.
             My navbar also has links to "All Recipes", "Your Suggestion", "Contact Us", "Dashboard", "Login". The navbar will appear in all pages
             with the same functions for all links.
         
2. [Home]

* Consists of one background image along with some information on contacting the webmaster and a link to the contact us page of the site. 
    
3. [All_Recipes]

* Directs the user to the "All Recipes" page which displays ALL recipes from ALL users which have been entered on the site. 
                The user can then filter or browse through the recipes.
                The can view more information on each recipe by selectign the "See Recipe Description" link which delivers the user to the "Recipe Detail" page. 

4. [Recipe_Detail]

* Provides users with the recipe details containg a recipe name, description, image (if available), flavour, meal type, race day, sport type, nutrition wise type of meal, author and date posted.

5. [My_Recipes]

* Provides the user with the recipes that they have added themselves. The user's recipes can be edited and deleted by using the buttons displayed under the recipes.

6. [Login]

* When first selected the user will be prompted to create a username to login to the application so that they can add recipes to the database.

7. [Register]



8. [Dashboard]

* Once logged in the user will be presented with their dashboard which provides a count of their recipes, along with 4 data charts depicting the number of favourite meal type, favourite sport type, favourite race day and meal associated for the vegan.

9. [Contact_Us]

* Delivers the user to the contact page. This page displays a blank form, which allows users to contact the website developers to offer feedback and suggestions (not currently wired up to an email address as this is not a real business). 
              Their are also 4 social media buttons so that the user may interact on social networks.

10. [Social_Links]

* Provides users with links to the website social media pages.


# GETTING STARTED / DEPLOYMENT

* If you wish to run this site locally, please clone or download this repo. You can then run index.html or open index.html in your browser.
* If you wish to deploy a live version of this site, then you will need to create your own GitHub repo. Navigate to settings and enable GitHub Pages by setting the Source to master branch.


## Technologies Used

* [Cloud 9 IDE](https://aws.amazon.com/cloud9/)
   This project used Cloud 9, an online integrated development environment, to construct the code end to end.

* [Bootstrap](https://getbootstrap.com/)
   This project used Bootstrap, a library of website themes. The [Materialize CSS Parallax template](https://materializecss.com/templates/parallax-template/preview.html), was used for this project.

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
   This project uses Flask, a Python micro-framework. It is classified as a microframework because it does not require particular tools or libraries.

* [mLab](https://mlab.com/)
   This project uses mLab, a fully managed cloud database service that hosts MongoDB databases. mLab runs on cloud providers Amazon, Google, and Microsoft Azure, and has partnered with platform-as-a-service providers. The developer used an mLab sandbox DB, which is for learning and prototyping. 
   Json value pairs were added into the mLab document to align with the recipe wireframe.

* [MongoDB](https://www.mongodb.com/)
   This project uses mongoDB, a free and open-source cross-platform document-oriented database program.
   Classified as a NoSQL database program, MongoDB uses JSON-like documents with schemata.

* [Jinga](https://jinja.palletsprojects.com/en/2.11.x/)
   This project uses Jinja, a template engine for Python, jinja code is included within the curly brackets

* [Python](https://www.python.org/)
   This project uses Python, an interpreted high-level programming language for general-purpose programming and used to write the logic of this game, which is included within `.py` files.

* [HTML](https://en.wikipedia.org/wiki/HTML)
   This project uses HTML, the standard mark-up language used to build website layout, which is included within the [.html] files.

* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
   This project uses CSS, a style sheet language, used to add styling to a website. The [.css]file was added to this project, to add additional styling on top of the Bootstrap template.

* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
   This project uses JavaScript, an object-oriented programming language used to create interactive effects within web browsers. JavaScript within this project was included with the Bootstrap template.

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

1. Ensure all required technologies are installed locally, as per the [requirements.txt] file.
2. Login to Heroku, using 'heroku login' command. Input Heroku login details.
3. Create new Heroku app, using 'heroku apps:create appname' command.
4. Push project to Heroku, using 'push -u heroku master' command.
5. Create scale, using 'heroku ps:scale web=1' command.
6. Login to Heroku and select newly created app.
7. Select settings. Select ‘Reveal Config'. Add IP 0.0.0.0 and PORT 5000.
8. From 'More' menu on the top right, select 'Restart all dynos'.
9. View app: In settings, select Domain URL, NOT Git URL to view your hosted application.
10. Deployed via Heroku:..............

Please visit DEMO at.........

## Credits

# Content

* The recipes came from the [BBC FOOD](https://www.bbc.co.uk/food/diets/healthy) website.

# Media

* The photos used in this site were obtained from the [BBC FOOD](https://www.bbc.co.uk/food/diets/healthy) website.

# Acknowledgements

* I received inspiration for this project from [BBC FOOD](https://www.bbc.co.uk/food/diets/healthy) website with the combination of [Nutritionist Resource](https://www.nutritionist-resource.org.uk/) website.














































