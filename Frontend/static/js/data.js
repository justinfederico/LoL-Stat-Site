const labels = ["summoner1", "summoner2", "summoner3", "summoner4", "summoner5", "summoner6", "summoner7", "summoner8", "summoner9", "summoner10"];
const champKillData0 = {
    labels: labels,
    datasets: [{
        label: '1st Match',
        data: [65, 59, 80, 81, 56, 55, 40, 43, 76, 10],
        backgroundColor: [
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)'
        ],
        borderColor: [
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)'
        ],
        borderWidth: 1
    }]
};

const champKillData1 = {
    labels: labels,
    datasets: [{
        label: '2nd Match',
        data: [30, 54, 83, 41, 55, 76, 45, 67, 12, 32],
        backgroundColor: [
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)'
            ],
        borderColor: [
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)'
        ],
        borderWidth: 1
    }]
};

const champKillData2 = {
    labels: labels,
    datasets: [{
        label: '3rd Match',
        data: [1, 87, 32, 32, 56, 46, 91, 67, 12, 32],
        backgroundColor: [
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)'
            ],
        borderColor: [
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)'
        ],
        borderWidth: 1
    }]
};

const champKillData3 = {
    labels: labels,
    datasets: [{
        label: '4th Match',
        data: [4, 65, 75, 21, 32, 87, 21, 43, 12, 41],
        backgroundColor: [
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)'
            ],
        borderColor: [
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)'
        ],
        borderWidth: 1
    }]
};

const champKillData4 = {
    labels: labels,
    datasets: [{
        label: '5th Match',
        data: [41, 75, 21, 43, 54, 12, 12, 43, 12],
        backgroundColor: [
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(242, 0, 0, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)',
            'rgba(0, 141, 242, 0.4)'
            ],
        borderColor: [
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)',
            'rgba(0, 0, 0, 0.8)'
        ],
        borderWidth: 1
    }]
};

const champKillDataArray = [champKillData0, champKillData1, champKillData2, champKillData3, champKillData4];