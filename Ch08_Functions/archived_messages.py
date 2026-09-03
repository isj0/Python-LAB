def send_messages(messages, sent_messages):
    """Print each message and move the message
        to sent_messages."""

    while messages:
        current_message = messages.pop()
        print(f"\nSending new message: {current_message}")
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    """Show all the sent messages."""
    for msg in sent_messages:
        print(msg)

# List of messages
messages = ['hi', 'hola', 'bonjour', 'ciao', 'konichiwa', 'namaste', 'marhaba']
sent_msgs = []

send_messages(messages[:], sent_msgs)
print()
show_sent_messages(sent_msgs)
print()
show_sent_messages(messages)

