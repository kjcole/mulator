// Written by Kevin Cole <kevin.cole@novawebcoop.org> 2016.12.15
//
// This "generates RAM" for the 'puter.
//

var table = document.getElementById("data");
var tr = 0;
var th = 0;
var td = 0;
var addr = 0;
var field = 0;

for (row = 0; row < 9; row++) {
  var tr = table.insertRow(-1);  // Append row (insert at bottom)
  th = document.createElement('th');
  th.className = "address";
  addr = row.toString(2)+"xxx";  // Convert to binary with masked bits
  while (addr.length < 8) addr = "0" + addr;  // Add leading zeros
  th.innerHTML = addr;
  tr.appendChild(th);
  for (cell = 0; cell < 8; cell++) {
    td = tr.insertCell(cell + 1);
    field = document.createElement("input");
    addr = row.toString(2) + cell.toString(2);  // Full address
    while (addr.length < 8) addr = "0" + addr;  // Add leading zeros
    field.id = "0b" + addr;           // Unique ID based on full address
    field.size = 8;                   // Holds eight characters
    field.className = "bits data";    // Holds binary data only
    field.pattern = "[01]{8}";        // Validation: 8 binary digits
    field.placeholder = "00000000";   // Visual indicator
    field.addEventListener("blur", blurFill);
//  field.defaultValue = "00000000";  // Default value
    td.appendChild(field);
  }
}

function blurFill() {
  alert("It's a start...");
}
