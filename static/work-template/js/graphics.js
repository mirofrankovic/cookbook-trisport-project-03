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
        .xAxisLabel("")
        .yAxisLabel("")
        .dimension(mealtypeDim)
        .barPadding(0.1)
        .outerPadding(0.05)
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
        .group(veganmealMix);
}












































