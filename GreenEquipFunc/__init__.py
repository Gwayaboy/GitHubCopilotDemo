'''
Create an Azure function that mimics turning and on and off industrial equipment.
I am using the carbon intensity of the grid as the trigger for turning on and off the equipment at https://api.carbonintensity.org.uk/intensity
if the actual carbon intensity of the grid is less than 100 gCO2/kWh then turn on the equipment
if the actual carbon intensity of the grid is greater than 100 gCO2/kWh then turn off the equipment

The response should be a json block with a key of "ShouldTurnOn" and a value of true or false
'''

import logging
import requests
import json
import os
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # Get the carbon intensity of the grid
    r = requests.get('https://api.carbonintensity.org.uk/intensity')
    # Check the status code of the response
    if r.status_code == 200:
        # Get the json from the response
        data = r.json()
        # Get the actual carbon intensity of the grid
        actual_intensity = data['data'][0]['intensity']['actual']
        # Check if the actual intensity is less than 100 gCO2/kWh
        if actual_intensity < 100:
            # Turn on the equipment
            should_turn_on = True
        else:
            # Turn off the equipment
            should_turn_on = False
        # Create a json response
        response = json.dumps({'ShouldTurnOn': should_turn_on})
        # Return the response
        return func.HttpResponse(response)
    else:
        # Return an error if the status code is not 200
        return func.HttpResponse('Error getting carbon intensity', status_code=400)