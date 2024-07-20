// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GOContract {
    struct Certificate {
        uint256 id;
        string producer;
        string energy;
        string date;
    }

    mapping(uint256 => Certificate) public certificates;
    uint256 public nextId;

    function createCertificate(string memory producer, string memory energy, string memory date) public {
        certificates[nextId] = Certificate(nextId, producer, energy, date);
        nextId++;
    }

    function getCertificate(uint256 id) public view returns (Certificate memory) {
        return certificates[id];
    }
}
