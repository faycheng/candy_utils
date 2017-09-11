# -*- coding:utf-8 -*-

from candy_utils import faker


def test_random_lower_str():
    s = faker.random_lower_string()
    assert s == s.lower()
    assert len(s) == 8

    s = faker.random_lower_string(length=10)
    assert len(s) == 10


