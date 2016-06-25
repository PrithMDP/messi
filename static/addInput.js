var counter = 1;
var limit = 5;
function addInput(divName){
     if (counter == limit)  {
          alert("You have reached the limit of adding " + counter + " inputs");
     }
     else {
          var newdiv = document.createElement('div');
          newdiv.innerHTML = "Column " + (counter + 1) +  "<br><select name='myInputs[]'> <option value = \"Int\"> Int </option><option value=\"Double\">Double</option><option value=\"String\">String</option><option value=\"Date\">Date</option><option value=\"Char\">Char</option> </select>"
          document.getElementById("dynamicInput").appendChild(newdiv);
          counter++;
     }
}




// <br> <select name = \"column_1\" id = \"column_1\">
//                 <option value=\"Int\">Int</option>
//                 <option value=\"Double\">Double</option>
//                 <option value=\"String\">String</option>
//                 <option value=\"Date\">Date</option>
//                 <option value=\"Char\">Char</option>
//             </select> name='myInputs[]'>"