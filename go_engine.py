from web3 import Web3
from web3.exceptions import TimeExhausted, TransactionNotFound
from typing import Any


class GOEngine:

    def __init__(
            self,
            infura_project_id: str,
            contract_address: str,
            private_key: str,
            contract_abi: Any
    ):
        infura_url = f'https://polygon-mainnet.infura.io/v3/{infura_project_id}'
        self.web3 = Web3(Web3.HTTPProvider(infura_url))
        self.private_key = private_key
        self.account = self.web3.eth.account.from_key(private_key)
        contract_address = Web3.to_checksum_address(contract_address)
        self.contract = self.web3.eth.contract(address=contract_address, abi=contract_abi)

    def is_connected(self) -> bool:
        try:
            # Check if connection is successful
            if self.web3.is_connected():
                return True
            else:
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def create_certificate(self, producer, energy, date):
        nonce = self.web3.eth.get_transaction_count(
            self.account.address
        )
        gas_price = self.web3.to_wei('100', 'gwei')  # Increase the gas price to 100 gwei
        txn = self.contract.functions.createCertificate(producer, energy, date).build_transaction({
            'chainId': 137,  # Chain ID for Polygon
            'gas': 2000000,
            'gasPrice': gas_price,
            'nonce': nonce
        })
        signed_txn = self.web3.eth.account.sign_transaction(
            txn,
            private_key=self.private_key
        )
        tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f"Transaction sent: {tx_hash.hex()}")

        try:
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash, timeout=300)  # Increase timeout to 300 seconds
            print(f"Transaction receipt: {receipt}")
        except TimeExhausted as ex:
            print(f"Transaction not confirmed in time: {ex}")
        except TransactionNotFound as ex:
            print(f"Transaction not found: {ex}")
        except Exception as ex:
            print(f"An error occurred: {ex}")

    def get_certificate(self, contract_id: int):
        certificate = self.contract.functions.getCertificate(contract_id).call()
        print(f"Certificate Data: {certificate}")
        return certificate




