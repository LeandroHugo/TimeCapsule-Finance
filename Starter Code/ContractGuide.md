# Time Lock Wallet in Solidity

In this guide, we will create a simple time lock wallet in Solidity. This wallet will allow deposits at any time but restricts withdrawals until a specified time has passed.

## Prerequisites

- Basic understanding of Solidity and smart contracts
- Ethereum development environment setup (e.g., Remix IDE)

## Step 1: Define the Contract and Variables

Start by defining the contract and the variables we will need.

```solidity
pragma solidity ^0.5.0;

contract TimeLockWallet {
    address payable public owner;
    uint public lockTime;
}
```

## Step 2: Define the Constructor

The constructor will set the owner of the contract to the address that deploys it.

```solidity
constructor() public {
    owner = msg.sender;
}
```

## Step 3: Define the Deposit Function

The deposit function will allow anyone to deposit funds into the contract. It checks that the value sent with the transaction is greater than zero.

```solidity
function deposit() public payable {
    require(msg.value > 0, "Must send some ether");
}
```

## Step 4: Define the Set Lock Time Function

The `setLockTime` function allows the owner to set the lock time of the contract. This function can only be called when the contract is empty to prevent funds from being locked indefinitely.

```solidity
function setLockTime(uint _lockTime) public {
    require(address(this).balance == 0, "Wallet must be empty to set the lock time");
    lockTime = _lockTime;
}
```

## Step 5: Define the Withdraw Function

The `withdraw` function allows the owner to withdraw funds from the contract. This function checks whether the current time is later than the lock time before allowing the withdrawal.

```solidity
function withdraw() public {
    require(msg.sender == owner, "Only the owner can withdraw");
    require(now > lockTime, "Wallet is locked");

    uint amount = address(this).balance;
    (bool success, ) = owner.call.value(amount)("");
    require(success, "Transfer failed.");
}
```

## Step 6: Define the Fallback Function

The fallback function will call the `deposit` function whenever the contract receives ether.

```solidity
function() external payable {
    deposit();
}
```

And that's it! You have now created a simple time lock wallet in Solidity. This wallet allows deposits at any time but restricts withdrawals until a specified time has passed.