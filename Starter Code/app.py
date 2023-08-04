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
    # ...
]


# The contract address that you get after deploying your smart contract
contract_address = '0x3F04bB7a6f01c94fAc0F33A796915eAc4E923e7F'

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
        lock_time = st.number_input('Enter lock time in seconds')
        tx_hash = contract.functions.setLockTime(lock_time).transact({'from': owner})
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        st.write(f"Lock time set. Transaction hash: {receipt['transactionHash'].hex()}")

    # Withdraw
    if st.button('Withdraw'):
        tx_hash = contract.functions.withdraw().transact({'from': owner})
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        st.write(f"Withdrawal successful. Transaction hash: {receipt['transactionHash'].hex()}")
else:
    st.write("You are not the owner of this contract.")