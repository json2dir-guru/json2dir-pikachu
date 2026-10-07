# json2dir-pikachu

json2dir in Pikalang (Pikachu): `json2dir.pokeball` is the Brainfuck program `json2dir.bf` (from json2dir-brainfuck) transliterated by `tools/bf2pika.py`; it validates the JSON and prints a shell script, which the POSIX sh launcher `json2dir` runs (input framed as decimal bytes via `od`).

    JSON2DIR_PIKALANG=/path/to/pikalang ./json2dir < tree.json
