pragma solidity ^0.5.0;

contract TimeLockWallet {
    address payable public owner;
    uint balance;
    uint public lockTime;

    constructor() public {
        owner = msg.sender;
    }

    function deposit(uint amount) public payable {
        require(msg.value > 0, "Must send some ether");
        balance = address(this).balance;
    }

    function setLockTime(uint _lockTime) public {
        // Only allow setting the lock time when the wallet is created or when it's empty
        require(address(this).balance == 0, "Wallet must be empty to set the lock time");
        lockTime = _lockTime;
    }

    function withdraw(uint amount) public {
        require(msg.sender == owner, "Only the owner can withdraw");
        require(now > lockTime, "Wallet is locked");

        uint amount = address(this).balance;
        (bool success, ) = owner.call.value(amount)("");
        require(success, "Transfer failed.");
    }

    function deadmanSwitch() public {
        require()
    }

    function() external payable {
    }
}
