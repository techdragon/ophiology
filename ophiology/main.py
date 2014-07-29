import click
from wrappers import clonedigger as clonedigger_app

@click.group()
@click.version_option()
def cli():
    """Ophiology studies your pythons."""
    pass


@cli.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)


@cli.group()
def commandwrappers():
    pass


@commandwrappers.group()
def run():
    pass


@run.command()
def clonedigger():
    click.echo('''Preparing to run "clonedigger" ...''')
    clonedigger_app.execute()

@cli.command()
def dropdb():
    click.echo('Dropped the database')


if __name__ == '__main__':
    cli()
