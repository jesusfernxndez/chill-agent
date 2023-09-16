import click


@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def saludar(name):
    message = f'Hola, {name}'
    click.echo(message)


if __name__ == '__main__':
    saludar()
