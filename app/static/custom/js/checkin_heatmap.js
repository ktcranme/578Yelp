function getPointCategoryName(point, dimension) {
  var series = point.series,
    isY = dimension === 'y',
    axis = series[isY ? 'yAxis' : 'xAxis'];
  return axis.categories[point[isY ? 'y' : 'x']];
}

function createMap(name, heat_map) {
  console.log("Entered heat map panel..")
  var chart = Highcharts.chart('heat-map-panel', {

    chart: {
      type: 'heatmap',
      marginTop: 40,
      marginBottom: 80,
      plotBorderWidth: 1
    },


    title: {
      text: 'Checkins Heat Map : ' + name
    },

    xAxis: {
      categories: ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
    },

    yAxis: {
      categories: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
      title: null,
      reversed: true
    },

    accessibility: {
      point: {
        descriptionFormatter: function (point) {
          var ix = point.index + 1,
            xName = getPointCategoryName(point, 'x'),
            yName = getPointCategoryName(point, 'y'),
            val = point.value;
          return ix + '. ' + xName + ' sales ' + yName + ', ' + val + '.';
        }
      }
    },

    colorAxis: {
      min: 0,
      minColor: '#FFFFFF',
      maxColor: '#03a678'
    },

    legend: {
      align: 'right',
      layout: 'vertical',
      margin: 0,
      verticalAlign: 'top',
      y: 25,
      symbolHeight: 280
    },

    tooltip: {
      formatter: function () {
        return '<b> There were ' + this.point.value + ' checkins at ' + name + ' <br> in the month of '
          + getPointCategoryName(this.point, 'x') + ' in ' + getPointCategoryName(this.point, 'y') + '</b>';
      }
    },

    series: [{
      name: 'Checkin dates and times',
      borderWidth: 0,
      data: heat_map,
      dataLabels: {
        enabled: false,
        color: '#000000'
      }
    }],

    responsive: {
      rules: [{
        condition: {
          maxWidth: 500
        },
        chartOptions: {
          yAxis: {
            labels: {
              formatter: function () {
                return this.value.charAt(0);
              }
            }
          }
        }
      }]
    }

  });

}

const createHeatMap = (business_id) => {
  fetch('/checkinHeatMap/testing?business_id=' + business_id)
    .then(res => {
      console.log("Reached createHeatMap...");
      console.log("Business id  : " + business_id);
      return res.json();
    }).then(data => {
      genHeatMap(data);
    }).catch(() => {
      chart.showNoData("Error loading cloud");
    });
  }

genHeatMap = (data) => {
  restaurant = data['name']
  heat_map = data['heat_map']
  createMap(restaurant, heat_map);
}

document.addEventListener("DOMContentLoaded", function(){
  const businessId = 'XKOAi4J47i-YEhhHfKkPRQ';
  createHeatMap(businessId);
});