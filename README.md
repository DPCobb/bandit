# Bandit
## Task Automation and GUI Scripting


### TODO
Everything.

### Bandit File (.bdt)

This will be loaded and run line by line

#### Language Definition

These are the first commands I'd like to have working

```
EXEC    Executes a command in the terminal
WAIT    Delay/wait etc
SUPE    Windows Key/Command key
HOTK    Sends a hot key combination
SEND    Sends a key stroke (ie: Enter)
GRAB    Take a screenshot
TYPE    Send text to GUI
COMM    Comment
EXIT    Ends the script
```

EX:

```
SUPE
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