import json
path = r'C:\Users\ASUS\.gemini\antigravity-ide\brain\98575fe1-7bfb-47de-ab78-78e4008d4e1d\.system_generated\logs\transcript_full.jsonl'
with open(path, 'r', encoding='utf-8', errors='ignore') as file:
    for line in file:
        try:
            d = json.loads(line)
            if 'tool_calls' in d:
                for call in d['tool_calls']:
                    if 'profile/page.tsx' in str(call):
                        print(f"Step {d.get('step_index')}: {call['name']}")
        except Exception:
            pass
