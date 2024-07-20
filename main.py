import json
from dotenv import load_dotenv
import os
from go_engine import GOEngine


# Load environment variables from .env_local file
load_dotenv('.env_local')
infura_project_id = os.getenv('INFURA_PROJECT_ID')
private_key = os.getenv('PRIVATE_KEY')
contract_address = os.getenv('CONTRACT_ADDRESS')

# Load the ABI
with open('contract_abi.json', 'r') as abi_file:
    contract_abi = json.load(abi_file)

# GOEngine setup
go_engine = GOEngine(
    infura_project_id=infura_project_id,
    contract_address=contract_address,
    private_key=private_key,
    contract_abi=contract_abi
)

# Ping
if not go_engine.is_connected():
    print("Failed to connect to the Polygon Network")
    exit()
print("Connected to the Polygon Network")

# Create certificate
go_certificate = {
    "producer": "Wind Farm",
    "energy": "700 kWh",
    "date": "2024-06-30"
}
upload_certificate = False

# Upload certificate
if upload_certificate:
    go_engine.create_certificate(
        producer=go_certificate["producer"],
        energy=go_certificate["energy"],
        date=go_certificate["date"]
    )
else:
    print("Certificate was set to not be uploaded")

# Read certificate
certificate_data = go_engine.get_certificate(3)
print(certificate_data)
