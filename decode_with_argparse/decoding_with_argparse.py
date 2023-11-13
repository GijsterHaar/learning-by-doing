import argparse
from urllib.parse import unquote, quote
from base64 import urlsafe_b64decode

def main():
    actions = {'from_percent': decode_string_percent, 'to_percent': encode_string_percent, 'from_base64': decode_from_base64, 'from_jwt': decode_from_jwt}
    arguments = get_arguments()
    endvalue = get_endvalue(actions, arguments.action, arguments.string, arguments.index)
    print(endvalue)

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['from_percent', 'to_percent', 'from_base64', 'from_jwt'],
                        help="choose your option, decode or encode string with percent, decode base64 or jwt")
    parser.add_argument('string', help="the string you want to decode/encode")
    parser.add_argument('index', nargs='?', type=int, default=1 ,choices=[0],
                        help="choose 0 for index 0, or don't and get default index 1")
    return parser.parse_args()

def get_endvalue(actions, action, string, index):
    return actions[action](string, index)

def decode_string_percent(string, index):
    return unquote(string)

def encode_string_percent(string, index):
    return quote(string)

def decode_from_base64(string, index):
    padded_payload = string + ('=' * (-len(string) % 4))
    return urlsafe_b64decode(padded_payload).decode()

def decode_from_jwt(token, index):
    payload = token.split('.')[index]
    return decode_from_base64(payload, index)

if __name__ == '__main__':
    main()

# actions you can perform. to_percent takes a "string" because it contains spaces, the rest doesn't:
# from_percent: This%20Gijzemans%20dude%20got%20this%20working. 
# to_percent: "This Gijzemans dude got this working."
# from_base64: TXkgbmFtZSBpcyBHaWp6ZW1hbnMgYW5kIEkgZ290IHRoaXMgZGVjb2RlciB3b3JraW5n
# from_jwt: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnZW5kZXIiOiJNYW4iLCJuYW1lIjoiR2lqemVtYW5zIiwic3RhdGUiOiJDaGlsbGF4In0.ix1UBqI8U-jkKy1xdByNtYFlDyMeCti0Tv5nlbvZxpI