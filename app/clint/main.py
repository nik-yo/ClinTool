import click
from .network.http import http_
from .network.https import https
from .uuid import uuid_
from .lettercase import lowercase, uppercase

@click.group()
def cli():
  pass

cli.add_command(http_)
cli.add_command(https)
cli.add_command(uuid_)
cli.add_command(lowercase)
cli.add_command(uppercase)