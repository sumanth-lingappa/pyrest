import requests
import argparse



headers = {}
headers['Content-Type'] = 'application/json'



def do_get():
    ...


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("positional_arg", help="This is an int arg", type=int)
    parser.add_argument("-v", "--verbosity", help="Increase output verbosity", action="store_true")
    # parser.add_argument("-v", "--verbosity", help="Increase output verbosity", action="count", default=0)
    args = parser.parse_args()
