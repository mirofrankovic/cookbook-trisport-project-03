//queue()
//    .defer(d3.json, "/find_recipes")
//    .await(makeGraphs);
    
function makeGraphs(recipeData){
    var ndx = crossfilter(recipeData.slice(1));
    console.log(recipeData);
    show_meal_type_graph(ndx);
    
    show_sport_type_graph(ndx);
    show_race_day_graph(ndx);
    show_vegan_meal_graph(ndx);
    
    dc.renderAll();
}   

function show_meal_type_graph(ndx){
    var mealtypeDim = ndx.dimension(dc.pluck("meal_type_name"));
    var mealtypeMix = mealtypeDim.group();
    
    
    dc.barChart("#meal_type-graph")
        .width(768)
        .height(480)
        .x(d3.scaleBand())
        .xUnits(dc.units.ordinal)
        .brushOn(false)
        .xAxisLabel("")
        .yAxisLabel("")
        .dimension(mealtypeDim)
        .barPadding(0.1)
        .outerPadding(0.05)
        .useViewBoxResizing(true)
        .group(mealtypeMix);
}

function show_sport_type_graph(ndx){
    var sporttypeDim = ndx.dimension(dc.pluck("sport_type_name"));
    var sporttypeMix = sporttypeDim.group();
    
    dc.barChart("#sport_type-graph")
        .width(768)
        .height(480)
        .x(d3.scaleBand())
        .xUnits(dc.units.ordinal)
        .brushOn(false)
        .xAxisLabel("")
        .yAxisLabel("")
        .dimension(sporttypeDim)
        .barPadding(0.1)
        .outerPadding(0.05)
        .useViewBoxResizing(true)
        .group(sporttypeMix);
}

function show_race_day_graph(ndx){
    var racedayDim = ndx.dimension(dc.pluck("race_day_name"));
    var racedayMix = racedayDim.group();
    
    dc.barChart("#race_day-graph")
        .width(768)
        .height(480)
        .x(d3.scaleBand())
        .xUnits(dc.units.ordinal)
        .brushOn(false)
        .xAxisLabel("")
        .yAxisLabel("")
        .dimension(racedayDim)
        .barPadding(0.1)
        .outerPadding(0.05)
        .useViewBoxResizing(true)
        .group(racedayMix);
}

function show_vegan_meal_graph(ndx){
    var veganmealDim = ndx.dimension(dc.pluck("vegan_type_meal"));
    var veganmealMix = veganmealDim.group();
    
    dc.barChart("#vegan_meal-graph")
        .width(768)
        .height(480)
        .x(d3.scaleBand())
        .xUnits(dc.units.ordinal)
        .brushOn(false)
        .xAxisLabel("")
        .yAxisLabel("")
        .dimension(veganmealDim)
        .barPadding(0.1)
        .outerPadding(0.05)
        .useViewBoxResizing(true)
        .group(veganmealMix);
}

/*_____________sidenav____________-*/

$(document).ready(function(){
              $('.collapsible').collapsible();
              $('select').formSelect();
           });

           (function($){        
             $(function(){
            $('.sidenav').sidenav();
            }); // end of document ready
            })(jQuery); // end of jQuery name space

 /*_________________recipe count________________*/
 
$(document).ready(function() {
    
    var username = '{{author_name}}';
    
    var recipesText = $('#hidden-recipes').text();
    var recipesJson = JSON.parse(recipesText);         
    //var recipesJson = recipesText;
    var recipesList = [];
    
    for (i in recipesJson) {
                    recipesList.push(recipesJson[i]);
    }
    
    makeDashboard(recipesList);
    
    function makeDashboard(recipesList) {
        
        
        myRecipesList = [];
        
        for ( var i = 0; i < recipesList.length; i++ ) {
            let authorName = recipesList[i]['author_name'];
                        
            if ( username == authorName ) {
                            myRecipesList.push(recipesList[i]);
            }
        }
        
        var ndx = crossfilter(myRecipesList);
        //console.log(myRecipesList);
        
        counteMyRecipes(ndx, '#count-recipes-text');
        counteMyRecipes(ndx, '#count-recipes-box');
        resetButton(ndx);
        
        dc.renderAll();
    }
    
        function resetButton(ndx) {
            $("#reset-button").on("click", function() {
                dc.filterAll();
                dc.redrawAll();
            });
        }
              
        function counteMyRecipes(ndx, element) {
                    
            var myRecipesTotal = ndx.groupAll();
                    
            dc.numberDisplay(element)
                .formatNumber(d3.format("d"))
                .valueAccessor(function (d) {
                    d = myRecipesList.length
                    return (+d);
                })
                .group(myRecipesTotal);
        }
               
        MyRecipeCount = myRecipesList.length
                
                if ( MyRecipeCount != 0 ) {
                    $('#username-with-zero-recipes').css('display', 'none');
               } else {
                   $('#username-with-recipes').css('display', 'none');
                   // $('.dashboard-graphs').css('display', 'none');
                }
                    
});

/*__________________my_recipes_____________________*/

$(document).ready(function(){
        $('.modal').modal();
    });  

/*_________________my_profile_thumbsUp_______________*/

document.getElementById("thumb-up-btn").onclick = function() {
    document.getElementById("form").submit();
}

/*_______________________________getready_________________*/
/*

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
} */