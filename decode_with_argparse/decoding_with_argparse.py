import argparse
from urllib.parse import unquote, quote
from base64 import urlsafe_b64decode

def main():
    
    parse_arguments = get_parse_arguments()
    endvalue = get_endvalue(parse_arguments)
    print(endvalue)


def get_parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('decode_encode', choices=['from_percent', 'to_percent', 'from_base64', 'from_jwt'],\
                        help="choose your option, decode or encode")
    parser.add_argument('string')
    return parser.parse_args()


def get_endvalue(parse_arguments):
    if parse_arguments.decode_encode == 'from_percent':
        endvalue = decode_text(parse_arguments.string)
    elif parse_arguments.decode_encode == 'to_percent':
        endvalue = encode_text(parse_arguments.string)
    elif parse_arguments.decode_encode == 'from_base64':
        endvalue = from_base64(parse_arguments.string)
    # elif parse_arguments.decode_encode == 'from_jwt':
    else:
        endvalue = from_jwt(parse_arguments.string)

    return endvalue
   

def decode_text(parse_arguments):
    return unquote(parse_arguments)


def encode_text(parse_arguments):
    return quote(parse_arguments)


def from_base64(parse_argument):
    padded_payload = parse_argument + ('=' * (-len(parse_argument) % 4))
    decoded= urlsafe_b64decode(padded_payload)
    return decoded.decode()


def from_jwt(token):
    payload = token.split('.')[1]
    padded_payload = payload + ('=' * (-len(payload) % 4))
    decoded= urlsafe_b64decode(padded_payload)
    return decoded.decode()

    
if __name__ == '__main__':
    main()

# actions you can perform. from_percent takes no string, the rest does:
# from_percent: This%20Gijzemans%20dude%20got%20this%20working. 
# to_percent: "This Gijzemans dude got this working."
# from_base64: "TXkgbmFtZSBpcyBHaWp6ZW1hbnMgYW5kIEkgZ290IHRoaXMgZGVjb2RlciB3b3JraW5n"
# from_jwt: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnZW5kZXIiOiJNYW4iLCJuYW1lIjoiR2lqemVtYW5zIiwic3RhdGUiOiJDaGlsbGF4In0.ix1UBqI8U-jkKy1xdByNtYFlDyMeCti0Tv5nlbvZxpI"