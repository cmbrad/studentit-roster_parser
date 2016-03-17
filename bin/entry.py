import click

from lib.models.roster import Roster
from lib.parser import parse_roster
from lib.uploader import GoogleCalendarUploader


@click.group()
def cli():
    pass


@cli.command()
@click.option('--file-name', required=True)
def parse(file_name):
    try:
        print('Parsing..')
        roster = parse_roster(file_name)
        roster.save()
    except IOError as e:
        print('Could not parse roster. Error: {}'.format(e.strerror))


@cli.command()
@click.option('--provider', default='gcal')
def upload(provider):
    roster = Roster.load('saves/roster.p')
    uploader = GoogleCalendarUploader(roster)
    uploader.upload_roster()


if __name__ == '__main__':
    cli()
