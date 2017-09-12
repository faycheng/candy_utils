# -*- coding:utf-8 -*-

import types
from functools import wraps


def _compare(item, another, attr, callable):
    if attr is None:
        return item == another
    try:
        if not callable:
            return getattr(item, attr) == getattr(another, attr)
        return getattr(item, attr)() == getattr(another, attr)()
    except AttributeError:
        return False


def _iter(obj, attr, callable):
    obj = sorted(obj)
    last = object()
    for item in obj:
        if _compare(item, last, attr, callable):
            continue
        yield item
        last = item


def unique(attr=None, callable=False):
    def func_decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            if not (isinstance(res, list) or isinstance(res, types.GeneratorType)):
                return res
            return _iter(res, attr, callable)

        return inner

    return func_decorator
