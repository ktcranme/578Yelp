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