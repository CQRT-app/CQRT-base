__author__ = "reza0310"

import globals


def echanger(client_socket, message):  # Code pour envoyer un msg
    message = message.encode('utf-8')
    message_header = f"{len(message):<{globals.HEADER_LENGTH}}".encode('utf-8')
    client_socket.send(message_header + message)
    message_header = client_socket.recv(globals.HEADER_LENGTH)
    if not len(message_header):
        print('Connection perdue.')
    message_length = int(message_header.decode('utf-8').strip())
    message = client_socket.recv(message_length).decode('utf-8')
    return message.replace("&apos;", "'").replace('&quot;', '"')