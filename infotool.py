import sys
import socket
import requests
import json

# Check if a website URL was provided
if len(sys.argv) != 2:
    print("Usage: python infotool.py <websiteurl>")
    sys.exit(1)

# Get website URL from command-line argument
website_url = sys.argv[1]

try:
    # Get IP address of the website
    ip_address = socket.gethostbyname(website_url)
    print(f"IP Address: {ip_address}")
    
    # Fetch location info from ipinfo.io
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Pretty print JSON response
        print(json.dumps(data, indent=4))
    else:
        print("Failed to retrieve information. Please check the IP address.")
        
except socket.gaierror:
    print("Invalid website URL. Please provide a valid one.")
except requests.RequestException as e:
    print(f"Request failed: {e}")
