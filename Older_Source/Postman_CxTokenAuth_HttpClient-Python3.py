import http.client

conn = http.client.HTTPConnection("192,168,2,112")

payload = "username=dcox&password=C0rky9%232016&grant_type=password&scope=sast_rest_api&client_id=resource_owner_client&client_secret=014DF517-39D1-4453-B7B3-9930C563627C&undefined="

headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Postman-Token': "f8b35e0c-2a12-42f9-94dc-654b3cb9014d"
    }

conn.request("POST", "cxrestapi,auth,identity,connect,token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
