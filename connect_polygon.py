from web3 import Web3

# Replace 'YOUR_INFURA_PROJECT_ID' with your actual Infura project ID
infura_url = 'https://polygon-mainnet.infura.io/v3/7b21cd85b26742869b461b15019499c4'

# Connect to the Polygon node
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if connection is successful
if web3.is_connected():
    print("Connected to the Polygon Network")
else:
    print("Failed to connect")
