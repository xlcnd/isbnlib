# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file

import os

from subprocess import Popen, PIPE, STDOUT
from tempfile import NamedTemporaryFile


def run_cmd(command, input_text):
    """Run: cmd 'some input text'."""
    return run_cmd_pipe(input_text)

def run_cmd_pipe(command, input_text):
    """Run: echo 'some input text' | python cmd.py."""
    pipe = Popen(['python', command], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    output = pipe.communicate(input=input_text)[0]
    return output

def run_cmd_file(command, input_text):
    """Run: python cmd.py file."""
    temp_file = NamedTemporaryFile(delete=False)
    temp_file.write(input_text)
    temp_file.close()
    pipe = Popen(['python', command, temp_file.name], stdout=PIPE, stderr=STDOUT)
    output = pipe.communicate()[0]
    os.unlink(temp_file.name)
    return output

def run_code(code):
    """Run: python -c 'some code'."""
    pipe = Popen(['python', '-c', code], stdout=PIPE, stderr=STDOUT)
    output = pipe.communicate()[0]
    return output
