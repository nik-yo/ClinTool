import click

@click.command()
@click.argument('text')
def lowercase(text):
  print(text.lower())

@click.command()
@click.argument('text')
def uppercase(text):
  print(text.upper())