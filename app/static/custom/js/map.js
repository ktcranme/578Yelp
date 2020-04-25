var map;
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 33.397, lng: -112.0},
    zoom: 5
    });
}


//  Fetching data
fetch('/mappath/testing')
  .then(res => {
    chart.hideLoading();
    return res.json();
  })
  .then(data => {
    printOut(data);
  })
  .catch(() => {
    console.log("error loading map data")
  });


printOut = (data) => {
  console.log(data);
}