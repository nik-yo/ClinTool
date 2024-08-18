import click
from clint.http import http
from clint.uuid import uuid_

@click.group()
def cli():
  pass

cli.add_command(http)
cli.add_command(uuid_)