import os
import subprocess
import time
import pyautogui


class BanditDebugger:
    def __init__(self):
        self.methods = [
            'EXEC',
            'WAIT',
            'HOTK',
            'SEND',
            'GRAB',
            'TYPE',
            'COMM',
            'IFEL',
            'SECT',
            'EXIT',
        ]

        self.totalErrors = 0
        self.errors = []

    def red(self, text, error=False):
        print('\033[91m' + text + '\033[0m')
        if error:
            self.totalErrors += 1
            self.errors.append(text)

    def blue(self, text):
        print('\033[94m' + text + '\033[0m')

    def green(self, text):
        print('\033[32m' + text + '\033[0m')

    def yellow(self, text):
        print('\033[33m' + text + '\033[0m')

    def checkMethodExists(self, method):
        if method not in self.methods:
            self.red('Error! Unknown method: ' + method, True)
            return False

        return True

    def displayErrors(self):
        if self.totalErrors == 0:
            self.yellow('\n\nNo Errors found in your script!')
            return

        self.red('\n\nDebugger found ' + str(self.totalErrors) +
                 ' errors in your script:')
        for error in self.errors:
            self.yellow(error)

        self.yellow('\nPlease review the output above for more information.')

    def parseDebug(self, cmd, line):
        # split 1 time this should give use the method
        parts = cmd.split(' ', 1)
        self.blue('\n\nDebugging Line Number ' + str(line + 1))
        self.yellow('Debugging method: ' + parts[0])

        exists = self.checkMethodExists(parts[0])
        if exists == False:
            return 0

        args = '' if len(parts) < 2 else parts[1]
        self.runCommand(parts[0], args)

    def runCommand(self, method, args=[]):
        if method == "EXEC":
            self.green('EXEC sends a shell command to the system.')

            if len(args) == 0:
                self.red(
                    'Error! EXEC expects the shell command to be passed.', True)
                return

            self.green('Shell command to send: ' + args)

        elif method == 'WAIT':
            self.green(
                'WAIT sends a delay to the machine. This should be passed in milliseconds')

            if len(args) == 0:
                self.red(
                    'Error! WAIT requires an amount of time in milliseconds to be passed.', True)
                return

            wait = int(args)/1000
            self.green('System would wait for ' + str(wait) + ' seconds')

        elif method == 'COMM':
            self.green('Line is a comment nothing to see here.')
            self.green(args)

        elif method == "GRAB":
            self.green(
                'GRAB command takes a screenshot and saves it to the passed location.')

            if len(args) == 0:
                self.red('Error! GRAB expects location to be passed.', True)
                return

            self.green('Location is: ' + args)

        elif method == "HOTK":
            self.green(
                'HOTK sends a hot key command to the system. This command should be followed by at least one key.')
            keys = args.split(' ')

            if len(keys) == 0:
                self.red('Error! HOTK requires keys to be passed', True)
                return

            self.green('Keys have been passed with the command.')
            self.green('Keys sent: ' + args)

        elif method == "TYPE":
            self.green('TYPE writes text to the current active window.')

            if len(args) == 0:
                self.red(
                    'Error! TYPE requires text to write to active window', True)
                return

            self.green('Text to write to active window: ' + args)

        elif method == "SEND":
            self.green('SEND passes a single key to the machine, like Enter')
            keys = len(args.split(' '))
            if len(args) == 0:
                keys = 0

            if int(keys) != 1:
                self.red('Error! SEND requires one key to be passed', True)
                return

            self.green('SEND would pass the following key: ' + args)

        elif method == 'SECT':
            self.green('SECT contains a single argument naming the SECT')
            if len(args) == 0:
                self.red('Error! SECT missing argument.', True)

        elif method == "EXIT":
            self.green('EXIT ends and exits the script.')
