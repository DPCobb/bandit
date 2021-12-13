# Bandit
## Task Automation Scripting

Bandit helps automate tasks in both the command line and GUI.

Requires curl for remote requests

### Bandit File (.bdt)

This will be loaded and run line by line

## Methods

Below is a list of methods and examples on their use.

### EXEC

Executes a shell command
```
EXEC ls -la
```

### WAIT

Tells the script to wait for a specific period of time in milliseconds.
```
WAIT 1000
```

### HOTK

Sends a series of keys as a hotkey command.

```
HOTK command space
```

### SEND

Sends a single keystroke
```
SEND enter
```

SEND can be used in combination with the special operator ```#[NUM]``` to tell the script to repeat that SEND command x times.

Example send tab four times:
```
SEND tab#4
```

### GRAB

Takes a screen shot and saves it to passed location
```
GRAB /foo/bar/baz.png
```

### TYPE

Sends text to the current active window
```
TYPE hello world
```

### COMM

Marks the line as a comment and it is ignored
```
COMM this is a comment
```

### IFEL
Starts a basic conditional (IF/ELSE) statement
```
IFEL [ls -la] INCLUDES [bandit.py];; MOVE a
```

The above command essentially means:
```
IF the output of executing [cmd] INCLUDES [this string] run;; ELSE MOVE to SECT a
```
The commands between ```IFEL``` and ```SECT a``` will only run if the comparison is TRUE.

**Nested conditionals are not yet supported**

EXAMPLE:
```
IFEL [ls -la] INCLUDES [bandit.py];; MOVE a
TYPE this should be typed if output includes bandit.py
SECT a
IFEL [ls -la] EXCLUDES [bandit.py];; MOVE b
TYPE This should show if output does not have bandit.py
SECT b
TYPE This should always show up
```
To see this in action run the ```payload_if.bdt``` file.

### EXIT

Terminates the script
```
EXIT
```

### Example Script

This is an example BDT script in that on a Mac will open Safari, navigate to google.com, and take a screenshot.
```
HOTK command space
WAIT 1000
TYPE safari.app
WAIT 1000
SEND enter
WAIT 2000
TYPE google.com
SEND enter
WAIT 1000
GRAB google-saf.png
EXIT
```

## Bandit Command Line Application

The command line application processes and runs the Bandit files.

### Commands
```
debug   Debugs a Bandit file and ensures it has the correct syntax
init    Show the title information
load    Load and run a Bandit file
remote  Loads a remote Bandit file and runs it
```

#### load
```
Usage: bandit load [OPTIONS]

  Load and run a Bandit file

Options:
  -f, --filename TEXT  The Bandit(.bdt) file to run
  -v, --verbose        Turn on some more verbose output
  --help               Show this message and exit.
```

#### remote
```
Usage: bandit remote [OPTIONS]

  Loads a remote Bandit file and runs it

Options:
  -u, --url TEXT  URL to the remote file to load
  -v, --verbose   Turn on some more verbose output
  --help          Show this message and exit.
```

#### debug (WIP)

Validates BDT script

```
Usage: bandit debug [OPTIONS]

  Debugs a Bandit file and ensures it has the correct syntax

Options:
  -f, --filename TEXT  Debug a Bandit file.
  --help               Show this message and exit.
```

*TODO* Need to add support for IFEL

### Notes about Mac

Use on a Mac will require some settings to be adjusted. Mac will ask for permissions as needed for the terminal to send key strokes and take screenshots.

## Running a BDT file

In the command line run the following after installing the bandit commnad line application.

```
bandit load -f [BANDIT FILE]
```

You can also pass ```-v``` for verbose output.

## Installing

Clone this repository and run ```pip install .```

## Notes, TODO, and Misc

These are the first commands I'd like to have working

```
EXEC    Executes a command in the terminal
WAIT    Delay/wait etc
HOTK    Sends a hot key combination
SEND    Sends a key stroke (ie: Enter)
GRAB    Take a screenshot
TYPE    Send text to GUI
COMM    Comment
EXIT    Ends the script
```

EX:

```
HOTK win
TYPE terminal
SEND enter
TYPE ls -la
SEND enter
GRAB
EXIT
```

Nice to have:
```
MOVE    Move to a specific spot in script
IF      If this do this (IF .... MOV ...)
```
We'll have to see what is possible with pyauto gui but here's the idea of if/move
(IF this is true MOVE to this part of the code)

```
IF window has something;; MOVE a
SUPE
TYPE terminal
SEND enter
[a] # << if condition met we skip to here
TYPE ls -la
```

Hold command to highlight text:
```
HOLD shift right#4
```
