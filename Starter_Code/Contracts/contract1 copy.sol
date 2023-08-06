pragma solidity ^0.8.0;

contract TimeLockWallet {

    address public owner;
    address public admin;
    uint public lockTime;
    
    // Deadman Switch variables
    uint public lastActive;
    uint public inactivityPeriod = 31536000; // Default to 1 year (in seconds)

    event Deposited(address indexed from, uint value, uint balance, string message);
    event Withdrawn(address indexed to, uint value, uint balance);
    event LockTimeUpdated(uint newLockTime);
    event Transfer(address indexed from, address indexed to, uint value, uint balance);

    constructor() {
        owner = msg.sender;
        lastActive = block.timestamp; // Updated to block.timestamp (previously 'now' in older versions)
    }

    function setAdmin(address newAdmin) public {
        require(msg.sender == owner, "Only the owner can set the admin");
        admin = newAdmin;
    }

    function deposit() public payable {
        require(msg.value > 0, "Must send some ether");
        emit Deposited(msg.sender, msg.value, address(this).balance, "");
    }

    function depositWithMessage(string memory message) public payable {
        require(msg.value > 0, "Must send some ether");
        emit Deposited(msg.sender, msg.value, address(this).balance, message);
    }

    function setLockTime(uint durationInSeconds) public {
        require(msg.sender == admin, "Only the admin can set the lock time");
        lockTime = block.timestamp + durationInSeconds;
        emit LockTimeUpdated(lockTime);
    }

    function withdraw(uint amount) public {
        require(msg.sender == owner, "Only the owner can withdraw");
        require(block.timestamp >= lockTime, "Wallet is locked");
        require(amount <= address(this).balance, "Insufficient balance");
        refreshLastActive(); // Refresh the last active timestamp
        payable(owner).transfer(amount); // Updated to use payable for addresses in ^0.8.0
        emit Withdrawn(owner, amount, address(this).balance);
    }

    function deadmanSwitch(address newOwner) public {
        require(msg.sender == owner, "Only the owner can activate the deadman switch");
        owner = newOwner;
    }

    function transfer(address payable recipient, uint amount) public {
        require(msg.sender == owner, "Only the owner can transfer");
        require(amount <= address(this).balance, "Insufficient balance");
        refreshLastActive(); // Refresh the last active timestamp
        recipient.transfer(amount);
        emit Transfer(owner, recipient, amount, address(this).balance);
    }

    // Internal function to refresh the lastActive timestamp
    function refreshLastActive() internal {
        lastActive = block.timestamp;
    }

    // Function to allow the backup owner to claim ownership
    function claimOwnership() public {
        require(block.timestamp >= lastActive + inactivityPeriod, "Owner is still active");
        owner = msg.sender;
    }

    // Fallback function
    fallback() external payable {
        deposit();
    }
}
