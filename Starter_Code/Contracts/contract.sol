pragma solidity ^0.5.0;

contract TimeLockWallet {
    address payable public owner;
    uint public balance;
    uint public lockTime;

    event Deposited(address from, uint amount, uint balance);
    event Withdrawn(address to, uint amount, uint balance);
    event LockTimeUpdated(uint newLockTime);

    constructor() public {
        owner = msg.sender;
    }

    function depositAndSetLockTime(uint _lockTimeInSeconds) public payable {
        require(msg.value > 0, "Must send some ether");
        balance += msg.value;

        if (balance == msg.value) { // Check if this is the initial deposit
            lockTime = now + _lockTimeInSeconds;
            emit LockTimeUpdated(lockTime);
        }

        emit Deposited(msg.sender, msg.value, balance);
    }

    function withdraw() public {
        require(msg.sender == owner, "Only the owner can withdraw");
        require(now >= lockTime, "Wallet is locked");

        uint amount = balance;
        balance = 0;
        owner.transfer(amount);
        emit Withdrawn(owner, amount, 0);
    }

    function deadmanSwitch(address payable newOwner) public {
        require(msg.sender == owner, "Only the owner can use the deadman switch");
        owner = newOwner;
    }

    function() external payable {
        depositAndSetLockTime(0);
    }
}
