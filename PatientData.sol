// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PatientData {
    address public patient;
    string public encryptedData;
    mapping(address => bool) public doctorApproved;

    constructor(string memory _data) {
        patient = msg.sender;
        encryptedData = _data;
    }

    function approveDoctor(address _doctor) public {
        require(msg.sender == patient, "Only patient can approve.");
        doctorApproved[_doctor] = true;
    }

    function getEncryptedData() public view returns (string memory) {
        require(doctorApproved[msg.sender], "Access denied");
        return encryptedData;
    }
}
