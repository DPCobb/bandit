import click
import os
from parser import BanditParser


def showTitle():
    print("""
.______        ___      .__   __.  _______   __  .___________.
|   _  \      /   \     |  \ |  | |       \ |  | |           |
|  |_)  |    /  ^  \    |   \|  | |  .--.  ||  | `---|  |----`
|   _  <    /  /_\  \   |  . `  | |  |  |  ||  |     |  |
|  |_)  |  /  _____  \  |  |\   | |  '--'  ||  |     |  |
|______/  /__/     \__\ |__| \__| |_______/ |__|     |__|

Task Automation and GUI Action Scripts

    """)


@click.group()
def main():
    pass


@main.command()
def init():
    showTitle()


@main.command()
@click.option('--filename', '-f', default="", help='The Bandit(.bdt) file to run')
@click.option('--verbose', '-v', is_flag=True, help="Turn on some more verbose output")
def load(filename, verbose):
    """Load and run a Bandit file"""
    showTitle()
    print('Attempting to run .bdt file...')
    if (os.path.exists(filename)):
        print('File discovered, running script...')
        f = open(filename, 'r')
        script = f.readlines()
        parser = BanditParser(verbose)
        for lines in script:
            clean = lines.strip()
            parser.parseCommand(clean)

    else:
        print('File not found: ' + filename)


if __name__ == '__main__':
    main()
