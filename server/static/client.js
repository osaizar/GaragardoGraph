var temps;
var chart;

window.onload = function() {
  getTemps(function() {
    showCurrent();
    createGraph();
  });

  setInterval(function() {
    getTemps(function() {
      showCurrent();
      chart.dataProvider = temps;
      chart.validateData();
    });
  }, 30000); // 30 segunduro datu berria dago
}

function getTemps(callback) {
  $.ajax({
      success: function(data){
        if (data.success){
          temps = data.temps;
          callback();
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
  chart = AmCharts.makeChart("chartdiv", {
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
    chart.zoomToIndexes(temps.length - 40, temps.length - 1);
}
