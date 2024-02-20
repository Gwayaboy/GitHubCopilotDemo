# Developer assisted Generative AI with GitHub Co-pilot and chat (preview) Demo

- Task 1: Create an azure function with an unknow programming language that reads from the [carbon intensity](https://api.carbonintensity.org.uk/) api and makes decisions to enable or disable a set of equipment in your factory. The azure function should store the state.

- Task 2: Write unit tests for the function


# Steps

- Task 1:
    Install the Azure Functions Core Tool with the help of Github Copilot Chat (preview)?

    - How to install the latest Azure Functions SDK and tooling with npm to scafflold a HTTP triggered python function?
    
        ![](/img/installFunc.png)

    - How can I test my HTTP triggered Python function locally?

        ![](/img/testFuncLocally.png)

    Prompting GitHub copilot to generate function
    - Scrap the generate code fr
    - Start with an outline the requirements with examples and uses cases

        ```python 
            '''
            Create an Azure function that mimics turning and on and off industrial equipment.
            I am using the carbon intensity of the grid as the trigger for turning on and off the equipment at https://api.carbonintensity.org.uk/intensity
            if the actual carbon intensity of the grid is less than 100 gCO2/kWh then turn on the equipment
            if the actual carbon intensity of the grid is greater than 100 gCO2/kWh then turn off the equipment
            '''
        ```

    - see co-pilot suggestions and browse through multiple suggestions to understand iteratively what context is missing

    - Adding will give some context on what the response should look like
    
        ```python 
        '''
        The response should be a json block with a key of "ShouldTurnOn" and a value of true or false
        '''
        ```


