import requests


response = requests.post('http://ccid-eddieantonio.rhcloud.com/toll')
print response.status_code

