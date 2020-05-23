
import requests
import json
from   pprint import pprint

url     = "http://192.168.2.112:8080/cxrestapi/auth/identity/connect/token";
payload = "username=dcox&password=C0rky9%232016&grant_type=password&scope=sast_rest_api&client_id=resource_owner_client&client_secret=014DF517-39D1-4453-B7B3-9930C563627C";
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Postman-Token': "2580274e-5818-4a41-8e73-a55f0e6df770"
    };

response = requests.request("POST", url, data=payload, headers=headers);

print();
print("=============== JSON Response ===============");
print(response.text);

pretty_data = json.dumps(response.json(), indent=4);
 
print();
print("=============== JSON 'pretty print' Response ===============");
print(pretty_data);

print();
print("=============== JSON 'pprint' Response ===============");
pprint(response.json());

