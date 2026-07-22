import json

with open('profile_lines.jsonl', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        try:
            d = json.loads(line)
            if 'tool_calls' in d:
                for call in d['tool_calls']:
                    args = call.get('arguments', {})
                    content = args.get('CodeContent') or args.get('ReplacementContent')
                    if content and 'export default function ProfilePage' in content:
                        with open(f'profile_extracted_{i}.tsx', 'w', encoding='utf-8') as out:
                            out.write(content)
                        print(f"Extracted to profile_extracted_{i}.tsx")
        except:
            pass
