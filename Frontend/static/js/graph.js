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
        data: goldEarnedDataArray[x]
    });
}

function renderTotalDamageChart() {
    let string = "totalDamageGraph-" + x;
    document.getElementById("newTotalDamageGraph").id = string;

    const ctx = document.getElementById(string).getContext('2d');
    new Chart(ctx, {
        maintainAspectRatio: false,
        type: 'bar',
        data: goldEarnedDataArray[x]
    });
}

function renderVisionScoreGraph() {
    let string = "visionScoreGraph-" + x;
    document.getElementById("newVisionScoreGraph").id = string;

    const ctx = document.getElementById(string).getContext('2d');
    new Chart(ctx, {
        maintainAspectRatio: false,
        type: 'bar',
        data: totalWardsPlacedDataArray[x]
    });
}

function renderTotalDamageTakenGraph() {
    let string = "totalDamageTakenGraph-" + x;
    document.getElementById("newTotalDamageTakenGraph").id = string;

    const ctx = document.getElementById(string).getContext('2d');
    new Chart(ctx, {
        maintainAspectRatio: false,
        type: 'bar',
        data: totalDamageTakenDataArray[x]
    });
}

function renderTotalCreepScoreGraph() {
    let string = "totalCreepScoreGraph-" + x;
    document.getElementById("newTotalCreepScoreGraph").id = string;

    const ctx = document.getElementById(string).getContext('2d');
    new Chart(ctx, {
        maintainAspectRatio: false,
        type: 'bar',
        data: totalCreepScoreDataArray[x]
    });
}