#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/6/7 11:45
@Author   : ji hao ran
@File     : __init__.py.py
@Project  : StreamlitAntdComponents
@Software : PyCharm
"""
from .data_class import *
from .setting import *
from .component_func import component_func
from .callback import register_callback
from .parser import *
from typing import Callable, Union
import inspect


def get_func_name():
    return inspect.stack()[1][3]
