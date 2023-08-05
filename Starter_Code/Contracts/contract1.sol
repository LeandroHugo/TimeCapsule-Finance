pragma solidity ^0.5.0;

contract TimeLockWallet {
    address payable public owner;
    address public admin;

    uint public balance;
    uint public lockTime;

    event Deposited(address indexed from, uint amount, uint balance, string message);
    event Withdrawn(address indexed to, uint amount, uint balance);
    event LockTimeUpdated(uint newLockTime);
    event Transfer(address indexed from, address indexed to, uint amount, uint balance);

    constructor() public {
        owner = msg.sender;
        admin = msg.sender;  // Initially, the admin is the same as the owner
    }

    function setAdmin(address _admin) public {
        require(msg.sender == owner, "Only the owner can set the admin");
        admin = _admin;
    }

    function deposit() public payable {
        require(msg.value > 0, "Must send some ether");
        balance += msg.value;
        emit Deposited(msg.sender, msg.value, balance, "");
    }

    function depositWithMessage(string memory message) public payable {
        require(msg.value > 0, "Must send some ether");
        balance += msg.value;
        emit Deposited(msg.sender, msg.value, balance, message);
    }

    function setLockTime(uint _lockTime) public {
        // Only the admin can set the lock time
        require(msg.sender == admin, "Only the admin can set the lock time");
        lockTime = _lockTime;
        emit LockTimeUpdated(_lockTime);
    }

    function withdraw(uint amount) public {
        require(msg.sender == owner, "Only the owner can withdraw");
        require(now >= lockTime, "Wallet is locked");
        require(amount <= balance, "Insufficient balance");

        balance -= amount;
        owner.transfer(amount);
        emit Withdrawn(owner, amount, balance);
    }

    function deadmanSwitch(address payable newOwner) public {
        // Allow the owner to transfer ownership to a backup owner
        require(msg.sender == owner, "Only the owner can use the deadman switch");
        owner = newOwner;
    }

    function transfer(address payable recipient, uint amount) public {
        require(msg.sender == owner, "Only the owner can transfer");
        require(amount <= balance, "Insufficient balance");

        balance -= amount;
        recipient.transfer(amount);
        emit Transfer(owner, recipient, amount, balance);
    }

    function() external payable {
        deposit();
    }
}
