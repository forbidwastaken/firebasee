import time
import requests
import threading
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

# --- FAKE WEB SERVER TO KEEP RENDER HAPPY ---
class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        # FIXED LINE: Encoding the emoji properly so Python doesn't crash
        self.wfile.write("FORB1D Bot is running online! 👽".encode('utf-8'))

def keep_alive():
    # Render assigns a dynamic port, we must use it
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), DummyHandler)
    print(f"✅ Web port {port} opened! Render is happy.")
    server.serve_forever()


# --- YOUR FIREBASE CODE ---
DATABASE_URL = "https://spammerachatv4-default-rtdb.asia-southeast1.firebasedatabase.app/global_chats.json"

def send_message(message_text):
    payload = {
        "username": " 🔱 FORB1D ON TOP🔥",
        "displayName": "FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥FORB1D🔥",
        "message": message_text,
        "jobIdLocation": "Render_Cloud",
        "timestamp": int(time.time())
    }
    
    try:
        response = requests.post(DATABASE_URL, json=payload, timeout=10)
        if response.status_code == 200:
            print("🔥 Message successfully posted!")
        else:
            print(f"❌ Failed to send. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Network connection error: {e}")


# --- EXECUTION FLOW ---
if __name__ == "__main__":
    # 1. Start the fake web server in the background so Render doesn't shut us down
    threading.Thread(target=keep_alive, daemon=True).start()
    
    output_text = "🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥🔱 FORB1D ON TOP🔥"
    print("🚀 Starting execution loop...")
    
    # 2. Run your infinite loop
    while True:
        send_message(output_text)
        time.sleep(0.8)
