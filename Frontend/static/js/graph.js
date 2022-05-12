/* CHAMP KILL CHART RENDER */
function renderChampKillChart() {
    let string1 = "champKillGraph-" + x;
    document.getElementById("newKillGraph").id = string1;

    const ctx = document.getElementById(string1).getContext('2d');
    const myChart = new Chart(ctx, {
        maintainAspectRatio: false,
        type: 'bar',
        data: champKillDataArray[x]
    });
}

/* GOLD EARNED CHART RENDER */
function renderGoldEarnedChart() {
    let string = "goldEarnedGraph-" + x;
    document.getElementById("newGoldEarnedGraph").id = string;

    const ctx = document.getElementById(string).getContext('2d');
    new Chart(ctx, {
        maintainAspectRatio: false,
        type: 'bar',
        data: {
            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            datasets: [{
                label: '# of Votes',
                data: [12, 19, 3, 5, 2, 3],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    x++;
}

