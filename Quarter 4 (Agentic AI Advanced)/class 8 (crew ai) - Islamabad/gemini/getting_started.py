import requests
import json

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=AIzaSyCgJIzDkDn3s-63fFGewoAn4KJTKz69NB8"
headers = {
    'Content-Type': 'application/json'
}
data = {
    "contents": [{
        "parts": [{"text": "Explain how AI works"}]
    }]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())