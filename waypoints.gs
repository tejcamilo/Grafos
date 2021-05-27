
function mapa(){// Get the directions.
// Creates a DirectionFinder with wapoint optimization enabled.
var directions = Maps.newDirectionFinder()
    .setOrigin('BOGOTÁ, Cundinamarca')
    .addWaypoint('COTA, Cundinamarca')
    .addWaypoint('CHÍA, Cundinamarca')
    .addWaypoint('CAJICÁ, Cundinamarca')
    .addWaypoint('SOPÓ, Cundinamarca')
    .addWaypoint('TOCANCIPÁ, Cundinamarca')
    .addWaypoint('GACHANCIPÁ, Cundinamarca')
    .addWaypoint('SESQUILÉ, Cundinamarca')
    .addWaypoint('SUESCA, Cundinamarca')
    .addWaypoint('CHOCONTÁ, Cundinamarca')
    .setDestination('VILLAPINZÓN, Cundinamarca')
    .setMode(Maps.DirectionFinder.Mode.DRIVING)
    .getDirections();
var route = directions.routes[0];


// Set up marker styles.
var markerSize = Maps.StaticMap.MarkerSize.MID;
var markerColor = Maps.StaticMap.Color.GREEN
var markerLetterCode = 'A'.charCodeAt();

// Add markers to the map.
var map = Maps.newStaticMap();
for (var i = 0; i < route.legs.length; i++) {
  var leg = route.legs[i];
  if (i == 0) {
    // Add a marker for the start location of the first leg only.
    map.setMarkerStyle(markerSize, markerColor, String.fromCharCode(markerLetterCode));
    map.addMarker(leg.start_location.lat, leg.start_location.lng);
    markerLetterCode++;
  }
  map.setMarkerStyle(markerSize, markerColor, String.fromCharCode(markerLetterCode));
  map.addMarker(leg.end_location.lat, leg.end_location.lng);
  markerLetterCode++;
}

// Add a path for the entire route.
map.addPath(route.overview_polyline.points);

// Send the map in an email.
var toAddress = Session.getActiveUser().getEmail();
MailApp.sendEmail(
  toAddress,
  'Directions',
  'Please open: ' + map.getMapUrl() + '&key=YOURAPIKEYHERE', {
    htmlBody: 'See below.<br/><img src="cid:mapImage">',
    inlineImages: {
      mapImage: Utilities.newBlob(map.getMapImage(), 'image/png')
    }
  }
);
}
