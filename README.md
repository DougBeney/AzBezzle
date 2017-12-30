# Azbezzle
## Make sure Amazon links on a given URL contain your affiliate ID.
#### Works on Windows, Mac, and Linux

## Usage:

```
usage: azbezzle [-h] [--id ID] url

positional arguments:
  url         The URL you want to analyze.

optional arguments:
  -h, --help  show this help message and exit
  --id ID     Your Amazon Associate ID

```

## Building:

Dependencies:

- Python3
- Virtualenv
- Make

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
make
```

## Installing (Windows):

Coming soon. (Maybe)

## Installing (Mac/Linux)

```bash
make install_unix
```

## Uninstalling (Mac/Linux)

```bash
make uninstall_unix
```

