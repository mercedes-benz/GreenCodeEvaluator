import click


def print_message(text: str, nl=True):
    click.echo(text, err=False, nl=nl)
