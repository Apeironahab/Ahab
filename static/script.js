document.getElementById('buy-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const buyer = document.getElementById('buyer').value;
    const amount = document.getElementById('amount').value;

    fetch('/buy', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            buyer: buyer,
            amount: amount,
            payment_details: {} // Aquí irían los detalles del pago
        })
    })
    .then(response => response.json())
    .then(data => {
        const messageDiv = document.getElementById('message');
        if (data.status === 'success') {
            messageDiv.textContent = data.message;
            messageDiv.style.color = 'green';
        } else {
            messageDiv.textContent = data.message;
            messageDiv.style.color = 'red';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

