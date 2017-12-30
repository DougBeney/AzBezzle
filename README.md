# Azbezzle
## Make sure Amazon links on a given URL contain your affiliate ID.
#### Works on Windows, Mac, and Linux


## Basic Usage:

Dependencies:

- Python3
- Virtualenv

**Installation:**

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
make
```

**Usage**:

After installing, you have an executable file in your `dist/` folder. You could execute it via the command line.

```
usage: azbezzle [-h] [--id ID] url

positional arguments:
  url         The URL you want to analyze.

optional arguments:
  -h, --help  show this help message and exit
  --id ID     Your Amazon Associate ID

```
