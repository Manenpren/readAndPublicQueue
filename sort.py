from numpy import record
import requests  
from queue01 import QueueService

print("Reading data...")
URL = 'https://jsonplaceholder.typicode.com/posts' 

data = requests.get(URL) 

data = data.json() 

response = {}

for element in data: 
    if not response.get(element['userId']): 
        response[element['userId']] =  { 'records':[]}
    else:
        element_replace = response[element['userId']]['records']
        element_replace.append(element)

queue_service = QueueService.create()

response_queue = queue_service.callqueue(response)

print(f'Response Queue: {response_queue}')


