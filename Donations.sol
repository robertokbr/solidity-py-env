// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

contract Donations {
  mapping(address => uint256) public donors;
  address public owner;

  constructor() public {
    owner = msg.sender;
  }

  modifier onlyOwner() {
    require(msg.sender == owner, "Only the contract owner is allowed to do it!");
    _;
  }

  function donate() public payable {
    donors[msg.sender] = msg.value;
  }

  function withdraw() public onlyOwner payable {
    payable(msg.sender).transfer(address(this).balance);
  }
}