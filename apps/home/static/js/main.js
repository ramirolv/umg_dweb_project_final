const ctx = document.getElementById('myChart');
const names = ['Carlos', 'Pedro', 'Maria', 'Rosa', 'Juan'];
const ages = [24, 10, 54, 51, 15];

const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: names,
        datasets: [{
            label: 'Gastos',
            data: ages,
            backgroundColor:[
                'rgba(255, 99, 132, 0.5)',
                'rgba(189, 147, 249, 0.5)',
                'rgba(80, 250, 123, 0.5)',
                'rgba(116, 202, 255, 0.5)',
                'rgba(127, 21, 108, 0.5)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)'
            ],
            borderWidth: 1.5
        }]
    }
})