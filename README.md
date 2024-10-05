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
clint http get <span style="color: red;">url</span>

examples: 
- clint http get example.com
- clint http get http://example.com

clint http post example.com --data '{"test":"data"}'

clint http put example.com --data <data>

clint http delete example.com

clint http head example.com

clint http options example.com

clint http patch example.com

#### HTTPS
clint https <span style="color: red;">http_verb</span> <span style="color: red;">url</span>

eg: clint https get example.com

#### HTTP server
clint http serve
eg: clint http serve --port <span style="color: red;">port</span> <span style="color: green;"># Port default: 8000</span>

### Generate UUID
clint uuid gen \

examples: 
- clint uuid gen --version <span style="color: red;">version</span> <span style="color: green;"># Supported version values: 1, 3, 4, 5. Default: 4</span>
- clint uuid gen --version 5

### Lettercase
clint lowercase <span style="color: red;">text</span> \
clint uppercase <span style="color: red;">text</span>