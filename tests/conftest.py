from typing import NamedTuple

import pytest

from repl.script import store_command


class Command(NamedTuple):
    cmd: str
    output: str
    file: str


@pytest.fixture
def prepopulated_cache_file(tmp_path):
    temp_file = tmp_path / "cache.txt"
    cmd = "import math; math.sqrt(16)"
    output = "4.0"
    store_command(cmd, output, file=temp_file)
    return Command(cmd, output, temp_file)
