import os
from google.oauth2 import service_account
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

UPLOAD_FOLDER = 'temp'
SCOPES = ['https://www.googleapis.com/auth/drive']
PARENT_FOLDER_ID = '1dumOuww0erGVR0ec1au_o7ehZA3Kulg5'

def authenticate():
    credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    if not credentials_path:
        raise ValueError("GOOGLE_APPLICATION_CREDENTIALS environment variable is not set")

    # Load credentials from the specified path
    creds = service_account.Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
    return creds
    