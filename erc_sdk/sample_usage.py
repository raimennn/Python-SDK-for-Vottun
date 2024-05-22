from erc import ERCSDK

# Replace these with your actual base URL and API key
base_url = 'http://api.example.com'
api_key = 'your_api_key'

# Initialize the SDK
sdk = ERCSDK(base_url=base_url, api_key=api_key)

# Fetch a resource by ID
resource_id = 1
resource = sdk.endpoints.get_resource(resource_id)

# Print the fetched resource
print(resource)