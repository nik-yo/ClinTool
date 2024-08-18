import click
import requests
import re

@click.group()
def http():
  pass

@http.command()
@click.argument('url')
def get(url):
  if url.startswith('http://'):
    r = requests.get(url)
  else:
    r = requests.get(f'http://{url}')
  print(r.text)