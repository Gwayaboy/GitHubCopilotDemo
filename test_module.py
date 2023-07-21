#write unit tests for the Azure function and mock the response from an external API

# Path: test_module.py


import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
import GreenEquipFunc.__init__ as func

class TestGreenEquipFunc(unittest.TestCase):
    def test_main(self):
        # Create a mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'data': [
                {
                    'intensity': {
                        'actual': 50
                    }
                }
            ]
        }
        # Patch the requests.get method to return the mock response
        with patch('GreenEquipFunc.__init__.requests.get', return_value=mock_response) as mock_get:
            # Call the function
            response = func.main(None)
            # Check the status code
            self.assertEqual(response.status_code, 200)
            # Check the response body
            self.assertEqual(response.get_body(), b'{"ShouldTurnOn": true}')
            # Check the call to requests.get
            mock_get.assert_called_once_with('https://api.carbonintensity.org.uk/intensity')
            
    def test_main_error(self):
        # Create a mock response
        mock_response = MagicMock()
        mock_response.status_code = 400
        # Patch the requests.get method to return the mock response
        with patch('GreenEquipFunc.__init__.requests.get', return_value=mock_response) as mock_get:
            # Call the function
            response = func.main(None)
            # Check the status code
            self.assertEqual(response.status_code, 400)
            # Check the response body
            self.assertEqual(response.get_body(), b'Error getting carbon intensity')
            # Check the call to requests.get
            mock_get.assert_called_once_with('https://api.carbonintensity.org.uk/intensity')