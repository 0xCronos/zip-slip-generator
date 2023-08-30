# Zip Slip Generator

A simple script for compressing malicious files appending a custom parent directory for exploiting zip slip vulnerability.

<!-- USAGE EXAMPLES -->
## Usage
```
python3 main.py  --help
usage: main.py [-h] -F FILE -D DEPTH [-P PATH] -O OUTPUT

Compress the given file appending parent directory the amount of
times passed as argument with the -D flag.

optional arguments:
  -h, --help            show this help message and exit
  -F FILE, --file FILE  File to zip
  -D DEPTH, --depth DEPTH
                        Depth of the parent directory
  -P PATH, --path PATH  Path to append after parent directory
  -O OUTPUT, --output OUTPUT
                        The filename of the zip file
```
Note: Also you can use runner.sh!
