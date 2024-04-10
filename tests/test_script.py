from textwrap import dedent

from repl.script import run_python_command, store_command


def test_run_addition():
    result = run_python_command('1 + 1')
    assert result == 2

def test_run_listcomp():
    cmd = "[x * 2 for x in range(5)]"
    result = run_python_command(cmd)
    assert result == [0, 2, 4, 6, 8]

def test_math_expression():
    cmd = "import math; math.sqrt(16)"
    result = run_python_command(cmd)
    assert result == "4.0"

def test_store_command_and_output(store_file):
    assert store_file.file.read_text() == f"{store_file.cmd}\n{store_file.output}\n"

'''
def test_store_commands_append(tmp_path):
    cmd = "[x * 2 for x in range(5)]"
    output = [0, 2, 4, 6, 8]
    store_command(cmd, output, file=temp_file)
    expected = dedent("""
    import math; math.sqrt(16)
    4.0
    [x * 2 for x in range(5)]
    [0, 2, 4, 6, 8]
    """).lstrip()
    assert temp_file.read_text() == expected
'''
