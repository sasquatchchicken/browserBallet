import uuid
import requests
import ipaddress
import random

def generate_random_ip():
    # Generate a random IPv4 address
    return str(ipaddress.IPv4Address(int(uuid.uuid4())))
   #return str(ipaddress.IPv4Address(random.randint(0, 2**32 - 1)))

def associate_ip_with_geolocation(ip_address):
    # Assume there's a geolocation API that returns location based on IP
    geolocation_api_url = "http://ip-api.com/batch"
    response = requests.get(geolocation_api_url, params={"ip": ip_address}).json()

    # Extract geolocation information from the API response (this depends on the API)
    geolocation_info = response.json()

    # Return the geolocation information
    return geolocation_info

def generate_browser_id_with_geolocation():
    # Generate a random IPv4 address
    random_ip = generate_random_ip()

    # Associate the IP address with geolocation
    geolocation_info = associate_ip_with_geolocation(random_ip)

    # Generate a random UUID (Universally Unique Identifier)
    browser_id = str(uuid.uuid4())

    # Attach geolocation information to the browser ID
    browser_id_with_geo = {"browser_id": browser_id, "geolocation": geolocation_info}

    # Return the browser ID with geolocation
    print(browser_id_with_geo)

# Example usage
#random_browser_id_with_geo = generate_browser_id_with_geolocation()
#print("Random Browser ID with Geolocation:", random_browser_id_with_geo)
