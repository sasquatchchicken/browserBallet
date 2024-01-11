import uuid
import ipaddress
import random

def generate_browser_id_with_ipv4():
    # Generate a random UUID (Universally Unique Identifier)
    browser_id = str(uuid.uuid4())

    # Generate a random IPv4 address
    ipv4_address = str(ipaddress.IPv4Address(random.randint(0, 2**32 - 1)))

    # Return the combination of UUID and IPv4 address
    #return browser_id, ipv4_address
    return f"{browser_id}_{ipv4_address}"
# Example usage
random_browser_id_ipv4_address = generate_browser_id_with_ipv4()
# Now you can use the generated IPv4 address in your code
print("Generated IPv4 Address:", random_browser_id_ipv4_address)

# Example usage
random_browser_id_with_ipv4 = generate_browser_id_with_ipv4()

# You can also extract the ipv4 part if needed
ipv4_part = random_browser_id_with_ipv4.split('_')[1]
print("Extracted IPV4:", ipv4_part)

# Example usage
random_browser_id_with_ipv4 = generate_browser_id_with_ipv4()

# You can also extract the UUID part if needed
uuid_part = random_browser_id_with_ipv4.split('_')[0]
print("Extracted UUID:", uuid_part)
