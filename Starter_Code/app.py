import streamlit as st
from web3 import Web3
import json

# Use Ganache for local blockchain development
GANACHE_URL = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(GANACHE_URL))

# This should be the contract ABI (Application Binary Interface), which you get after compiling your smart contract
# For simplicity, let's use an empty list
ABI = [
	{
		"constant":False,
		"inputs": [],
		"name": "deadmanSwitch",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [],
		"name": "deposit",
		"outputs": [],
		"payable": True,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_lockTime",
				"type": "uint256"
			}
		],
		"name": "setLockTime",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "balance",
				"type": "uint256"
			}
		],
		"name": "Deposited",
		"type": "event"
	},
	{
		"constant": False,
		"inputs": [],
		"name": "withdraw",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "balance",
				"type": "uint256"
			}
		],
		"name": "Withdrawn",
		"type": "event"
	},
	{
		"payable": True,
		"stateMutability": "payable",
		"type": "fallback"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "balance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "lockTime",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address payable",
				"name": "",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	}
]



# The contract address that you get after deploying your smart contract
contract_address = '0x88Dae24EbC7F8a30c7eBeF7FEF6b4dcCD283e3d1'

# Creating contract instance
contract = web3.eth.contract(address=contract_address, abi=ABI)

# Streamlit App
st.title('TimeLock Wallet')

# Set owner of the contract
owner = st.sidebar.text_input("Owner Address", value="0xYourAddress")

# If contract owner, show options
if owner == web3.eth.accounts[0]:
    st.header('Welcome Owner')

    # Deposit
    if st.button('Deposit'):
        tx_hash = contract.functions.deposit().transact({'from': owner, 'value': web3.toWei(1, 'ether')})
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        st.write(f"Deposit successful. Transaction hash: {receipt['transactionHash'].hex()}")

    # Set lock time
    if st.button('Set Lock Time'):
        lock_time = st.number_input('Enter lock time in seconds', step=1)
        tx_hash = contract.functions.setLockTime(int(lock_time)).transact({'from': owner})
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        st.write(f"Lock time set. Transaction hash: {receipt['transactionHash'].hex()}")

    # Withdraw
    if st.button('Withdraw'):
        tx_hash = contract.functions.withdraw().transact({'from': owner})
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        st.write(f"Withdrawal successful. Transaction hash: {receipt['transactionHash'].hex()}")

    # Deadman Switch
    if st.button('Activate Deadman Switch'):
        new_owner = st.text_input("Enter new owner address")
        tx_hash = contract.functions.deadmanSwitch(new_owner).transact({'from': owner})
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        st.write(f"Deadman Switch activated. New owner is {new_owner}. Transaction hash: {receipt['transactionHash'].hex()}")

else:
    st.write("You are not the owner of this contract.")