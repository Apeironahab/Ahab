from web3 import Web3

# Conectar a la red de Ethereum usando la URL de Infura
infura_url = 'https://mainnet.infura.io/v3/dc4192bdc43a43d5906af5629a61b5ac'
w3 = Web3(Web3.HTTPProvider(infura_url))

# Verificar conexión
if w3.is_connected():
    print("Conectado a Ethereum a través de Infura")
else:
    print("No se pudo conectar a Ethereum a través de Infura")

# Dirección a verificar (en formato no checksum)
address = '0x54baa6dfa3cabab2b8d8d1abf2e0d308be6ee7a0'

# Convertir la dirección a formato checksum
checksum_address = Web3.to_checksum_address(address)

# Verificar el saldo
balance = w3.eth.get_balance(checksum_address)

# Convertir el saldo de wei a ether
balance_in_ether = w3.from_wei(balance, 'ether')

print(f'Balance de {checksum_address}: {balance_in_ether} ETH')

