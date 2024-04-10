from pathlib import Path

from .interpreter import CapturingInterpreter


def run_python_command(command):
    try:
        return eval(command)
    except SyntaxError:
        interpreter = CapturingInterpreter()
        interpreter.runsource(command)
        output = interpreter.get_output()
        return output.strip()


def store_command(cmd, output, file=Path("cache.txt")):
    with file.open("a") as f:
        f.write(f"{cmd}\n{output}\n")
