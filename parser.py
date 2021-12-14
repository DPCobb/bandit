import os
import subprocess
import time
import pyautogui


class BanditParser:
    def __init__(self, verbose=False):
        self.methods = [
            'EXEC',
            'WAIT',
            'HOTK',
            'SEND',
            'GRAB',
            'TYPE',
            'COMM',
            'EXIT',
            'IFEL',
            'SECT'
        ]

        self.special = [
            'MOVE'
        ]

        self.logical = [
            'INCLUDES',
            'EXCLUDES',
            'EQ',
            'NOTEQ'
        ]

        self.verbose = verbose
        self.ifActive = False
        self.ifFound = False
        self.ifBlock = ''

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
        output = subprocess.run(args.split(
            ' '), stdout=subprocess.PIPE).stdout.decode('utf-8')
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

    def runSend(self, args):
        if '#' in args:
            parts = args.split('#')
            i = 0

            while i < int(parts[1]):
                pyautogui.hotkey(parts[0])
                i += 1

        else:
            pyautogui.hotkey(args)

    def runTypeMethod(self, args):
        pyautogui.write(args)

    def runIf(self, args):
        parts = args.split(']', 1)
        condition = parts[0]
        condition = condition.replace('[', '', 1)

        output = subprocess.run(condition.split(
            ' '), stdout=subprocess.PIPE).stdout.decode('utf-8')

        if self.verbose:
            print(output)

        logical = parts[1].strip().split(' ', 1)[0]

        if logical not in self.logical:
            self.red('Error! Unknown logical operator: ' + logical)
            return 0

        search = parts[1].strip().split('[', 1)[1]
        search = search.replace(']', '', 1)
        search = search.replace(';;', '', 1)
        search = search.split(' ', 1)[0].strip()
        output = str(output)

        if logical == 'INCLUDES':
            found = output.find(search)
            if self.verbose:
                print(search)

            if found < 0:
                self.ifActive = True
                move = parts[1].strip().split(';;', 1)[1]

                move = move.strip().split('MOVE ', 1)[1]
                self.ifBlock = move

        if logical == 'EXCLUDES':
            found = output.find(search)
            if self.verbose:
                print(search)

            if found > 0:
                self.ifActive = True
                move = parts[1].strip().split(';;', 1)[1]

                move = move.strip().split('MOVE ', 1)[1]
                self.ifBlock = move

        if logical == 'EQ':
            found = output == search
            if self.verbose:
                print(search)

            if found:
                self.ifActive = True
                move = parts[1].strip().split(';;', 1)[1]

                move = move.strip().split('MOVE ', 1)[1]
                self.ifBlock = move

        if logical == 'NOTEQ':
            found = output != search
            if self.verbose:
                print(search)

            if found:
                self.ifActive = True
                move = parts[1].strip().split(';;', 1)[1]

                move = move.strip().split('MOVE ', 1)[1]
                self.ifBlock = move

    def runCommand(self, method, args='', debug=False):
        if method not in self.methods:
            self.red('Error! Unknown method: ' + method)
            return 0

        if self.ifActive == True:
            if method == 'SECT':
                if self.ifBlock == args:
                    self.ifActive = False
        else:
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

            elif method == "SEND":
                self.runSend(args)

            elif method == "IFEL":
                self.runIf(args)

            elif method == "SECT":
                pass

            elif method == "EXIT":
                self.blue("Script complete, exiting now.")
                return 0
