#!/usr/bin/env python3
"""Transliterate a Brainfuck program into Pikalang (stdlib only).

Usage: python3 tools/bf2pika.py json2dir.bf > json2dir.pokeball

Word table of Pikalang (esolangs.org, groteworld/pikalang, and the C interpreter
Amirreza-Ipchi-Haq/Pikalang used here): pipi > , pichu < , pi + , ka - ,
pikachu . , pikapi , , pika [ , chu ].  Non-command characters are dropped.
Words are separated by blanks; the file ends with a newline (the interpreter's
reader drops a last word that is directly followed by end of file).
"""
import sys

WORDS = {
    ">": "pipi",
    "<": "pichu",
    "+": "pi",
    "-": "ka",
    ".": "pikachu",
    ",": "pikapi",
    "[": "pika",
    "]": "chu",
}
PER_LINE = 16


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: bf2pika.py PROGRAM.bf > PROGRAM.pokeball")
    with open(sys.argv[1], encoding="latin-1") as f:
        words = [WORDS[c] for c in f.read() if c in WORDS]
    out = sys.stdout
    for i in range(0, len(words), PER_LINE):
        out.write(" ".join(words[i:i + PER_LINE]) + "\n")


if __name__ == "__main__":
    main()
