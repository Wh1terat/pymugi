#!/usr/bin/env python3
import sys
from pymugi import Mugi

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print("Missing Key and IV")
        sys.exit()
    k = bytes.fromhex(args[0])
    i = bytes.fromhex(args[1])
    m = Mugi(k, i)
    p = m.prng()
    with sys.stdin.buffer as f:
        c = f.read(8)
        k = next(p).to_bytes(8,'big')
        out = bytes(a ^ b for (a, b) in zip(c, k))
        sys.stdout.buffer.write(out)

if __name__ == '__main__':
    main()
