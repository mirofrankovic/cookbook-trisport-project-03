//queue()
//    .defer(d3.json, "/find_recipes")
//    .await(makeGraphs);
    
function makeGraphs(recipeData){
    var ndx = crossfilter(recipeData.slice(1));
    console.log(recipeData);
    show_meal_type_graph(ndx);
    
    // show_sport_type_graph(ndx);
    // show_race_day_graph(ndx);
    // show_vegan_meal_graph(ndx);
    
    dc.renderAll();
}   

function show_meal_type_graph(ndx){
    var mealtypeDim = ndx.dimension(dc.pluck("meal_type_name"));
    var mealtypeMix = mealtypeDim.group();
    // var commitmentSumGroup = programmeDimension.group().reduceSum();
    
    // dc.barChart("meal_type-graph")
    //     .width(350)
    //     .height(250)
    //     .margins({top: 20, right: 20, bottom: 30, left: 10})
    //     .dimension(mealtypeDim)
    //     .group(mealtypeMix)
    //     .transitionDuration(500)
    //     .x(d3.scale.ordinal())
    //     // .x(d3.scaleBand())
    //     .xUnits(dc.units.ordinal)
    //     .elasticY(true)
    //     .xAxisLabel("Meal-Type")
    //     .yAxis().tickFormat(d3.format("d"));
        
        
    // var ndx = crossfilter(data);
    // var programmeDimension = ndx.dimension((d) => d[PROGRAMME_NAME_KEY]);
    // var commitmentSumGroup = programmeDimension.group().reduceSum((d) => d[TOTAL_COMMITMENT_KEY]);
    
    dc.barChart("#meal_type-graph")
        .width(768)
        .height(480)
        .x(d3.scaleBand())
        .xUnits(dc.units.ordinal)
        .brushOn(false)
        .xAxisLabel("use label here")
        .yAxisLabel("Total Commitmemt")
        .dimension(mealtypeDim)
        .barPadding(0.1)
        .outerPadding(0.05)
        .group(mealtypeMix);
}
