var path_to_markers = '/static/assets/markers/'
var markerWindow
var map

function initMap () {
  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 33.424564, lng: -111.93 },
    zoom: 16
  })
}

//  Fetching data
fetch('/mappath/testing')
  .then(res => {
    return res.json()
  })
  .then(data => {
    fillMap(data)
  })
  .catch(error => {
    console.log(error)
  })

var mapData
var allMarkers = []

function fillMap (data) {
  mapData = data
  for (var i = 0; i < data.length; i++) {
    var businessCircle = new google.maps.Marker({
      map: map,
      clickable: true,
      business_id: data[i][0],
      address: data[i][6],
      name: data[i][1],
      position: { lat: Number(data[i][2]), lng: Number(data[i][3]) },
      title:
        data[i][1] +
        '\nReview Count: ' +
        data[i][5] +
        '\nAvg Stars: ' +
        data[i][4],
      icon: get_marker(Number(data[i][4])) //gives 404 error
    })

    //weird syntax is wrapping the function so to preserve the index namespace
    businessCircle.addListener(
      'click',
      (function (i) {
        return function () {
          var business_id = mapData[i][0]
          panMap(Number(data[i][2]), Number(data[i][3]), business_id)
        }
      })(i)
    )

    //add to marker list
    allMarkers.push(businessCircle)
  }
}

function panMap (lat, lng, business_id) {
  // Pan map
  map.panTo(new google.maps.LatLng(lat, lng))

  //open info window
  var marker = allMarkers.filter(
    marker => marker.business_id === business_id
  )[0]
  console.log(marker)
  if (markerWindow) {
    markerWindow.close()
  }
  markerWindow = new google.maps.InfoWindow({
    content: `<b>${marker.name}</b><br>${marker.address}`
  })
  markerWindow.open(map, marker)

  //generate charts
  createWordCloudChart(business_id)
  createSentimentGraph(business_id)
  createHeatMap(business_id)
}

//sorry this logic is so ugly - couldn't think how to do it cleaner
function get_marker (avgStars) {
  if (avgStars < 1.5) {
    return path_to_markers + 'google-map-marker-1small.png'
  } else if (avgStars < 2) {
    return path_to_markers + 'google-map-marker-15small.png'
  } else if (avgStars < 2.5) {
    return path_to_markers + 'google-map-marker-2small.png'
  } else if (avgStars < 3) {
    return path_to_markers + 'google-map-marker-25small.png'
  } else if (avgStars < 3.5) {
    return path_to_markers + 'google-map-marker-3small.png'
  } else if (avgStars < 4) {
    return path_to_markers + 'google-map-marker-35small.png'
  } else if (avgStars < 4.5) {
    return path_to_markers + 'google-map-marker-4small.png'
  } else if (avgStars < 5) {
    return path_to_markers + 'google-map-marker-45small.png'
  } else {
    return path_to_markers + 'google-map-marker-5small.png'
  }
}
