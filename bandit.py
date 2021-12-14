import click
import os
import subprocess
from parser import BanditParser
from debugger import BanditDebugger


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


def red(text):
    print('\033[91m' + text + '\033[0m')


def checkDownload(response):
    codes = ['404', '401', '403', '500', '501', '503', '301', '302']
    if (response.split(':')[0] in codes):
        blue('Error getting file: ' + response + '. Exiting')
        return False


@click.group()
def main():
    pass


@main.command()
def init():
    """Show the title information"""
    showTitle()
    blue("This tool is for personal use only. Please follow allow applicable laws when using this tool.")
    blue("\nI'm not responsible if you do anything dumb.")
    blue("\nThis tool uses PyAutoGUI for sending keystrokes and taking screenshots.")
    blue("\nView the possible key inputs here: https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys")


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
@click.option('--url', '-u', default="", help="Raw GitHub URL to the remote file to load")
@click.option('--verbose', '-v', is_flag=True, help="Turn on some more verbose output")
def remote(url, verbose):
    """Loads a remote Bandit file and runs it"""
    showTitle()
    blue('Attempting to load and run remote file...')

    if url.find('https://raw.githubusercontent.com') < 0:
        red('Error! Remote file must be a Raw GitHub URL')
        return 0

    command = ['curl', '-s', url]

    if verbose == True:
        command = ['curl', url]

    r = subprocess.run(
        command, stdout=subprocess.PIPE).stdout.decode('utf-8')
    parser = BanditParser(verbose)
    blue('Running remote file...')
    for lines in r.split('\n'):
        clean = lines.strip()
        if len(clean) > 0:
            if checkDownload(clean) == False:
                return 0
            parser.parseCommand(clean)


@main.command()
@click.option('--filename', '-f', help="Debug a Bandit file.")
def debug(filename):
    """Debugs a Bandit file and ensures it has the correct syntax"""
    showTitle()
    blue('Loading Bandit file to debug...')
    debugger = BanditDebugger()
    if (os.path.exists(filename)):
        blue('File discovered, running script...')
        f = open(filename, 'r')
        script = f.readlines()
        for i, lines in enumerate(script):
            clean = lines.strip()
            if len(clean) > 0:
                debugger.parseDebug(clean, i)

        debugger.displayErrors()

    else:
        blue('File not found: ' + filename)


if __name__ == '__main__':
    main()
