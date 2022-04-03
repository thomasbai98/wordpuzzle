// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.2;

contract ERC20Puzz {
    string  public name = "Puzzle";
    string  public symbol = "PUZ";
    uint public decimal=18;
    uint256 public totalSupply;
    address public creator;
    uint price=1* (10 ** 18);

    mapping(address => uint256) public balanceOf;
    mapping(address => uint) public buytime;
    constructor  (uint256 _initialSupply)  {
        balanceOf[msg.sender] = _initialSupply * (10 ** 18);
        totalSupply = _initialSupply;
        creator = msg.sender;
    }

    function buy() public returns (bool success) {
        buytime[msg.sender]=block.timestamp;
        return transferFrom(msg.sender, creator, price);
    }

    function report() public returns (bool success) {
        require(buytime[msg.sender]!=0,"buy one first");
        uint time = block.timestamp - buytime[msg.sender];
        buytime[msg.sender]=0;
        return transferFrom(creator,msg.sender, price * 10 / time);
    }

    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value);
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        return true;
    }


    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(_value <= balanceOf[_from]);
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        return true;
    }
}