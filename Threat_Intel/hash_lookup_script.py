# -----------------------------------------------------------------------------
# Script: VirusTotal Hash Lookup
# Author: By Gross
# Description: Uses VirusTotal API to fetch threat info on a given file hash.
# Certifications: ISC2 CC, SSCP (in progress)
# Education: MS in Information Systems (Expected March 2026)
# GitHub: github.com/sarcasticwitwizard
# LinkedIn: linkedin.com/in/philliplgross
# -----------------------------------------------------------------------------

import requests

API_KEY = "your_api_key_here"
file_hash = input("Enter hash to look up: ")

url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
headers = {"x-apikey": API_KEY}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")
