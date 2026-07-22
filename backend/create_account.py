import os
import sys
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

if not url or not key:
    print("Error: Missing SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY")
    sys.exit(1)

supabase: Client = create_client(url, key)

def create_account(email, password):
    print(f"Attempting to create account for {email} bypassing rate limits...")
    try:
        response = supabase.auth.admin.create_user(
            {
                "email": email,
                "password": password,
                "email_confirm": True
            }
        )
        print(f"Success! Account created with ID: {response.user.id}")
        print("You can now log in directly from the frontend.")
    except Exception as e:
        print(f"Error creating account: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_account.py <email> <password>")
        sys.exit(1)
        
    create_account(sys.argv[1], sys.argv[2])
