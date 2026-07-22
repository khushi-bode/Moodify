import os
import random
from datetime import datetime, timedelta
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

# Using the Service Role Key to bypass RLS and email confirmations
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

if not url or not key:
    print("Error: SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY must be set in .env")
    exit(1)

supabase: Client = create_client(url, key)

DEMO_EMAIL = "demo@moodify.app"
DEMO_PASSWORD = "password123"

def main():
    print(f"--- Seeding Demo Data for {DEMO_EMAIL} ---")
    
    # 1. Delete existing demo user if exists
    try:
        users = supabase.auth.admin.list_users()
        for u in users:
            if u.email == DEMO_EMAIL:
                print(f"Deleting existing demo user {u.id}...")
                supabase.auth.admin.delete_user(u.id)
    except Exception as e:
        print(f"Note: Could not check/delete existing users: {e}")

    # 2. Create the demo user with auto-confirmed email
    print("Creating user account...")
    try:
        response = supabase.auth.admin.create_user(
            {
                "email": DEMO_EMAIL,
                "password": DEMO_PASSWORD,
                "email_confirm": True
            }
        )
        user = response.user
        user_id = user.id
        print(f"Created user {user_id}")
    except Exception as e:
        print(f"Failed to create user: {e}")
        return

    # Helper function to generate timestamps
    now = datetime.utcnow()
    
    # 3. Seed Mood History (14-21 days of varied records)
    print("Seeding mood history...")
    num_days = random.randint(14, 21)
    emotions = ["Happy", "Neutral", "Surprise", "Sad", "Fear", "Angry", "Disgust"]
    insights = [
        "Your mood seems quite positive today, keep it up!",
        "A balanced day with stable energy levels.",
        "You seem a bit surprised by events today.",
        "It's okay to feel down sometimes. Take a moment to breathe.",
        "Feeling a bit anxious? Try a short mindfulness exercise.",
        "Some frustration is evident. A short walk might help.",
        "Not the best day, but tomorrow is a fresh start."
    ]
    
    history_ids = []
    
    for i in range(num_days, -1, -1):
        # 1-3 scans per day
        scans_today = random.randint(1, 3)
        
        for j in range(scans_today):
            # Distribute times: Morning (8), Afternoon (14), Evening (20)
            hour_offset = random.choice([8, 14, 20])
            minute_offset = random.randint(0, 59)
            record_time = now - timedelta(days=i)
            record_time = record_time.replace(hour=hour_offset, minute=minute_offset)
            
            # Create a slight trend (more happy towards recent days)
            if i < 7:
                weights = [40, 30, 10, 5, 5, 5, 5]
            else:
                weights = [10, 20, 10, 20, 20, 10, 10]
                
            emotion = random.choices(emotions, weights=weights)[0]
            confidence = random.randint(75, 99)
            
            # Simple mood score map
            score_map = {"Happy": 90, "Surprise": 70, "Neutral": 50, "Sad": 30, "Fear": 20, "Angry": 10, "Disgust": 10}
            mood_score = score_map[emotion] + random.randint(-5, 5)
            
            insight = insights[emotions.index(emotion)]
            
            result = supabase.table("mood_history").insert({
                "user_id": user_id,
                "emotion": emotion,
                "confidence": confidence,
                "mood_score": mood_score,
                "ai_insight": insight,
                "created_at": record_time.isoformat()
            }).execute()
            
            history_ids.append(result.data[0]['id'])
            
    print(f"Inserted {len(history_ids)} mood history records.")

    # 4. Seed Tasks
    print("Seeding tasks...")
    # Insert some base suggestions if the table is empty
    suggestions_res = supabase.table("suggestions").select("*").execute()
    suggestions = suggestions_res.data
    
    if not suggestions:
        print("Suggestions table empty, skipping task relations to suggestions...")
    
    tasks = [
        ("Take a 10-minute walk outside", True),
        ("Drink 2 glasses of water", True),
        ("Write down 3 things you are grateful for", True),
        ("Do a 5-minute breathing exercise", False),
        ("Listen to an upbeat playlist", False),
        ("Call a friend or family member", False)
    ]
    
    for title, completed in tasks:
        task_data = {
            "user_id": user_id,
            "title": title,
            "completed": completed,
            "created_at": (now - timedelta(days=random.randint(0, 5))).isoformat()
        }
        
        # Link to a random mood history item
        if history_ids:
            task_data["mood_history_id"] = random.choice(history_ids)
            
        supabase.table("tasks").insert(task_data).execute()
        
    print(f"Inserted {len(tasks)} tasks.")

    # 5. Seed Chat Messages
    print("Seeding chat conversation...")
    messages = [
        {"role": "user", "content": "I've been feeling a bit overwhelmed with work lately.", "time_offset": 60},
        {"role": "ai", "content": "I'm sorry to hear that you're feeling overwhelmed. Work stress can definitely pile up. What specifically has been the most stressful part of your week?", "time_offset": 59},
        {"role": "user", "content": "Just too many deadlines and not enough time to rest.", "time_offset": 55},
        {"role": "ai", "content": "That sounds exhausting. When we have back-to-back deadlines, our brains stay in a constant 'fight or flight' state. Have you been able to take any short breaks at all during your day?", "time_offset": 54}
    ]
    
    for msg in messages:
        msg_time = now - timedelta(minutes=msg["time_offset"])
        supabase.table("chat_messages").insert({
            "user_id": user_id,
            "role": msg["role"],
            "content": msg["content"],
            "created_at": msg_time.isoformat()
        }).execute()
        
    print(f"Inserted {len(messages)} chat messages.")

    # 6. Seed Reports
    print("Seeding weekly report...")
    report_content = """### Weekly Mood Summary
Your mood this week has shown a positive upward trend! 
- **Dominant Emotion:** Happy (60% of scans)
- **Average Mood Score:** 72/100

**Insights:**
You seem to have lower energy on Tuesday and Wednesday mornings, but your mood consistently improves by the afternoon. 

**Recommendation for next week:**
Keep up the daily walks—they strongly correlate with your highest mood scores! Try to maintain a consistent sleep schedule to help with those groggy mornings."""

    supabase.table("reports").insert({
        "user_id": user_id,
        "period": "weekly",
        "summary": report_content,
        "created_at": (now - timedelta(days=1)).isoformat()
    }).execute()
    
    print("Inserted 1 weekly report.")

    print(f"\n--- SUCCESS! ---")
    print(f"Demo Account Created:")
    print(f"Email: {DEMO_EMAIL}")
    print(f"Password: {DEMO_PASSWORD}")
    print(f"You can now log in directly at http://localhost:3000/login without needing email verification.")

if __name__ == "__main__":
    main()
