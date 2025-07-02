
import json
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

# Replace with your Ganache accounts
patient_account = w3.eth.accounts[0]
doctor_account = w3.eth.accounts[1]
# Load contract details
with open("contract_details.json") as f:
    details = json.load(f)

contract = w3.eth.contract(address=details["address"], abi=details["abi"])

# Approve doctor (run by patient)
tx = contract.functions.approveDoctor(doctor_account).transact({'from': patient_account})
w3.eth.wait_for_transaction_receipt(tx)
print("Doctor approved.")

# Doctor retrieves encrypted data
try:
    encrypted = contract.functions.getEncryptedData().call({'from': doctor_account})
    with open("data/encrypted_from_blockchain.txt", "w") as f:
        f.write(encrypted)
    print("Encrypted data retrieved from blockchain.")
except Exception as e:
    print("Access denied or error:", str(e))
