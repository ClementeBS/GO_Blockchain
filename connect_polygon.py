from web3 import Web3


infura_url = 'https://polygon-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'

web3 = Web3(Web3.HTTPProvider(infura_url))

try:
    if web3.is_connected():
        print("Connected to the Polygon Network")
    else:
        print("Failed to connect")
except Exception as e:
    print(f"An error occurred: {e}")


