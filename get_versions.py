import json
path = r'C:\Users\ASUS\.gemini\antigravity-ide\brain\98575fe1-7bfb-47de-ab78-78e4008d4e1d\.system_generated\logs\transcript_full.jsonl'
with open(path, 'r', encoding='utf-8', errors='ignore') as file:
    for line in file:
        try:
            d = json.loads(line)
            if 'tool_calls' in d:
                for call in d['tool_calls']:
                    args = call.get('arguments', {})
                    if 'profile/page.tsx' in str(call):
                        if d.get('step_index') == 1074:
                            with open('profile_1074.tsx', 'w', encoding='utf-8') as out:
                                out.write(args.get('CodeContent', ''))
                        if d.get('step_index') == 356:
                            with open('profile_356.tsx', 'w', encoding='utf-8') as out:
                                out.write(args.get('ReplacementContent', ''))
        except Exception:
            pass
