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
        args = '' if len(parts) < 2 else parts[1]
        self.runCommand(parts[0], args)

    def runCommand(self, method, args=''):
        # These will be moved to methods, this is just quick test
        if method not in self.methods:
            print('Error! Unknown method: ' + method)
            return 0

        if method == "EXEC":
            output = subprocess.run(args.split(' '))
            print(output)

        elif method == 'WAIT':
            wait = int(args)/1000
            time.sleep(wait)

        elif method == "EXIT":
            print("Script complete, exiting now.")
            return 0
