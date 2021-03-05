#!/usr/bin/env python3
import sys
from pymugi import Mugi

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print("Missing Key and IV")
        sys.exit()
    key = bytes.fromhex(args[0])
    iv = bytes.fromhex(args[1])
    mugi = Mugi(key, iv)
    with sys.stdin.buffer as f:
        while True:
            chunk = f.read(8)
            if not chunk:
                break
            sys.stdout.buffer.write(mugi.crypt(chunk))

if __name__ == '__main__':
    main()
