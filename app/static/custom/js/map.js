var path_to_markers = "app/static/assets/markers/"

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
        var businessCircle = new google.maps.Marker({
            map: map,
            clickable: true,
            position: {lat: Number(data[i][2]), lng: Number(data[i][3])},
            title: data[i][1] + "\nReview Count: " + data[i][5] + "\nAvg Stars: " + data[i][4],
            //icon: get_marker(Number(data[i][4])),     //gives 404 error
        });

        //weird syntax is wrapping the function so to preserve the index namespace
        businessCircle.addListener('click', (function(i) { return function() {
            console.log(mapData[i][0]);
            createWordCloudChart(mapData[i][0]);
            console.log(map.getBounds());
            //THIS IS WHERE THE ONCLICK EVENT HAPPENS WHEN A USER CLICKS ON A CIRCLE
            console.log(get_marker(Number(data[i][4])))
            //examples pan
            panMap(Number(data[i][2]), Number(data[i][3]));

        };})(i));
    }
}


function panMap(lat, lng) {
    map.panTo(new google.maps.LatLng(lat,lng));
}

//sorry this logic is so ugly - couldn't think how to do it cleaner
function get_marker(avgStars) {
    if (avgStars < 1.5) {
        return path_to_markers + "google-map-marker-1.png";
    } else if (avgStars < 2) {
        return path_to_markers + "google-map-marker-15.png";
    } else if (avgStars < 2.5) {
        return path_to_markers + "google-map-marker-2.png";
    } else if (avgStars < 3) {
        return path_to_markers + "google-map-marker-25.png";
    } else if (avgStars < 3.5) {
        return path_to_markers + "google-map-marker-3.png";
    } else if (avgStars < 4) {
        return path_to_markers + "google-map-marker-35.png";
    } else if (avgStars < 4.5) {
        return path_to_markers + "google-map-marker-4.png";
    } else if (avgStars < 5) {
        return path_to_markers + "google-map-marker-45.png";
    } else {
        return path_to_markers + "google-map-marker-5.png";
    }
}