# -*- coding:utf-8 -*-

import pytest
import types

from unittest import mock
from candy_utils import faker
from candy_utils import unique


def test_compare():
    item = faker.random_string()
    another = item

    assert unique._compare(item, another, None, False) is True

    class Item(object):
        pass
    item = Item()
    attr = faker.random_string()
    attr_value = faker.random_string()
    setattr(item, attr, attr_value)
    another = Item()
    setattr(another, attr, attr_value)
    assert unique._compare(item, another, attr, False) is True

    def item_compare_func():
        return 'hello world'

    def another_compare_func():
        return 'hello world'

    item = Item()
    setattr(item, 'compare_func', item_compare_func)
    another = Item()
    setattr(another, 'compare_func', another_compare_func)
    assert unique._compare(item, another, 'compare_func', True) is True

    item = Item()
    another = Item()
    unique._compare(item, another, faker.random_string(), False) is False


def test_iter():
    with mock.patch.object(unique, '_compare', return_value=False):
        l = [1, 2, 3]
        res = unique._iter(l, None, False)
        assert isinstance(res, types.GeneratorType)
        res = list(res)
        assert len(res) == 3
        assert set(res) == set(l)


def test_unique():
    def func():
        return [1, 2, 3, 2]
    res = unique.unique(None, False)(func)()
    assert isinstance(res, types.GeneratorType)
    res = list(res)
    assert len(res) == 3
    assert set(res) == set([1, 2, 3])

    def func():
        for i in [1, 2, 3, 2]:
            yield i
    res = unique.unique(None, False)(func)()
    assert isinstance(res, types.GeneratorType)
    res = list(res)
    assert len(res) == 3
    assert set(res) == set([1, 2, 3])

    def func():
        return 'hello world'
    res = unique.unique(None, False)(func)()
    assert res == 'hello world'

