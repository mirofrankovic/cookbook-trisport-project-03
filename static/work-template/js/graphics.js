$(document).ready(function() {
    var username = '{{username}}';
    
    var recipesText = $('#hidden-recipes').text();
    var recipesJson = JSON.parse(recipesText);
    var recipesList = [];
    
    
    for (i in recipesJson){
        recipesList.push(recipesJson[i]);
    }
    
    myDashboard(recipesList);
    
    
    function myDashboard(recipesList){
        
        
        // recipes by current user
        myRecipesList =[];
        
         for ( var i = 0; i < recipesList.length; i++ ) {
             let authorName = recipesList[i]['author_name'];
             
             if ( username == authorName ) {
                 myRecipesList.push(recipesList[i]);
             }
         }
         
         var ndx = crossfilter(myRecipesList);
         console.log(myRecipeList);
    }
    
    
});