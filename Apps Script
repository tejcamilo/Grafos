function myFunction() {
  var getSpreadSheet = SpreadsheetApp.openById("1r-ZqwVnkWToFeNFo8FF0Vtwcff6PbkTiixJWZrLEU0k");
  var sheet = getSpreadSheet.getSheetByName('Sheet3');
  var lastRow = sheet.getLastRow();
  var row = sheet.getRange(1,1,lastRow);
  var values = row.getValues();
  Logger.log(values);
  for (var counter = 0; counter <= lastRow; counter = counter + 1) {
    //Logger.log(values[counter][0]);
    var directions = Maps.newDirectionFinder()
      .setOrigin('Bogota, Colombia')
      .setDestination(values[counter][0]+',Colombia')
      .setMode(Maps.DirectionFinder.Mode.DRIVING)
      .getDirections();
    Logger.log(values[counter][0]+' '+directions.routes[0].legs[0].duration.text);
  }

// Logs how long it would take to walk from Times Square to Central Park.
var directions = Maps.newDirectionFinder()
    .setOrigin('Bogota, Colombia')
    .setDestination('AGUA DE DIOS, Colombia')
    .setMode(Maps.DirectionFinder.Mode.DRIVING)
    .getDirections();
Logger.log(directions.routes[0].legs[0].duration.text);
}
