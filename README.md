# Proof of Concept: GO Certificates on Polygon Network

## Overview

This proof of concept demonstrates a blockchain solution for creating and managing Guarantee of Origin (GO) certificates using the Polygon network. The system employs a smart contract written in Solidity and a Python client to interact with the blockchain.

## Requirements

- **Python 3.x**
- **Libraries**: `web3`, `dotenv`
- **Polygon Account**: Private key from MetaMask
- **Infura Project ID**
- **Contract ABI**: Saved as `contract_abi.json`

## Smart Contract

The smart contract, written in Solidity, defines the structure and functions for GO certificates. Each certificate contains an ID, producer name, energy amount, and production date. The contract ensures that each certificate has a unique ID and cannot be overwritten.

## Infura

Infura is a service that provides easy access to the Ethereum and Polygon networks via API. It allows developers to connect their applications to the blockchain without needing to run their own nodes. For this proof of concept, Infura is used to connect the Python client to the Polygon network.

## Python Client

The Python client uses `web3.py` to interact with the deployed smart contract on the Polygon network. The client provides functions to create and retrieve GO certificates.

### Environment Variables (`.env_local`):

Set up a `.env_local` file to securely store sensitive information.

```plaintext
INFURA_PROJECT_ID=your_infura_project_id
PRIVATE_KEY=your_private_key
CONTRACT_ADDRESS=your_contract_address
```

### Creating Certificates
The create_certificate function sends a transaction to the smart contract to create a new GO certificate with specified details such as producer, energy, and date. Each certificate is assigned a unique ID by the smart contract.

Example:
```plaintext
create_certificate("Solar Farm", "1000 kWh", "2024-06-30")
create_certificate("Wind Farm", "500 kWh", "2024-07-01")
create_certificate("Hydro Plant", "2000 kWh", "2024-08-15")
```
### Retrieving Certificates
The get_certificate function retrieves a certificate by its unique ID and prints the certificate details.

Example:
```plaintext
certificate_data = get_certificate(0)
print(certificate_data)
```

## Example Results
```plaintext
Connected to the Polygon Network

Transaction sent: 0x0cdc73a88e30835c381a8a070ea0b968808c9062b0ea41e2534711be654d1b46

Transaction receipt: AttributeDict({
    'blockHash': '0x76896aaab18e009c421d920e00eb9dbafb216c44db655b1b58254b37c132ef2b',
    'blockNumber': 59669862,
    'from': '0x4F31597472874bA32368B1265ebFaF384ac50416',
    'gasUsed': 120832,
    'status': 1,
    'to': '0x38Ab9E0eEFf8b1De8503236FE40F25f194B16C60',
    'transactionHash': '0x0cdc73a88e30835c381a8a070ea0b968808c9062b0ea41e2534711be654d1b46',
    'transactionIndex': 0,
    // Other fields omitted for brevity
})

Certificate Data: (4, 'Hydro Plant', '2000 kWh', '2024-07-01')
```
