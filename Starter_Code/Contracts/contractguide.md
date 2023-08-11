# TimeLockWallet in Solidity

In this guide, we delve into the construction of a basic time lock wallet using Solidity. This wallet is designed to permit deposits at any given moment but sets constraints on withdrawals based on a predetermined time frame.

## Prerequisites

- An introductory knowledge of Solidity and smart contracts.
- An environment set up for Ethereum development (for instance, Remix IDE).

## Step 1: Initiate the Contract and Variables

Kick off by laying down the contract and listing out the variables that will be required.

```solidity
pragma solidity ^0.5.0;

contract TimeLockWallet {
    address payable public owner;
    uint public balance;
    uint public lockTime;
}
```

## Step 2: Set Up the Constructor

The constructor function is designed to assign the contract's owner to the address that initiates it.

```solidity
constructor() public {
    owner = msg.sender;
}
```

## Step 3: Structure the Deposit Functions

We'll construct two deposit functions. The primary deposit function permits any user to place funds into the wallet. It ensures the transaction value is positive. The secondary one, `depositAndSetLockTime`, sets the `lockTime` during the initial deposit.

```solidity
function deposit() public payable {
    require(msg.value > 0, "Must send some ether");
    balance += msg.value;
}

function depositAndSetLockTime(uint _lockTimeInSeconds) public payable {
    require(msg.value > 0, "Must send some ether");
    balance += msg.value;

    if (balance == msg.value) { 
        lockTime = now + _lockTimeInSeconds;
    }
}
```

## Step 4: Draft the Withdraw Function

The `withdraw` function enables the owner to retrieve funds from the contract. It verifies if the current time surpasses the `lockTime` before authorizing the withdrawal.

```solidity
function withdraw() public {
    require(msg.sender == owner, "Only the owner can withdraw");
    require(now >= lockTime, "Wallet is locked");

    uint amount = balance;
    balance = 0;
    owner.transfer(amount);
}
```

## Step 5: Create the Deadman Switch

The `deadmanSwitch` is a function that acts as a safety protocol, letting the existing owner transfer ownership to another address in cases of emergencies.

```solidity
function deadmanSwitch(address payable newOwner) public {
    require(msg.sender == owner, "Only the owner can use the deadman switch");
    owner = newOwner;
}
```

## Step 6: Design the Fallback Function

The fallback function is structured to invoke the `deposit` function whenever the contract receives ether.

```solidity
function() external payable {
    depositAndSetLockTime(0);
}
```

Congratulations! You have now successfully fashioned a rudimentary time lock wallet using Solidity. This wallet is capable of receiving deposits at any point in time but imposes limitations on withdrawals based on a pre-set duration.