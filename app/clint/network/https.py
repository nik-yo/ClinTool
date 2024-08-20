import click
import requests
from clint.network.http import get, post, put, delete, head, options, patch

@click.group()
def https():
  pass

@https.command('get')
@click.argument('url')
@click.pass_context
def get_(ctx, url):
  n_url = normalize_url(url)
  ctx.invoke(get, url=n_url)

@https.command('post')
@click.argument('url')
@click.option('--data', default=None, metavar='', help='Payload for HTTP POST')
@click.pass_context
def post_(ctx, url, data):
  n_url = normalize_url(url)
  ctx.invoke(post, url=n_url, data=data)

@http.command('put')
@click.argument('url')
@click.option('--data', default=None, metavar='', help='Payload for HTTP PUT')
@click.pass_context
def put_(ctx, url, data):
  n_url = normalize_url
  ctx.invoke(put, url=n_url, data=data)

@http.command('delete')
@click.argument('url')
@click.pass_context
def delete_(ctx, url):
  n_url = normalize_url
  ctx.invoke(delete, url=n_url)

@http.command('head')
@click.argument('url')
@click.pass_context
def head_(ctx, url)
  n_url = normalize_url
  ctx.invoke(head, url=n_url)

@http.command('options')
@click.argument('url')
@click.pass_context
def options_(ctx, url):
  n_url = normalize_url(url)
  ctx.invoke(options, url=n_url)

@http.command('patch')
@click.argument('url')
@click.option('--data', default=None, metavar='', help='Payload for HTTP PATCH')
@click.pass_context
def patch_(ctx, url, data):
  n_url = normalize_url(url)
  ctx.invoke(patch, url=n_url, data=data)

def normalize_url(url):
  if url.startswith('http://') or url.startswith('https://'):
    return url
  else:
    return f'https://{url}'
