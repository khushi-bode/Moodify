import json

path = r'C:\Users\ASUS\.gemini\antigravity-ide\brain\98575fe1-7bfb-47de-ab78-78e4008d4e1d\.system_generated\logs\transcript_full.jsonl'
with open(path, 'r', encoding='utf-8', errors='ignore') as file:
    for line in file:
        if 'ProfilePage' in line:
            with open('profile_lines.jsonl', 'a', encoding='utf-8') as out:
                out.write(line)
