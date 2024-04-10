from typing import NamedTuple

import pytest

from repl.script import store_command


class Command(NamedTuple):
    cmd: str
    output: str
    file: str


@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "cache.txt"


@pytest.fixture
def prepopulated_cache_file(temp_file):
    cmd = "import math; math.sqrt(16)"
    output = "4.0"
    store_command(cmd, output, file=temp_file)
    return Command(cmd, output, temp_file)


@pytest.fixture
def prepopulated_cache_file_more_commands(prepopulated_cache_file):
    cmd = "[x * 2 for x in range(5)]"
    output = [0, 2, 4, 6, 8]
    file = prepopulated_cache_file.file
    store_command(cmd, output, file=file)
    return Command(cmd, output, file)
