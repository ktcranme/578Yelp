
function createChart(series) {

  var chart = Highcharts.chart('sentiment-panel', {

    title: {
      text: 'Average sentiment scores for the restaurant over the years, 2010 to 2020'
    },

    subtitle: {
      text: 'Source: yelp review dataset'
    },

    yAxis: {
      title: {
        text: 'Average sentiment score'
      }
    },

    xAxis: {
      accessibility: {
        rangeDescription: 'Year : 2010 to 2020'
      }
    },

    legend: {
      layout: 'vertical',
      align: 'right',
      verticalAlign: 'middle'
    },

    plotOptions: {
      series: {
        label: {
          connectorAllowed: false
        },
        pointStart: 2010
      }
    },

    series: this.series,

    responsive: {
      rules: [{
        condition: {
          maxWidth: 500
        },
        chartOptions: {
          legend: {
            layout: 'horizontal',
            align: 'center',
            verticalAlign: 'bottom'
          }
        }
      }]
    },
  });

}

const createSentimentGraph = (business_id) => {
fetch('/sentimentAnalysis/testing?business_id=' + business_id)
  .then(res => {
    console.log("Reached createSentimentGraph...");
    console.log("Business id  : " + business_id);
    return res.json();
  }).then(data => {
    genSentimentGraph(data);
  }).catch(() => {
    chart.showNoData("Error loading cloud");
  });
}

genSentimentGraph = (jsondata) => {
  console.log("Reached generate sentiment graph");
  console.log(jsondata);
  series = [];
  //creating the series to be used.
  for (i = 0; i < jsondata.length; i++) {
    var obj = { 'name': jsondata[i].name, 'data': jsondata[i].data };
    series.push(obj);
  }
  createChart(series);
  console.log("chart redraw done...");
}

document.addEventListener("DOMContentLoaded", function(){
  const businessId = 'XKOAi4J47i-YEhhHfKkPRQ';
  createSentimentGraph(businessId);
});