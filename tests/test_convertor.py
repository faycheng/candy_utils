# -*- coding:utf-8 -*-
import pytest

from candy_utils import faker
from candy_utils.convertor import str2boo
from candy.enums.boolstrs import BoolStrs


def test_str2bool():
    ts = BoolStrs.TRUE.value
    for t in ts:
        assert str2boo(t) is True

    fs = BoolStrs.FALSE.value
    for f in fs:
        assert str2boo(f) is False

    s = faker.random_string()
    assert str2boo(s, strict=False) is False

    with pytest.raises(ValueError):
        str2boo(s, strict=True)
