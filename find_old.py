import os
import json
brain_dir = r'C:\Users\ASUS\.gemini\antigravity-ide\brain'
for root, _, files in os.walk(brain_dir):
    for f in files:
        if f.endswith('transcript_full.jsonl'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                for line in file:
                    if 'profile/page.tsx' in line:
                        try:
                            d = json.loads(line)
                            for call in d.get('tool_calls', []):
                                args = call.get('arguments', {})
                                if 'TargetFile' in args and 'profile/page.tsx' in args['TargetFile']:
                                    print(f"FOUND in {path}: {call['name']}")
                                    if 'ReplacementChunks' in args:
                                        print('HAS CHUNKS')
                                    if 'ReplacementContent' in args:
                                        with open('recovered.tsx', 'w', encoding='utf-8') as out:
                                            out.write(args['ReplacementContent'])
                                    if 'CodeContent' in args:
                                        with open('recovered.tsx', 'w', encoding='utf-8') as out:
                                            out.write(args['CodeContent'])
                        except: pass
