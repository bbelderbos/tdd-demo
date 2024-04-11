from textwrap import dedent

from repl.script import run_python_command


def test_run_addition():
    result = run_python_command("1 + 1")
    assert result == 2


def test_run_listcomp():
    cmd = "[x * 2 for x in range(5)]"
    result = run_python_command(cmd)
    assert result == [0, 2, 4, 6, 8]


def test_math_expression():
    cmd = "import math; math.sqrt(16)"
    result = run_python_command(cmd)
    assert result == "4.0"


def test_store_command_and_output(prepopulated_cache_file):
    expected = f"{prepopulated_cache_file.cmd}\n{prepopulated_cache_file.output}\n"
    assert prepopulated_cache_file.file.read_text() == expected


def test_store_commands_append(prepopulated_cache_file_more_commands):
    expected = dedent(
        """\
        import math; math.sqrt(16)
        4.0
        [x * 2 for x in range(5)]
        [0, 2, 4, 6, 8]
        """
    )

    file_content = prepopulated_cache_file_more_commands.file.read_text()
    assert file_content == expected
