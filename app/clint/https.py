import click
import requests

@click.group()
def https():
  pass

@http.command()
@click.argument('url')
def get(url):
  if url.startswith('https://'):
    r = requests.get(url)
  else:
    r = requests.get(f'https://{url}')
  print(r.text)