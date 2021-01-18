import requests

for api_key in range(1, 100, 2):
    html = requests.get(f'http://10.10.213.94:8000/api/{api_key}')

    print(html.text)