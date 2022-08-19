from typing import Iterable
from functools import cached_property
from pathlib import Path


class TestFile():
    """
    Attributes:
        path (Path): Path to the file.
        bin (bool): Whether the file is binary.
    """
    def __init__(self, path: Path, bin: bool) -> None:
        self.bin = bin
        self.path = path

    def __repr__(self):
        return f'TestFile({self.path!r})'

    @cached_property
    def content(self):
        with open(self.path, 'rb' if self.bin else 'r') as f:
            return f.read()


def load(path: Path | str, bin=False) -> TestFile:
    """
    Load a testing data file by path relative this source file.
    """
    here_dir = Path(__file__).parent
    return TestFile(here_dir / path, bin=bin)


def gload(pattern: str, bin=False) -> Iterable[TestFile]:
    """
    Load multiple data files by glob pattern.

    Example:
        test_data.gload('specs/a_b_*.yaml')
    """
    here_dir = Path(__file__).parent
    matches = here_dir.glob(pattern)
    return (TestFile(m, bin=bin) for m in matches)
