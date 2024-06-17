document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();

    var ticker = document.querySelector('input[name="ticker"]').value;
    var start_date = document.querySelector('input[name="start_date"]').value;
    var end_date = document.querySelector('input[name="end_date"]').value;
    var interval = document.querySelector('select[name="interval"]').value;

    fetch(`http://localhost:8000/stocks/?ticker=${ticker}&start_date=${start_date}&end_date=${end_date}&interval=${interval}`)
        .then(response => response.json())
        .then(data => {
            var table = document.querySelector('table');
            table.innerHTML = '';

            for (var date in data) {
                var row = document.createElement('tr');

                var dateCell = document.createElement('td');
                dateCell.textContent = date;
                row.appendChild(dateCell);

                for (var key in data[date]) {
                    var cell = document.createElement('td');
                    cell.textContent = data[date][key];
                    row.appendChild(cell);
                }

                table.appendChild(row);
            }
        });
});