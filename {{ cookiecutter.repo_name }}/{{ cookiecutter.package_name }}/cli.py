import click


@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='world', required=False, help='The name to greet with.')
def main(name, as_cowboy):
    greet = 'Howdy' if as_cowboy else 'Hello'
    click.echo('{}, {}.'.format(greet, name))
