import click


@click.group()
def main():
    pass


@main.command()
def init():
    """Title screen"""
    print("""
.______        ___      .__   __.  _______   __  .___________.
|   _  \      /   \     |  \ |  | |       \ |  | |           |
|  |_)  |    /  ^  \    |   \|  | |  .--.  ||  | `---|  |----`
|   _  <    /  /_\  \   |  . `  | |  |  |  ||  |     |  |     
|  |_)  |  /  _____  \  |  |\   | |  '--'  ||  |     |  |     
|______/  /__/     \__\ |__| \__| |_______/ |__|     |__|     

Task Automation and GUI Action Scripts 

Use --help for available commands.      
    """)


@main.command()
@click.option('--filename', '-f', default="", help='The Bandit(.bdt) file to run')
def load(filename):
    """Load and run a Bandit file"""
    print(filename)


if __name__ == '__main__':
    main()
