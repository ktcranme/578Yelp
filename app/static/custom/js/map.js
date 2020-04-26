var map;
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 33.424564, lng: -111.93},
    zoom: 14
    });
}


//  Fetching data
fetch('/mappath/testing')
    .then(res => {
    return res.json();
    })
  .then(data => {
    fillMap(data);
  })
  .catch((error) => {
    console.log(error)
  });

var mapData;

function fillMap(data) {
    mapData = data;
    for(var i = 0; i < data.length; i++) {
        var businessCircle = new google.maps.Circle({
            strokeColor: '#FF0000',
            strokeOpacity: 0.8,
            strokeWeight: 0,
            fillColor: '#FF0000',
            fillOpacity: 0.35,
            map: map,
            clickable: true,
            center: {lat: Number(data[i][1]), lng: Number(data[i][2])},
            radius: data[i][4] * 20
        });

        //weird syntax is wrapping the function so to preserve the index namespace
        businessCircle.addListener('click', (function(i) { return function() {
            console.log(mapData[i][0]);

            //THIS IS WHERE THE ONCLICK EVENT HAPPENS WHEN A USER CLICKS ON A CIRCLE

        };})(i));
    }
}