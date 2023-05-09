function formatChart(contexto, datos, etiquetas){
    const myChart = new Chart(contexto, {
        type: 'doughnut',
        data: {
            labels: etiquetas,
            datasets: [{
                label: 'Gastos',
                data: datos,
                /*
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
                */
            }]
        }
    })
}