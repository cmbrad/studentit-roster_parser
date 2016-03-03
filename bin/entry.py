import click

from lib.parser import parse_roster


@click.group()
def cli():
    pass


@cli.command()
@click.option('--file-name', required=True)
def parse(file_name):
    try:
        roster = parse_roster(file_name)
        print(roster)
    except IOError as e:
        print('Could not parse roster. Error: {}'.format(e.strerror))


if __name__ == '__main__':
    cli()
