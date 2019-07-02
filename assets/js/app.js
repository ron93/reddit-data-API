//declaration sql query for sqlite
var createStatement = "CREATE TABLE IF NOT EXISTS Shops (
    id INTERGER PRIMARY KEY AUTOINCREMENT, shop_name TEXT,
    description TEXT)";
var selectStatement = "SELECT * FROM Shops ";
var insertStatement = "INSERT INTO Shops (shop_name,description) value(?,?)";
var updateStatement = "UPDATE Shops SET shop_name = ?, description = ? WHERE id=?";
 
var deleteStatement = "DELETE FROM Shops WHERE id=?";
 
var dropStatement = "DROP TABLE Shops";
 
 var db = openDatabase("Mbugus'",  "Chapati,Nya,achoma,kuku");  // Open SQLite Database
 
var dataset;
 
var DataType;

//function initialize database when page ready
function initDatabase(){
    try {
        //check if sqlite supported by browser
        if(!window.openDatabase){
            alert('Database not supported')
        }
        else {
            createTable();
        }
    }
    catch(e){
        
     
        if (e == 2) {
 
            // Version number mismatch. 
 
            console.log("Invalid database version.");
 
        } else {
 
            console.log("Unknown error " + e + ".");
 
        }
 
        return;
 
    }
    
}

//function to create tables
function createTable()
{
    db.transaction(function(tx){tx.executeSql(createStatement,[],showRecord,onError);});
}
//function to insert shop to db
function insertRecord(){
    var shoptmp= $('input:text[id=shop_name]').val();
    var description = $('input:text[id=description]').val();
    db.transaction(function (tx) { tx.executeSql(insertStatement, [shoptmp, description], loadAndReset, onError); });
 
        //tx.executeSql(SQL Query Statement,[ Parameters ] , Sucess Result Handler Function, Error Result Handler Function );
 

}