# Pelcro & Zendesk API Authentication

## Overview
This Flask-based project uses both **Pelcro** and **Zendesk** APIs. The application includes endpoints to:
- Check a Zendesk support ticket's details
- Verify authentication with Pelcro API

## Installation
### Prerequisites
Ensure you have **Python 3** installed on your system.

### 1. Clone the Repository
```bash
 git clone https://github.com/your-username/your-repo-name.git
 cd your-repo-name
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate on macOS/Linux
venv\Scripts\activate  # Activate on Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add the following:
```ini
ZENDESK_SUBDOMAIN=your_zendesk_subdomain
ZENDESK_API_TOKEN=your_zendesk_api_token
ZENDESK_EMAIL=your_email
PELCRO_SITE_ID=your_pelcro_site_id
PELCRO_API_KEY=your_pelcro_api_key
```

### 5. Run the Application
```bash
python app.py
```

The Flask server will start, and you can access it at `http://127.0.0.1:5000/`.

## API Endpoints
### 1. Check Zendesk Ticket
**GET `/`**

**Response:**
```json
{
  "id": 2,
  "subject": "Ticket Subject",
  "status": "open",
  "priority": "high",
  "description": "Detailed ticket description."
}
```

### 2. Verify Pelcro Authentication
**GET `/pelcro_auth`**

**Response (Successful Authentication):**
```json
{
  "message": "Authentication successful!"
}
```

**Response (Failed Authentication):**
```json
{
  "error": "Authentication failed. Status code: 401",
  "details": "Invalid API Key"
}
```

## Security Best Practices
- **DO NOT** push `.env` files to GitHub.
- Add `.env` to your `.gitignore` file:
  ```bash
  echo .env >> .gitignore
  ```
- Share an `.env.example` file (without secrets) for reference.

## About
- Securely fetch Zendesk ticket details.
- Authenticate and interact with the Pelcro API.
- Uses **Flask** as the backend framework.
- Hides sensitive credentials using environment variables.

## Technologies Used
- **Python 3**
- **Flask**
- **Requests** (for API calls)
- **Python-dotenv** (for managing environment variables)

## Author
**Sara Habib**  
📧 [sara.habib48@gmail.com](mailto:sara.habib48@gmail.com)

