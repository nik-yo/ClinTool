import click
from clint.network.http import http
from clint.network.https import https
from clint.uuid import uuid_

@click.group()
def cli():
  pass

cli.add_command(http)
cli.add_command(https)
cli.add_command(uuid_)