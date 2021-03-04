import socket
import argparse
import itertools
import string


parser = argparse.ArgumentParser()
parser.add_argument('ip_address')
parser.add_argument('port')

args = parser.parse_args()


class Kraken:
    _characters = tuple(string.ascii_lowercase)
    _numbers = tuple(string.digits)
    _all_values = tuple(itertools.chain(_characters, _numbers))
    _current_list = _all_values[:]
    _typical_passwords = []

    def __init__(self):
        self.address = (args.ip_address, int(args.port))

    def next_attempt(self):
        while True:
            for text in self._current_list:
                yield text
            self._current_list = [a + b for a, b in itertools.product(self._current_list[:], self._all_values)]

    def load_dict(self):
        with open('passwords.txt', 'r', encoding='utf-8') as passwords:
            for line in passwords.readlines():
                self._typical_passwords.append(line.strip())

    def next_dict_entry(self):
        for current_entry in self._typical_passwords:
            all_variations = map(''.join, itertools.product(*zip(current_entry.lower(), current_entry.upper())))
            for variation in all_variations:
                yield variation

    def bite(self, method):
        with socket.socket() as client_socket:
            client_socket.connect(self.address)

            if method == "brute":
                for word in self.next_attempt():
                    data = word.encode()
                    client_socket.send(data)
                    response = client_socket.recv(1024)
                    decoded_response = response.decode()

                    if decoded_response == "Wrong password!":
                        continue
                    elif decoded_response == "Connection success!":
                        print(word)
                        break
                    elif decoded_response == "Too many attempts":
                        break
            elif method == "dict":
                self.load_dict()
                for word in self.next_dict_entry():
                    data = word.encode()
                    client_socket.send(data)
                    response = client_socket.recv(1024)
                    decoded_response = response.decode()

                    if decoded_response == "Wrong password!":
                        continue
                    elif decoded_response == "Connection success!":
                        print(word)
                        break
                    elif decoded_response == "Too many attempts":
                        break


kraken = Kraken()
kraken.bite("dict")
