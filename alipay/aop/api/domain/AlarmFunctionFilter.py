#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlarmFunctionFilter(object):

    def __init__(self):
        self._filter_type = None
        self._functions = None

    @property
    def filter_type(self):
        return self._filter_type

    @filter_type.setter
    def filter_type(self, value):
        self._filter_type = value
    @property
    def functions(self):
        return self._functions

    @functions.setter
    def functions(self, value):
        if isinstance(value, list):
            self._functions = list()
            for i in value:
                self._functions.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.filter_type:
            if hasattr(self.filter_type, 'to_alipay_dict'):
                params['filter_type'] = self.filter_type.to_alipay_dict()
            else:
                params['filter_type'] = self.filter_type
        if self.functions:
            if isinstance(self.functions, list):
                for i in range(0, len(self.functions)):
                    element = self.functions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.functions[i] = element.to_alipay_dict()
            if hasattr(self.functions, 'to_alipay_dict'):
                params['functions'] = self.functions.to_alipay_dict()
            else:
                params['functions'] = self.functions
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlarmFunctionFilter()
        if 'filter_type' in d:
            o.filter_type = d['filter_type']
        if 'functions' in d:
            o.functions = d['functions']
        return o


