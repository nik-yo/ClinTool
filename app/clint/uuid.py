import click
import uuid

@click.group('uuid')
def uuid_():
  pass

@uuid_.command()
@click.option('--version', default='4', metavar='', help='(Optional) UUID version, supported values: 1, 3, 4, 5. Default: 4')
def gen(version):
  match version:
    case '1':
      print(uuid.uuid1())
    case '3':
      print(uuid.uuid3(uuid.NAMESPACE_DNS, 'python'))
    case '4':
      print(uuid.uuid4())
    case '5':
      print(uuid.uuid5(uuid.NAMESPACE_DNS, 'python'))
    case _:
      print('Invalid version. Supported versions: 1, 3, 4, 5. Default: 4')

    