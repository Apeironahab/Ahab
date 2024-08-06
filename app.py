from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Ruta para servir la interfaz de usuario
@app.route('/')
def index():
    return render_template('index.html')

#parte nueva hasta port 5000
@app.route('/')
def home():
    return "Hello, world!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Ruta para manejar la compra de criptomonedas
@app.route('/buy', methods=['POST'])
def buy_crypto():
    data = request.json
    buyer = data['buyer']
    amount = data['amount']
    
    # Lógica para validar el pago con PayPal
    payment_success = validate_paypal_payment(data['payment_details'])
    
    if payment_success:
        # Aquí iría la lógica para crear la transacción en la blockchain
        # blockchain.create_transaction(buyer, amount, "crypto")
        return jsonify({'status': 'success', 'message': f'Transaction successful: {buyer} received {amount} tokens.'})
    else:
        return jsonify({'status': 'error', 'message': 'Payment validation failed.'})

def validate_paypal_payment(payment_details):
    # Aquí iría la lógica para validar el pago con PayPal
    # Placeholder para el ejemplo
    return True

if __name__ == '__main__':
    app.run(debug=True)

