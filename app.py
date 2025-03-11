from flask import Flask, request, jsonify
import requests
import re
import base64
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()

app = Flask(__name__)

# Fetch credentials from environment variables
ZENDESK_SUBDOMAIN = os.getenv("ZENDESK_SUBDOMAIN")
ZENDESK_API_TOKEN = os.getenv("ZENDESK_API_TOKEN")
ZENDESK_EMAIL = os.getenv("ZENDESK_EMAIL")

PELCRO_SITE_ID = os.getenv("PELCRO_SITE_ID")
PELCRO_API_KEY = os.getenv("PELCRO_API_KEY")


@app.route("/")
def check_ticket_2():
    ticket_id = 2
    # https://pelcrointerview.zendesk.com/api/v2/tickets/2.json
    url = f"https://{ZENDESK_SUBDOMAIN}.zendesk.com/api/v2/tickets/{ticket_id}.json"

    '''https://developer.zendesk.com/api-reference/introduction/security-and-auth/#oauth-access-token'''
    # Format the credentials as: {email_address}/token:{api_token}
    credentials = f"{ZENDESK_EMAIL}/token:{ZENDESK_API_TOKEN}"

    # Encode credentials in Base64
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        ticket_data = response.json().get("ticket", {})
        return {
            "id": ticket_data.get("id"),
            "subject": ticket_data.get("subject"),
            "status": ticket_data.get("status"),
            "priority": ticket_data.get("priority"),
            "description": ticket_data.get("description")
        }
    else:
        return {"error": f"Failed to fetch ticket. Status code: {response.status_code}", "details": response.text}


def check_pelcro_auth():
    url = f"https://www.pelcro.com/api/v1/core/addresses?limit=100&site_id={PELCRO_SITE_ID}"
    headers = {
        "Authorization": f"Bearer {PELCRO_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return {"message": "Authentication successful!"}
    else:
        return {"error": f"Authentication failed. Status code: {response.status_code}", "details": response.text}


@app.route("/")
def check_ticket():
    return jsonify({"message": check_ticket_2()})


@app.route("/pelcro_auth")
def check_auth():
    return jsonify(check_pelcro_auth())


if __name__ == "__main__":
    app.run(debug=False)
