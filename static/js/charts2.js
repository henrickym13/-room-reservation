var ctx = document.getElementById('reservasPorSalaChart').getContext('2d');
var reservasPorSalaChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: labels_data,  // Variáveis passadas no template
        datasets: [{
            label: 'Salas Mais Utilizadas',
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

var ctx = document.getElementById('reservasPorMesChart').getContext('2d');
var reservasPorMesChart = new Chart(ctx, {
    type: 'line',  // Você pode escolher 'bar' ou 'line'
    data: {
        labels: lbl_data,
        datasets: [{
            label: 'Reservas',
            data: reserve_data,
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

var ctx = document.getElementById('horarioPicoChart').getContext('2d');
var horarioPicoChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: lb_data,
        datasets: [{
            label: 'Reservas',
            data: peak_data,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
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