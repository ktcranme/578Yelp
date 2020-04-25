class wordCloudChart {
  constructor(business_id) {
    this.divId = null;
    this.chart = null;
    this.data = null;
    this.businessId = business_id
  }

  // function to create 
  createChart = () => {
    // Creating empty chart
    this.chart = Highcharts.chart('word-cloud-panel', {
      accessibility: {
        screenReaderSection: {
          beforeChartFormat: '<h5>{chartTitle}</h5>'
        }
      },
      series: [{
        type: 'wordcloud',
        data: [],
        name: 'Occurrences',
        minFontSize: 25,
        maxFontSize: 100
      }],
      title: {
        text: 'Review word cloud'
      },
      tooltip: {
        formatter: function () {
          return '<b>Name: </b>' + this.point.name + '<br>' +
            '<b>Occurences: </b>' + this.point.weight + '<br>' +
            '<b>Sentiment: </b>' + this.point.sentiment;
        }
      },
      credits: { enabled: false }
    });

    //show loading data
    this.chart.hideNoData();
    this.chart.showLoading();
  }

  //fetch data
  getWordCloud = () => {
    fetch('/wordCloud/testing?business_id=' + this.businessId)
      .then(res => {
        this.chart.hideLoading();
        return res.json();
      })
      .then(data => {
        this.data = data;
        this.redrawChart();
      })
      .catch(() => {
        this.chart.showNoData("Error loading cloud");
      });
  }

  redrawChart = () => {
    this.chart.series[0].setData(this.data);
    this.chart.redraw();
  }

}



document.addEventListener("DOMContentLoaded", function () {
  const businessId = 'XKOAi4J47i-YEhhHfKkPRQ';
  let wcChart = new wordCloudChart(businessId);
  wcChart.createChart();
  wcChart.getWordCloud();
  wcChart.redrawChart();
});
