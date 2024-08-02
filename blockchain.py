import hashlib

class Blockchain:
    def __init__(self, total_supply):
        self.chain = [self.create_genesis_block()]
        self.current_transactions = []
        self.total_supply = total_supply
        self.balances = {"genesis_address": total_supply}
        
    def create_genesis_block(self):
        block = {
            'index': 1,
            'previous_hash': '0',
            'transactions': [],
            'nonce': 0
        }
        block['hash'] = self.hash_block(block)
        return block

    def create_transaction(self, sender, recipient, amount):
        if sender not in self.balances or self.balances[sender] < amount:
            raise ValueError("Insufficient funds")
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        
    def mine_block(self):
        block = {
            'index': len(self.chain) + 1,
            'previous_hash': self.chain[-1]['hash'],
            'transactions': self.current_transactions,
            'nonce': 0
        }
        block['hash'] = self.hash_block(block)
        self.chain.append(block)
        self.current_transactions = []
        
        # Update balances
        for tx in block['transactions']:
            sender = tx['sender']
            recipient = tx['recipient']
            amount = tx['amount']
            self.balances[sender] -= amount
            if recipient in self.balances:
                self.balances[recipient] += amount
            else:
                self.balances[recipient] = amount

    def hash_block(self, block):
        block_string = f"{block['index']}{block['previous_hash']}{block['transactions']}{block['nonce']}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def get_balance(self, address):
        return self.balances.get(address, 0)

