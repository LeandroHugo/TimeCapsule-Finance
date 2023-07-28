pragma solidity ^0.5.0;

contract TimeLockWallet {
    address payable public owner;
    uint public balance;
    uint public lockTime;

    constructor() public {
        owner = msg.sender;
    }

    function deposit() public payable {
        require(msg.value > 0, "Must send some ether");
        balance = address(this).balance;
    }

    function setLockTime(uint _lockTime) public {
        // Only allow setting the lock time when the wallet is created or when it's empty
        require(balance == 0, "Wallet must be empty to set the lock time");
        lockTime = _lockTime;
    }

    function withdraw() public {
        require(msg.sender == owner, "Only the owner can withdraw");
        require(now >= lockTime, "Wallet is locked");

        uint amount = balance;
        (bool success, ) = owner.call.value(amount)("");
        require(success, "Transfer failed.");
        balance = 0;
    }

    function deadmanSwitch() public {
        // Let's say the deadman switch allows the owner to reset the lockTime, for now
        require(msg.sender == owner, "Only the owner can use the deadman switch");
        lockTime = 0;
    }

    function() external payable {
        deposit();
    }
}


// In this version, the deposit function no longer takes an amount argument.
// Instead, it uses the msg.value directly from the transaction, which is the usual way to handle deposits in Solidity.

// The withdraw function now only withdraws the entire balance of the contract and resets the balance to zero.
// Also, the lockTime comparison has been changed to >= to allow for withdrawal exactly at lockTime.

// I've made the deadmanSwitch function reset the lockTime to zero, allowing immediate withdrawal. 
// This is just an example, you should replace it with your desired functionality.

// Lastly, the fallback function now calls the deposit function, meaning any Ether
//  sent to the contract without data will be treated as a deposit.