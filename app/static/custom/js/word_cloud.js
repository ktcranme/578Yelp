var chart = Highcharts.chart('word-cloud-panel', {
  accessibility: {
    screenReaderSection: {
      beforeChartFormat: '<h5>{chartTitle}</h5>'
    }
  },
  series: [{
    type: 'wordcloud',
    data: [],
    name: 'Occurrences'
  }],
  title: {
    text: 'Review word cloud'
  },
  options: {
    chart: {
      height: window.innerHeight + 'px'
    }
  },
  credits: { enabled: false }
});
chart.showLoading();

fetch('/wordCloud/testing')
  .then(res => {
    return res.json();
  })
  .then(data => {
    chart.series[0].setData(data);
    chart.redraw();
    chart.hideLoading();
  });


genWordCloud = (data) => {
  chart.series.data = data;
}