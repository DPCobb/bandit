import click
import os
import subprocess
from parser import BanditParser


def showTitle():
    print('\033[91m' + """
.______        ___      .__   __.  _______   __  .___________.
|   _  \      /   \     |  \ |  | |       \ |  | |           |
|  |_)  |    /  ^  \    |   \|  | |  .--.  ||  | `---|  |----`
|   _  <    /  /_\  \   |  . `  | |  |  |  ||  |     |  |
|  |_)  |  /  _____  \  |  |\   | |  '--'  ||  |     |  |
|______/  /__/     \__\ |__| \__| |_______/ |__|     |__|

Task Automation Scripting
Version: 1.0.0-b

    """ + '\033[0m')


def blue(text):
    print('\033[94m' + text + '\033[0m')


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
    blue('Attempting to run .bdt file...')
    if (os.path.exists(filename)):
        blue('File discovered, running script...')
        f = open(filename, 'r')
        script = f.readlines()
        parser = BanditParser(verbose)
        for lines in script:
            clean = lines.strip()
            if len(clean) > 0:
                parser.parseCommand(clean)

    else:
        blue('File not found: ' + filename)


@main.command()
@click.option('--url', '-u', default="", help="URL to the remote file to load")
@click.option('--verbose', '-v', is_flag=True, help="Turn on some more verbose output")
def remote(url, verbose):
    """Loads a remote Bandit file and runs it"""
    showTitle()
    blue('Attempting to load and run remote file...')
    r = subprocess.run(
        ['curl', url], stdout=subprocess.PIPE).stdout.decode('utf-8')
    parser = BanditParser(verbose)
    blue('Running remote file...')
    for lines in r.split('\n'):
        clean = lines.strip()
        if len(clean) > 0:
            parser.parseCommand(clean)


if __name__ == '__main__':
    main()
