import requests

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "4ac6c9bdb3mshb4e0b566f9a1d29p1c8350jsn4412c9dd2197",
	"X-RapidAPI-Host": "chatgpt-best-price.p.rapidapi.com"
}

url = "https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions"

payload = {
	"model": "gpt-3.5-turbo",
	"messages": [
		{
			"role": "user",
			"content": "Hello, how are you?"
		}
	]
}

response = requests.post(url, json=payload, headers=headers, timeout=10)

print(f"Status code: {response.status_code}")
print(f"Status response: {response.json()}")
print(f"Response from GPT: {response.json()["choices"][0]["message"]["content"]}")