import os
import requests

orchestrator_endpoint = os.getenv("ORCHESTRATOR_ENDPOINT", "http://localhost:8080/api/orchestrate")

def get_orchestrator_response(command:str):
    
    custom_tools_definition=open("ae/orchestration/functions.json", "r").read()
    params = {
        "query": command,
        "sessionid": "1234", #to do , create a unique session id per run
        "use_custom_tools": "true",
        "tools_definition": custom_tools_definition
    }
    headers = {
        "accept": "application/json"
    }
    response = requests.post(orchestrator_endpoint, params=params, headers=headers)
    return response.json()