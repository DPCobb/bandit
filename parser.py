import os
import subprocess
import time
import pyautogui


class BanditParser:
    def __init__(self, verbose=False):
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

        self.verbose = verbose

    def red(self, text):
        print('\033[91m' + text + '\033[0m')

    def blue(self, text):
        print('\033[94m' + text + '\033[0m')

    def parseCommand(self, cmd):
        # split 1 time this should give use the method
        parts = cmd.split(' ', 1)
        args = '' if len(parts) < 2 else parts[1]
        self.runCommand(parts[0], args)

    def runExecMethod(self, args):
        output = subprocess.run(args.split(' '))

        if self.verbose:
            print(output)

    def runWaitMethod(self, args):
        wait = int(args)/1000
        time.sleep(wait)

    def runCommentMethod(self, args):
        if self.verbose:
            self.red("Comment: " + args)

    def runGrab(self, args):
        pyautogui.screenshot(args)

    def runHotKey(self, args):
        keys = args.split(' ')
        pyautogui.hotkey(*keys)

    def runTypeMethod(self, args):
        pyautogui.write(args)

    def runCommand(self, method, args=''):
        if method not in self.methods:
            self.red('Error! Unknown method: ' + method)
            return 0

        if method == "EXEC":
            self.runExecMethod(args)

        elif method == 'WAIT':
            self.runWaitMethod(args)

        elif method == 'COMM':
            self.runCommentMethod(args)

        elif method == "GRAB":
            self.runGrab(args)

        elif method == "HOTK":
            self.runHotKey(args)

        elif method == "TYPE":
            self.runTypeMethod(args)

        elif method == "EXIT":
            self.blue("Script complete, exiting now.")
            return 0
