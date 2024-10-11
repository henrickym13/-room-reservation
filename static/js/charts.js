var ctx = document.getElementById('reservasPorSalaChart').getContext('2d');
var reservasPorSalaChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: labels_data,  // Variáveis passadas no template
        datasets: [{
            label: 'Número de Reservas',
            data: reservations_data,
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
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
