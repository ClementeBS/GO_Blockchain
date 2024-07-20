from web3 import Web3

# Replace 'YOUR_INFURA_PROJECT_ID' with your actual Infura project ID
infura_url = 'https://polygon-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'

# Connect to the Polygon node
web3 = Web3(Web3.HTTPProvider(infura_url))

try:
    # Check if connection is successful
    if web3.is_connected():
        print("Connected to the Polygon Network")
    else:
        print("Failed to connect")
except Exception as e:
    print(f"An error occurred: {e}")


