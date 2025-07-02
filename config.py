from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

# Replace with your Ganache accounts
patient_account = w3.eth.accounts[0]
doctor_account = w3.eth.accounts[1]
