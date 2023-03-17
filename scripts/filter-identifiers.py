#!/usr/bin/env python3

import fileinput

def main() -> None:
    for line in fileinput.input():
        line = line.replace('$', '$#')
        print(line.rstrip())

if __name__ == '__main__':
    main()
