import click

from pyfiglet import Figlet

from green_code_evaluator.commands import analyze
from green_code_evaluator.util.cli import print_message
from green_code_evaluator.util.text import remove_last_line


@click.group()
def cli():
    pass


cli.add_command(analyze.command)

try:
    import colorama

    colorama.init()
except Exception:
    pass


def get_motd():
    figlet = Figlet(font="standard")
    logo = figlet.renderText("GCODE")
    logo = remove_last_line(remove_last_line(logo))
    logo += "\nCode Analyzer Tool\n"
    return logo


def run():
    print_message(get_motd())
    cli()


if __name__ == "__main__":
    run()
