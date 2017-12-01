var temps;

window.onload = function() {
  getTemps();
  setInterval(function() {
    getTemps();
  }, 30000); // 30 segunduro datu berria dago
}

function getTemps() {
  $.ajax({
      success: function(data){
        if (data.success){
          temps = data.temps;
          showCurrent();
          createGraph();
        }else{
          alert(data.error);
        }
      },
      error: function(data){
        if(data.responseJSON){
        	alert(data.responseJSON.error);
        }else{
        	alert(data.statusText);
        }
      },
      processData: false,
      type: 'GET',
      url: '/ajax/get_temps'
    });
}

function showCurrent(){
  $("#currTemp").html(temps[temps.length-1].tenp);
}

function createGraph() {
  var chartData = temps;
  var chart = AmCharts.makeChart("chartdiv", {
      "type": "serial",
      "theme": "light",
      "marginRight": 80,
      "autoMarginOffset": 20,
      "marginTop": 7,
      "dataProvider": chartData,
      "valueAxes": [{
          "axisAlpha": 0.2,
          "dashLength": 1,
          "position": "left"
      }],
      "mouseWheelZoomEnabled": true,
      "graphs": [{
          "id": "g1",
          "balloonText": "[[value]]",
          "bullet": "round",
          "bulletBorderAlpha": 1,
          "bulletColor": "#FFFFFF",
          "hideBulletsCount": 50,
          "title": "red line",
          "valueField": "tenp",
          "useLineColorForBulletBorder": true,
          "balloon":{
              "drop":true
          }
      }],
      "chartScrollbar": {
          "autoGridCount": true,
          "graph": "g1",
          "scrollbarHeight": 20
      },
      "chartCursor": {
         "limitToGraph":"g1"
      },
      "categoryField": "data",
      "categoryAxis": {
          "parseDates": true,
          "axisColor": "#DADADA",
          "dashLength": 1,
          "minorGridEnabled": true
      },
  });

  chart.addListener("rendered", zoomChart);
  zoomChart();
}

function zoomChart() {
    // different zoom methods can be used - zoomToIndexes, zoomToDates, zoomToCategoryValues
    chart.zoomToIndexes(chartData.length - 40, chartData.length - 1);
}
