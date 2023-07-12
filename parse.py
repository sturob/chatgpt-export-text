import json
import datetime
import os
import re


with open('json-data/conversations.json', 'r') as f:
    data = json.load(f)

if not os.path.exists('chats'):
    os.makedirs('chats')

for chat in data:
    timestamp_seconds = chat['create_time']

    # timestamp will be YYYY-MM-DD
    timestamp = datetime.datetime.fromtimestamp(timestamp_seconds).strftime('%Y-%m-%d')

    # replace non-word characters with underscores
    title = re.sub('\W+', '_', chat['title'])

    file_name = f'chats/{timestamp}_{title}.txt'

    with open(file_name, 'w') as f:
        for mapping in chat['mapping']:
            message = chat['mapping'][mapping]['message']

            # Check if message is not None
            if message is not None:
                # Check if author is not None and get the role
                if message['author'] is not None:
                    role = message['author']['role']
                    f.write(f'# {role}:\n')

                # Check if content is not None and get the parts
                if message['content'] is not None and 'parts' in message['content']:
                    parts = message['content']['parts']
                    for part in parts:
                        # Replace \n with actual new line
                        part = part.replace('\\n', '\n')
                        f.write(f'{part}\n')

            # Separate mappings with a couple of new lines
            f.write('\n')
    os.utime(file_name, (timestamp_seconds, timestamp_seconds))

