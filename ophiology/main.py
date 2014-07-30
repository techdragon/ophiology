# -*- coding: utf-8 -*-
"""This is the entry point for the Ophiology application"""
import click

from ophiology.util.log import LOGGING
from ophiology.util.log import CONSOLE
from ophiology.tools import ccm as ccm_tool
from ophiology.tools import checkstyle as checkstyle_tool
from ophiology.tools import clonedigger as clonedigger_tool
from ophiology.util.django import django_apps

@click.group()
@click.version_option()
@click.option('--debug', is_flag=True, default=False,
    help='Enable Debug Statements')
@click.option('--log-test', is_flag=True, default=False)
def cli(debug, log_test):
    """Ophiology studies your pythons."""
    if debug:
        LOGGING.add(LOGGING.DEBUG, CONSOLE)
    if log_test:
        LOGGING.debug('Testing the DEBUG level logger')
        LOGGING.info('Testing the INFO level logger')
        LOGGING.error('Testing the ERROR level logger')
        LOGGING.warning('Testing the WARNING level logger')
        LOGGING.critical('Testing the CRITICAL level logger')
        LOGGING.all('Testing the ALL level logger')
        LOGGING.multi(
            ('DEBUG', 'INFO', 'ERROR', 'WARNING', 'CRITICAL'),
            'Testing the MULTI level logger to the ' +
            'DEBUG, INFO, ERROR, WARNING, and CRITICAL levels')


@cli.command()
def clonedigger():
    click.echo('''Preparing to run "clonedigger" ...''')
    clonedigger_tool.execute()


@cli.command()
def ccm():
    click.echo('''Running "ccm" ...''')
    ccm_tool.execute()


@cli.command()
def checkstyle():
    click.echo('''Running "checkstyle" ...''')
    checkstyle_tool.execute()



@cli.command()
@click.argument('path')
def django(path):
    click.echo('Under development')
    django_apps(path)



if __name__ == '__main__':
    cli()
