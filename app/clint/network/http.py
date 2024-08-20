import click
import requests
import re
import json
import http.server
import socketserver

@click.group('http')
def http_():
  pass

@http_.command()
@click.argument('url')
def get(url):
  n_url = normalize_url(url)
  r = requests.get(n_url)    
  print(r.text)

@http_.command()
@click.argument('url')
@click.option('--data', default=None, metavar='', help='Payload for HTTP POST')
def post(url, data):
  n_url = normalize_url(url)
  if data is not None:
    try:
      json_data = json.loads(data)
      r = requests.post(n_url, data=json_data)
      print(r.text)
      return
    except:
      pass
  r = requests.post(n_url, data=data)
  print(r.text)

@http_.command()
@click.argument('url')
@click.option('--data', default=None, metavar='', help='Payload for HTTP PUT')
def put(url, data):
  n_url = normalize_url(url)
  if data is not None:
    try:
      json_data = json.loads(data)
      r = requests.put(n_url, data=json_data)
      print(r.text)
      return
    except:
      pass
  r = requests.put(n_url, data=data)
  print(r.text)

@http_.command()
@click.argument('url')
def delete(url):
  n_url = normalize_url(url)
  r = requests.delete(n_url)
  print(r.text)

@http_.command()
@click.argument('url')
def head(url):
  n_url = normalize_url(url)
  r = requests.head(n_url)
  print(r.text)

@http_.command()
@click.argument('url')
def options(url):
  n_url = normalize_url(url)
  r = requests.options(n_url)
  print(r.text)

@http_.command()
@click.argument('url')
@click.option('--data', default=None, metavar='', help='Payload for HTTP PATCH')
def patch(url, data):
  n_url = normalize_url(url)
  if data is not None:
    try:
      json_data = json.loads(data)
      r = requests.patch(n_url, data=json_data)
      print(r.text)
      return
    except:
      pass
  r = requests.patch(n_url, data=data)
  print(r.text)

def normalize_url(url):
  if url.startswith('http://') or url.startswith('https://'):
    return url
  else:
    return f'http://{url}'

@http_.command()
@click.option('--port', default=8000, metavar='', help='Port for local HTTP server. Default: 8000.')
def serve(port):
  """Serve local http server. For dev/test only. Do NOT use for production."""
  with socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f'Serving at port {port}')
    httpd.serve_forever()
