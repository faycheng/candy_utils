# -*- coding:utf-8 -*-

import pytest

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


def test_iter():
    pass


def test_unique():
    pass
