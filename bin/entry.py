import click

from lib.parse import parse_document


@click.group()
def cli():
	pass


@cli.command()
@click.option('--file-name', required=True)
def parse(file_name):
	parse_document(file_name)


if __name__ == '__main__':
	cli()

