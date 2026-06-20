import time
import requests

# Placeholder endpoint - replace with your actual environment variable or target configuration
DATABASE_URL = "https://your-project-default-rtdb.firebaseio.com/chats.json"

def send_message(message_text):
    """Encodes a payload and sends an HTTP POST request."""
    payload = {
        "username": "FORB1D🔥",
        "displayName": "SYSTEM_OVERRIDE",
        "message": message_text,
        "jobIdLocation": "External_Server",
        "timestamp": int(time.time())
    }
    
    try:
        response = requests.post(DATABASE_URL, json=payload, timeout=10)
        
        if response.status_code == 200:
            print("🔥 Message successfully posted!")
        else:
            print(f"❌ Failed to send. Status Code: {response.status_code}")
            print(f"Server Response: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network connection error: {e}")

def read_messages():
    """Retrieves data using an HTTP GET request."""
    try:
        response = requests.get(DATABASE_URL, timeout=10)
        if response.status_code == 200 and response.text != "null":
            data = response.json()
            print("📡 Current Data standard output:", data)
        else:
            print(f"❌ Failed to read data. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Network connection error: {e}")

# --- Execution Flow ---
if __name__ == "__main__":
    output_text = "FORB1D RUNS THIS CHAT NOW 👽✌️"
    
    print("🚀 Starting Python execution loop...")
    
    # Infinite loop logic
    while True:
        send_message(output_text)
        
        # A delay is essential to prevent local resource starvation 
        # and respect remote server rate limits.
        time.sleep(2.0)