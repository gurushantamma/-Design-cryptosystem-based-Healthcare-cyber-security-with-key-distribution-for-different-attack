import hashlib
import json
import time
import sqlite3
class Block:
    def __init__(self, index, timestamp, patient_data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.patient_data = patient_data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'patient_data': self.patient_data,
            'previous_hash': self.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), new_data, latest_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

    def display_chain(self):
        for block in self.chain:
            print(f"\nBlock {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Patient Data: {block.patient_data}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")

# Example usage
healthchain = Blockchain()

conn = sqlite3.connect('Form.db')
with conn:
    cur = conn.cursor()
    fn=input("ENter Name")
    cur.execute("SELECT * FROM patient where fullname=? ", (fn,))
    rows = cur.fetchall()
    flag = 0
    for row in rows:
      healthchain.add_block({"patient_Name": row[0], "diagnosis": row[8], "Doctor": row[11]})

# Display blockchain
healthchain.display_chain()

# Check validity
print("\nIs blockchain valid?", healthchain.is_chain_valid())
