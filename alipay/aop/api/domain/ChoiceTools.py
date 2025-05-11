#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChoiceTools(object):

    def __init__(self):
        self._expected = None
        self._name = None
        self._params = None
        self._type = None

    @property
    def expected(self):
        return self._expected

    @expected.setter
    def expected(self, value):
        self._expected = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.expected:
            if hasattr(self.expected, 'to_alipay_dict'):
                params['expected'] = self.expected.to_alipay_dict()
            else:
                params['expected'] = self.expected
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChoiceTools()
        if 'expected' in d:
            o.expected = d['expected']
        if 'name' in d:
            o.name = d['name']
        if 'params' in d:
            o.params = d['params']
        if 'type' in d:
            o.type = d['type']
        return o


