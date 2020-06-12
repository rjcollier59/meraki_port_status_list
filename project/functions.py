import requests

base_url = "https://n270.meraki.com/api/v0"

api_key = "d6d09bf4a98906445a42ed1433c28844c708a3f0"

def get_orgs():
    global base_url
    global api_key

    url = base_url + "/organizations"
    payload = {}
    headers = {
    'X-Cisco-Meraki-API-Key': api_key
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    return response.json()

def get_inventory(org_id):

    global base_url
    global api_key

    url = base_url + "/organizations/" + org_id + "/inventory"

    payload = {}
    headers = {
        'X-Cisco-Meraki-API-Key': api_key
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    return response.json()

def get_switch_ports(serial):
    global base_url
    global api_key

    url = base_url + "/devices/" + serial + "/switchPortStatuses"
   
    payload = {}
   
    headers = {
     'X-Cisco-Meraki-API-Key': api_key
     }
    
    
    response = requests.request("GET", url, headers=headers, data = payload)

    if response.status_code == 200:
        return response.json()
    else:
        print ('Error with device serial: ',serial)
        return ' '

def get_networks(org_id):
    global api_key
    global base_url

    url = base_url + "/organizations/" + org_id + "/networks"

    payload = {}
    headers = {
    'X-Cisco-Meraki-API-Key': api_key
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    return response.json()

