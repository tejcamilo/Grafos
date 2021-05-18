function myFunction() {
  var getSpreadSheet = SpreadsheetApp.openById("1r-ZqwVnkWToFeNFo8FF0Vtwcff6PbkTiixJWZrLEU0k");
  var sheet1 = getSpreadSheet.getSheetByName('Sheet3');
  var sheet2 = getSpreadSheet.getSheetByName('Sheet4');
  var lastRow = sheet1.getLastRow();
  var row = sheet1.getRange(1,1,lastRow);
  var values = row.getValues();
  Logger.log(values[77][0])
  for (var i = 1; i <= lastRow; i = i+1) {
    for (var j = 1; j <= lastRow; j = j+1 ){
      var directions = Maps.newDirectionFinder()
        .setOrigin(values[i][0]+',Colombia')
        .setDestination(values[j][0]+',Colombia')
        .setMode(Maps.DirectionFinder.Mode.DRIVING)
        .getDirections();
      Logger.log(values[i][0]+' '+values[j][0]);
      //SpreadsheetApp.flush();
      sheet2.getRange(j+1, i+1).setValue(directions.routes[0].legs[0].duration.text);
      //SpreadsheetApp.flush();
    }
  }
}
