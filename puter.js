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
    addr = row.toString(2)+"xxx";
    while (addr.length < 8) addr = "0" + addr;
	th.innerHTML = addr;
    tr.appendChild(th);
    for (cell = 1; cell < 9; cell++) {
	td = tr.insertCell(cell);
	field = document.createElement("input");
	field.size = 8;
	field.id="qwert" + cell;
	td.appendChild(field);
    }
}
