pragma solidity ^0.5.0;

contract TimeLockWallet {
    address payable public owner;
    address payable public backupOwner;
    uint public balance;
    uint public lockTime;

    event Deposited(address from, uint amount, uint balance);
    event Withdrawn(address to, uint amount, uint balance);
    event LockTimeUpdated(uint newLockTime);

    constructor(address payable _backupOwner) public {
        require(_backupOwner != address(0), "Backup owner address can't be zero");
        owner = msg.sender;
        backupOwner = _backupOwner;
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
        emit LockTimeUpdated(_lockTime);
    }

    function withdraw() public {
        require(msg.sender == owner || msg.sender == backupOwner, "Only the owner or backup owner can withdraw");
        require(now >= lockTime, "Wallet is locked");

        uint amount = balance;
        (bool success, ) = msg.sender.call.value(amount)("");
        require(success, "Transfer failed.");
        emit Withdrawn(msg.sender, amount, balance);
        balance = 0;
    }

    function deadmanSwitch(address payable newOwner) public {
        require(msg.sender == owner, "Only the owner can use the deadman switch");
        require(newOwner != address(0), "New owner address can't be zero");
        owner = newOwner;
        lockTime = 0;  // reset the lock time
    }

    function() external payable {
        deposit();
    }
}
