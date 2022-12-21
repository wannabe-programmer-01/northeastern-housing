import json
import re


def extract_data_from_message(message):
    # Extract the date and time from the beginning of the message (assuming it's in the format "DD/MM/YY HH:MM:SS")
    date_time_match = re.match(r'(\d{2}/\d{2}/\d{2}, \d{2}:\d{2}) - (.+): (.+)', message)
    date_time = date_time_match.group(1) if date_time_match else None
    # Extract the sender and message text from the rest of the message
    sender_match = re.search(r'[\+]?[\(]?[\d]{1,3}[\)]?[\s|\-|\.]?[\d]{3}[\s|\-|\.]?[\d]{3}[\s|\-|\.]?[\d]{1}', message)
    sender = sender_match.group() if sender_match else None
    message_text = message[sender_match.end():] if sender_match else message
    # Split the date and time into separate date and time values
    date, time = date_time.split(',') if date_time else (None, None)
    return date, time, sender, message_text


def split_by_messages(chat_content):
    # Split the chat content into messages using the timestamp as a delimiter
    # (assuming the timestamp is in the format "DD/MM/YYYY HH:MM:SS")
    return re.split(r"(^\d{2}/\d{2}/\d{2}, \d{2}:\d{2})", chat_content, flags=re.MULTILINE)


# Extract the relevant data from the messages
# (You'll need to figure out what data you want to extract and how to extract it)
# For example, you might want to extract the date, time, sender, and message for each message

chat_content_file = r"C:\Users\kashi\Downloads\WhatsApp Chat with NEU MEM’22.txt"

# Open the exported chat file
with open(chat_content_file, 'r',  encoding='utf-8') as f:
    chat_content = f.read()

# Split the chat content into messages
messages = split_by_messages(chat_content)
extracted_data = []
for message in messages:
    # Extract the date, time, sender, and message for each message
    date, time, sender, message_text = extract_data_from_message(message)
    extracted_data.append({'date': date, 'time': time, 'sender': sender, 'message': message_text})

with open('chat.json', 'w') as f:
    json.dump(extracted_data, f)
