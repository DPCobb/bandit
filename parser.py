import os
import subprocess
import time


class BanditParser:
    def __init__(self):
        self.methods = [
            'EXEC',
            'WAIT',
            'SUPE',
            'HOTK',
            'SEND',
            'GRAB',
            'TYPE',
            'COMM',
            'EXIT',
        ]

    def parseCommand(self, cmd):
        # split 1 time this should give use the method
        parts = cmd.split(' ', 1)

        self.runCommand(parts[0], parts[1])

    def runCommand(self, method, args):
        # These will be moved to methods, this is just quick test
        if method == "EXEC":
            output = subprocess.run(args.split(' '))
            print(output)

        elif method == 'WAIT':
            wait = int(args)/1000
            time.sleep(wait)
