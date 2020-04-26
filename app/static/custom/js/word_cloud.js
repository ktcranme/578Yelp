class wordCloudChart {
  constructor(business_id) {
    this.divId = null;
    this.chart = null;
    this.data = null;
    this.name = null;
    this.businessId = business_id
  }

  // binds an empty Word cloud to panel
  bindChart = () => {
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

  //fetch data for word cloud
  getWordCloud = () => {
    fetch('/wordCloud/testing?business_id=' + this.businessId)
      .then(res => {
        this.chart.hideLoading();
        return res.json();
      })
      .then(data => {
        this.data = data.data;
        this.name = data.name;
        this.redrawChart();
      })
      .catch(() => {
        this.chart.showNoData("Error loading cloud");
      });
  }

  //redraw data in chart
  redrawChart = () => {
    this.chart.series[0].setData(this.data);
    this.chart.setTitle({ text: 'Review word cloud : ' + this.name });
    this.chart.redraw();
  }

}

const createWordCloudChart = (businessId) => {
  let wcChart = new wordCloudChart(businessId);
  wcChart.bindChart();
  wcChart.getWordCloud();
  wcChart.redrawChart();
}

document.addEventListener("DOMContentLoaded", function () {
  const businessId = 'XKOAi4J47i-YEhhHfKkPRQ';
  createWordCloudChart(businessId);
});
