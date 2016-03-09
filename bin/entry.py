import click

from lib.parser import parse_roster
from lib.uploader import GoogleCalendarUploader


@click.group()
def cli():
    pass


@cli.command()
@click.option('--file-name', required=True)
def parse(file_name):
    try:
        roster = parse_roster(file_name)
    except IOError as e:
        print('Could not parse roster. Error: {}'.format(e.strerror))

    uploader = GoogleCalendarUploader(roster)
    uploader.upload_roster()


if __name__ == '__main__':
    cli()
