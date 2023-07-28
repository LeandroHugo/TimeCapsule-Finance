pragma solidity ^0.5.0;

contract TimeLockWallet {
    address payable public owner;
    uint public balance;
    uint public lockTime;

    event Deposited(address from, uint amount, uint balance);
    event Withdrawn(address to, uint amount, uint balance);

    constructor() public {
        owner = msg.sender;
    }

    function deposit() public payable {
        require(msg.value > 0, "Must send some ether");
        balance += msg.value;
        emit Deposited(msg.sender, msg.value, balance);
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
        emit Withdrawn(owner, amount, balance);
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
