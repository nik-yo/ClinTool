# CLInt (CLI) Tool

A simple cli commands to assist with development process.

## Install
1. Clone this repo
2. cd /path/to/app
3. Run: python -m build
4. Install pipx: pip install --user pipx
5. Run: pipx ensurepath
6. Build: python -m build
7. Install: pipx install /dist/clintool-0.0.1.tar.gz
    - Dev install: pip install --editable .

## Examples

### Network call
clint http get <url> \
clint http get example.com \
clint http get http://example.com

clint http post example.com --data '{"test":"data"}'

clint http put example.com --data <data>

clint http delete example.com

clint http head example.com

clint http options example.com

clint http patch example.com

#### HTTPS
clint https <http_verb> <url>
clint https get example.com

### Generate UUID
clint uuid gen \
clint uuid gen --version <version> # Supported version values: 1, 3, 4, 5. Default: 4 \
clint uuid gen --version 5