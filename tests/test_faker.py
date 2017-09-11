# -*- coding:utf-8 -*-

import random
import string
import pytest

from candy_utils import faker


def test_random_lower_str():
    s = faker.random_lower_string()
    assert s == s.lower()
    assert len(s) == 8

    s = faker.random_lower_string(length=10)
    assert len(s) == 10


def test_random_upper_str():
    s = faker.random_upper_string()
    assert s == s.upper()
    assert len(s) == 8

    s = faker.random_upper_string(length=10)
    assert len(s) == 10


def test_random_number_str():
    n = faker.random_number_string()
    assert n.isdigit() is True

    n = faker.random_number_string(length=10)
    assert len(n) == 10


def test_random_str():
    s = faker.random_string()
    for c in s:
        assert c in list(string.ascii_letters + string.digits)
    assert len(s) == 8

    s = faker.random_string(length=10)
    assert len(s) == 10


def test_random_enum():
    enums = ['RED', 'GREEN', 'YELLOW']
    enum = faker.random_enum(enums)
    assert enum in enums

    def gen_enums():
        for color in ['RED', 'GREEN', 'YELLOW']:
            yield color

    enums = gen_enums()
    enum = faker.random_enum(enums)
    assert enum in ['RED', 'GREEN', 'YELLOW']

    for enums in [None, 123]:
        with pytest.raises(TypeError):
            faker.random_enum(enums)

    for enums in [[], {}]:
        with pytest.raises(IndexError):
            faker.random_enum(enums)


