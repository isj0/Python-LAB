def show_messages(messages):
    """Prints message in the list"""
    for msg in messages:
        print(f"{msg.title()} !")

messages = ['hi', 'hola', 'bonjour', 'ciao', 'konichiwa']

show_messages(messages)