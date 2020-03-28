# **Miro does Snack - Cookbook for triathlon athleetes today - Code Institute - Milestone project 03**

The brief was to create a web application that allows users to store and easily access cooking recipes.
The recipes are to be stored in a database which can be filtered by a user on the website using the categories.
It is a data-driven application, and the target audience is any user targeted towards athletes working out for their competition.

This application will access into designing a database schema based on recipes, and any other related properties and entities 
(e.g. views, upvotes, ingredients, recipe authors, allergens, cuisine etc…).

In addition we create the backend code to retrieve a list of recipes, filtered based on various criteria (e.g. allergens, cuisine, etc…)
and order them based on some reasonable aspect (e.g. number of views). Create a frontend page to display these,
and to show some summary statistics around the list (e.g. number of new recipes). Optionally, add support for pagination, when the number of results is large.
Create a detailed view for each recipes, that would just show all attributes for that recipe, and the full preparation instructions.
Allow for editing and deleting of the recipe records, either on separate pages, or built into the list/detail pages.

# **UX**

This application is for use by all users especially for athleetes who are busy with study, work, school,
extra curricular activities, coming up with quick meals before and after workout.
I designed the site so that users can share recipes and rate them accordingly.

User stories:

> As an athlete, prepering for the next season, I would like to know what to eat to keep myself fit during the winter preparation.
> As an athlete, preparing for the race, I would like to learn what to eat a couple days before my race day.
> As an athlete, competing during the race day, I would like to know how to keep myself full loaded with my nutritions.
> As an athlete, finishing my race, I would like to know what to eat afther my race for my recovery.


# Layout

The layout used the *[Materialize CSS Parallax template](https://materializecss.com/templates/parallax-template/preview.html)* which I modified to suit my own requirements.

# Features 

In this section I will describe the front-end features of my project:

1. **Navbar**:consists of the PREPARE FOR YOUR RACE logo which also returns the user to the "Home" page of the application.
             My navbar also has links to "All Recipes", "Your Suggestion", "Contact Us", "Dashboard", "Login". The navbar will appear in all pages
             with the same functions for all links.
         
2. **Home**:consists of one background image along with some information on contacting the webmaster and a link to the contact us page of the site. 
    
3. **All Recipes**:directs the user to the "All Recipes" page which displays ALL recipes from ALL users which have been entered on the site. 
                The user can then filter or browse through the recipes.
                The can view more information on each recipe by selectign the "See Recipe Description" link which delivers the user to the "Recipe Detail" page. 

4. **Recipe Detail**:provides users with the recipe details containg a recipe name, description, image (if available), flavour, meal type, race day, sport type, nutrition wise type of meal, author and date posted.

5. **My Recipes**:provides the user with the recipes that they have added themselves. The user's recipes can be edited and deleted by using the buttons displayed under the recipes.

6. **Login**:when first selected the user will be prompted to create a username to login to the application so that they can add recipes to the database.

7. **Dashboard**:once logged in the user will be presented with their dashboard which provides a count of their recipes, along with 4 data charts depicting the number of favourite meal type, favourite sport type, favourite race day and meal associated for the vegan.

8. **Contact Us**:delivers the user to the contact page. This page displays a blank form, which allows users to contact the website developers to offer feedback and suggestions (not currently wired up to an email address as this is not a real business). 
              Their are also 4 social media buttons so that the user may interact on social networks.

9. **Social Links*:provides users with links to the website social media pages.


# **Technologies Used**

* *[Cloud 9 IDE](https://aws.amazon.com/cloud9/)*
> This project used Cloud 9, an online integrated development environment, to construct the code end to end.











