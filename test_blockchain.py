import pytest
from blockchain import Blockchain

def test_transfer():
    total_supply = 444444444.444
    blockchain = Blockchain(total_supply)
    blockchain.create_transaction("genesis_address", "0xRecipientAddress", 1000)
    blockchain.mine_block()
    assert blockchain.get_balance("0xRecipientAddress") == 1000
    assert blockchain.get_balance("genesis_address") == total_supply - 1000

def test_check_balance():
    total_supply = 444444444.444
    blockchain = Blockchain(total_supply)
    blockchain.create_transaction("genesis_address", "0x54baa6DFa3CAbAB2b8d8d1abf2e0d308bE6EE7a0", 1000)
    blockchain.mine_block()
    assert blockchain.get_balance("0x54baa6DFa3CAbAB2b8d8d1abf2e0d308bE6EE7a0") == 1000

def test_insufficient_funds():
    total_supply = 444444444.444
    blockchain = Blockchain(total_supply)
    with pytest.raises(ValueError, match="Insufficient funds"):
        blockchain.create_transaction("genesis_address", "0xRecipientAddress", total_supply + 1)
    assert blockchain.get_balance("genesis_address") == total_supply

def test_block_integrity():
    total_supply = 444444444.444
    blockchain = Blockchain(total_supply)
    blockchain.create_transaction("genesis_address", "0xRecipientAddress", 1000)
    blockchain.mine_block()
    assert len(blockchain.chain) > 1
    assert blockchain.chain[-1]['transactions'][0]['amount'] == 1000

def test_high_volume_transactions():
    total_supply = 444444444.444
    blockchain = Blockchain(total_supply)
    for _ in range(1000):
        blockchain.create_transaction("genesis_address", "0xRecipientAddress", 1)
    blockchain.mine_block()
    assert blockchain.get_balance("0xRecipientAddress") == 1000

