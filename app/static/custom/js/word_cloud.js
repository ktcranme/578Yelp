// Creating empty chart
var chart = Highcharts.chart('word-cloud-panel', {
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

chart.hideNoData();
chart.showLoading();

//  Fetching data
fetch('/wordCloud/testing')
  .then(res => {
    chart.hideLoading();
    return res.json();
  })
  .then(data => {
    genWordCloud(data);
  })
  .catch(() => {
    chart.showNoData("Error loading cloud");
  });


genWordCloud = (data) => {
  chart.series[0].setData(data);
  chart.redraw();
}