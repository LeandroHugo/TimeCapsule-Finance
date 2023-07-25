pragma solidity ^0.5.0;

contract TimeLockWallet {
    address payable public owner;
    uint public lockTime;

    constructor() public {
        owner = msg.sender;
    }

    function deposit() public payable {
        require(msg.value > 0, "Must send some ether");
    }

    function setLockTime(uint _lockTime) public {
        // Only allow setting the lock time when the wallet is created or when it's empty
        require(address(this).balance == 0, "Wallet must be empty to set the lock time");
        lockTime = _lockTime;
    }

    function withdraw() public {
        require(msg.sender == owner, "Only the owner can withdraw");
        require(now > lockTime, "Wallet is locked");

        uint amount = address(this).balance;
        (bool success, ) = owner.call.value(amount)("");
        require(success, "Transfer failed.");
    }

    function() external payable {
        deposit();
    }
}
