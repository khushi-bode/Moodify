import os
import json

brain_dir = r'C:\Users\ASUS\.gemini\antigravity-ide\brain'
counter = 0

for root, _, files in os.walk(brain_dir):
    for f in files:
        if f.endswith('transcript_full.jsonl'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                for line in file:
                    if 'profile/page.tsx' in line:
                        try:
                            data = json.loads(line)
                            for call in data.get('tool_calls', []):
                                if 'profile/page.tsx' in str(call):
                                    content = call.get('arguments', {}).get('CodeContent')
                                    if content:
                                        counter += 1
                                        with open(f'profile_v{counter}.tsx', 'w', encoding='utf-8') as out:
                                            out.write(content)
                                        print(f"Saved profile_v{counter}.tsx from CodeContent")
                                    
                                    content_rep = call.get('arguments', {}).get('ReplacementContent')
                                    if content_rep:
                                        counter += 1
                                        with open(f'profile_v{counter}_rep.tsx', 'w', encoding='utf-8') as out:
                                            out.write(content_rep)
                                        print(f"Saved profile_v{counter}_rep.tsx from ReplacementContent")
                        except Exception as e:
                            pass
