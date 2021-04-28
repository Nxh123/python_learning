messages = [
    'Hello',
    'World',
    'I love Python',
]
send_message = []


def show_messages(list):
    for message in list:
        print(message)


def send_messages(messages, send_messages):
    while messages:
        message = messages.pop()
        print(message)
        send_messages.append(message)


show_messages(messages)
send_messages(messages[:], send_message)
print(messages)
print(send_message)
