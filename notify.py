
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

def send_notification(msg):
    client = Client(os.getenv("ACebe64aa9ba38247039f20f8e8cce282f"), os.getenv("978e05181eb2509d8f900048c2369cab"))
    message = client.messages.create(
        body=msg,
        from_=os.getenv("TWILIO_WHATSAPP_FROM"),
        to=os.getenv("TWILIO_WHATSAPP_TO")
    )
    print(f"Zpráva odeslána: {message.sid}")
