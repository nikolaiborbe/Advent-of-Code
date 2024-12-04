import requests
import sys
import os
from dotenv import load_dotenv
load_dotenv()

def fetch_input(day):
    session_cookie = os.getenv("SESSION_COOKIE")
    if not day.isdigit() or int(day) <= 0:
        print("Error: Day must be a positive integer.")
        return

    url = f"https://adventofcode.com/2024/day/{day}/input"

    headers = {"Cookie": f"session={session_cookie}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        with open("input", "w") as file:
            file.write(response.text)
            print(response.text)
        
    else:
        print(f"Failed to fetch data. HTTP status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <day>")
    else:
        day = sys.argv[1]
        fetch_input(day)