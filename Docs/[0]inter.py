# Using Python Interpreter

# py\python\python3 will launch interactive mode
# function quit() will exit the mode

# likewise unixshell, interpreter:
r"""
when connected to tty device it reads\executes commands
interactively

but when given a file as an input (same with filename arg)
it reads and executes from a sctipt from that file
"""

primary_prompt = ">>>"
print("single commands through:", primary_prompt)

secondary_prompt = "..."
print("tabbed or indented code:", secondary_prompt)


# secondary prompt is obviously needed in multi-line construct

r"""
>>> multi_verse_exists = True
>>> if multi_verse_exists:
...     print('so we\'re immortal and funny')
... else:
...     print('bummer jokes')
...
"""

# encoding settings
# -*- coding: utf-8 -*-
