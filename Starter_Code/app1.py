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
				"indexed": True,
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
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "message",
				"type": "string"
			}
		],
		"name": "Deposited",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "newLockTime",
				"type": "uint256"
			}
		],
		"name": "LockTimeUpdated",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
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
		"name": "admin",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
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
		"constant": False,
		"inputs": [
			{
				"internalType": "address payable",
				"name": "newOwner",
				"type": "address"
			}
		],
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
				"internalType": "string",
				"name": "message",
				"type": "string"
			}
		],
		"name": "depositWithMessage",
		"outputs": [],
		"payable": True,
		"stateMutability": "payable",
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
	},
	{
		"constant": False,
		"inputs": [
			{
				"internalType": "address",
				"name": "_admin",
				"type": "address"
			}
		],
		"name": "setAdmin",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
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
		"constant": False,
		"inputs": [
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "withdraw",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	}
]

# The contract address that you get after deploying your smart contract
contract_address = '0x88Dae24EbC7F8a30c7eBeF7FEF6b4dcCD283e3d1'

# Creating contract instance
contract = web3.eth.contract(address=contract_address, abi=ABI)

st.sidebar.image('sidebar.png')  # Add this line to display your logo in the sidebar
# 🎈🖼️ Streamlit App
st.title('⏳ TimeLock Wallet')  # 🏦

# 🕵️‍♂️ Contract Owner
owner = st.sidebar.text_input("👤 OWNER WALLET ADDRESS", value="0xYourAddress")  # 🔑

# Owner's Panel
if owner == web3.eth.accounts[0]:
    st.header('👋 Welcome Owner')

    # 💰 Deposit
    deposit_amount = st.slider('💲 Select deposit amount:', min_value=0.0, max_value=100.0, step=0.1)  # 🎚️
    deposit_message = st.text_input('💌 Enter a message for the deposit:')  # 💬
    if st.button('💸 Deposit'):
        tx_hash = contract.functions.depositWithMessage(deposit_message).transact({'from': owner, 'value': web3.toWei(deposit_amount, 'ether')})  # 📨
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)  # 🧾
        st.success(f"💵 Deposit successful. Transaction hash: {receipt['transactionHash'].hex()}")  # 🥳
        st.audio('depositsuccessful.mp3') # 🎵 Play success sound
        st.balloons()  # 🎈🎈🎈

    # ⏳ Set Lock Time
    lock_time = st.number_input('⏲️ Enter lock time', step=1)  # ⏱️
    time_unit = st.radio('⌚ Select lock time unit:', ('Seconds', 'Minutes', 'Hours', 'Days', 'Weeks', 'Months', 'Years'))  # 🔄
#     time_unit = st.selectbox('Select time unit', ['Seconds', 'Minutes', 'Hours', 'Days', 'Weeks', 'Months', 'Years'])

    # Convert the lock time to seconds based on the selected time unit
    if time_unit == 'Minutes':
        lock_time *= 60
    elif time_unit == 'Hours':
        lock_time *= 60 * 60
    elif time_unit == 'Days':
        lock_time *= 60 * 60 * 24
    elif time_unit == 'Weeks':
        lock_time *= 60 * 60 * 24 * 7
    elif time_unit == 'Months':
        lock_time *= 60 * 60 * 24 * 30
    elif time_unit == 'Years':
        lock_time *= 60 * 60 * 24 * 365

    if st.button('🔒 Set Lock Time'):
        tx_hash = contract.functions.setLockTime(int(lock_time)).transact({'from': owner})  # 🔐
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)  # 🧾
        st.success(f"⌛ Lock time set. Transaction hash: {receipt['transactionHash'].hex()}")  # 🥳
        st.balloons()  # 🎈🎈

    # 💵 Withdraw
    withdraw_amount = st.slider('💰 Select withdrawal amount:', min_value=0.0, max_value=100.0, step=0.1)  # 🎚️
    if st.button('💵 Withdraw'):
        tx_hash = contract.functions.withdraw(web3.toWei(withdraw_amount, 'ether')).transact({'from': owner})  # 📤
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)  # 🧾
        st.success(f"🏧 Withdrawal successful. Transaction hash: {receipt['transactionHash'].hex()}")  # 🥳
        st.balloons()  # 🎈🎈

# ⚠️ Withdrawal Warning
st.warning("⚠️ Please be aware that withdrawal transactions may be subject to fees.")  # 💸

# 💀 Deadman Switch
use_deadman_switch = st.checkbox('💀 Activate Deadman Switch')  # ☑️
if use_deadman_switch:
    new_owner = st.text_input("🔄 Enter new owner address")  # 🔄
    if Web3.isAddress(new_owner):  # ✅
        tx_hash = contract.functions.deadmanSwitch(new_owner).transact({'from': owner})  # 💀
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)  # 🧾
        st.success(f"🔄 Deadman Switch activated. New owner is {new_owner}. Transaction hash: {receipt['transactionHash'].hex()}")  # 🎉
        st.balloons()  # 🎈🎈
    else:
        st.error("❌ The address entered is not valid. Please enter a valid Ethereum address.")  # 🚫