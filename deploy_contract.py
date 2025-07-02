
import json
import os
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

# Replace with your Ganache accounts
patient_account = w3.eth.accounts[0]
doctor_account = w3.eth.accounts[1]
# Load contract
with open("F:/PDA2024/healthblcokchain/contracts/PatientData.sol", "r") as file:
    source_code = file.read()

from solcx import compile_source
compiled_sol = compile_source(source_code)
contract_id, contract_interface = compiled_sol.popitem()

# Deploy contract
PatientData = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
with open("F:/PDA2024/healthblcokchain/data/encrypted_record.txt", "rb") as f:
    encrypted_data = f.read().decode()

tx_hash = PatientData.constructor(encrypted_data).transact({'from': patient_account})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print("Contract deployed at:", tx_receipt.contractAddress)

# Save ABI and address
with open("contract_details.json", "w") as f:
    json.dump({
        "abi": contract_interface['abi'],
        "address": tx_receipt.contractAddress
    }, f, indent=4)
