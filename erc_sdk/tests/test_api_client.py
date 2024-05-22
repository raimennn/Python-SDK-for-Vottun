import unittest
from erc.api_client import APIClient
from erc.endpoints import ERCEndpoints
from unittest.mock import patch

class TestAPIClient(unittest.TestCase):

    @patch('erc.api_client.requests.get')
    def test_get_resource(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'id': 1, 'name': 'Test Resource'}

        client = APIClient('http://api.example.com', 'fake_api_key')
        endpoints = ERCEndpoints(client)

        response = endpoints.get_resource(1)
        self.assertEqual(response, {'id': 1, 'name': 'Test Resource'})

if __name__ == '__main__':
    unittest.main()
