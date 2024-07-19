import requests

def get_hubspot_data(access_token, endpoint): # function with 2 parameters
    url = f'https://api.hubapi.com{endpoint}'

    #created a Dictionary 
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code}, {response.text}")

access_token =  'pat-na1-6e06257c-648e-49ef-b470-cb62905986da'
endpoint = '/crm/v3/objects/contacts'
data = get_hubspot_data(access_token, endpoint)

# To print the fetched data
print(data)
