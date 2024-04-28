// car_make_model_index.js

function sortTable(attribute) {
  var table, rows, switching, i, x, y, shouldSwitch;
  table = document.getElementById("car-table");
  switching = true;
  while (switching) {
      switching = false;
      rows = table.rows;
      for (i = 1; i < (rows.length - 1); i++) {
          shouldSwitch = false;
          x = rows[i].getElementsByTagName("td")[attribute].innerText;
          y = rows[i + 1].getElementsByTagName("td")[attribute].innerText;
          if (x.toLowerCase() > y.toLowerCase()) {
              shouldSwitch= true;
              break;
          }
      }
      if (shouldSwitch) {
          rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
          switching = true;
      }
  }
}
