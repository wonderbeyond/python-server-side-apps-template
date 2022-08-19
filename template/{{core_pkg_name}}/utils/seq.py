"""
Utils for sequence types.
"""
from typing import Any
from collections.abc import Sequence


def interlude(seq: Sequence[Any], lude: Any, /) -> Sequence[Any]:
    """
    >>> interlude(["a", "b", "c"], "-")
    ['a', '-', 'b', '-', 'c']

    >>> interlude((1, 2, 3), 0)
    (1, 0, 2, 0, 3)
    """
    seq_type = type(seq)
    seq_len = len(seq)
    ret_elms = []

    for idx, val in enumerate(seq):
        ret_elms.append(val)
        if idx != seq_len - 1:
            ret_elms.append(lude)

    return seq_type(ret_elms)
