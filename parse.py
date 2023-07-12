import json
import datetime
import os

# Load JSON file
with open('data/conversations.json', 'r') as f:
    data = json.load(f)

# Check if the 'chats' subdirectory exists, if not create it
if not os.path.exists('chats'):
    os.makedirs('chats')

# Process each mapping
for entry in data:
    timestamp_seconds = entry['create_time']

    # Format timestamp as YYYY-MM-DD
    timestamp = datetime.datetime.fromtimestamp(timestamp_seconds).strftime('%Y-%m-%d')

    # replace non-word characters with an underscore
    title = re.sub('\W+', '_', entry['title'])

    # Create file name
    file_name = f'chats/{timestamp}_{title}.txt'

    # Write each mapping to a separate file
    with open(file_name, 'w') as f:
        for mapping in entry['mapping']:
            message = entry['mapping'][mapping]['message']

            # Check if message is not None
            if message is not None:
                # Check if author is not None and get the role
                if message['author'] is not None:
                    role = message['author']['role']
                    f.write(f'#-# {role}\n')

                # Check if content is not None and get the parts
                if message['content'] is not None:
                    parts = message['content']['parts']
                    for part in parts:
                        # Replace \n with actual new line
                        part = part.replace('\\n', '\n')
                        f.write(f'{part}\n')

            # Separate mappings with a couple of new lines
            f.write('\n')
    os.utime(file_name, (timestamp_seconds, timestamp_seconds))

