#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JhjTestNew import JhjTestNew


class RegressionPublic(object):

    def __init__(self):
        self._a_open_id = None
        self._a_test_a = None
        self._b = None
        self._com_a = None
        self._date = None
        self._input_a = None
        self._new_a = None

    @property
    def a_open_id(self):
        return self._a_open_id

    @a_open_id.setter
    def a_open_id(self, value):
        self._a_open_id = value
    @property
    def a_test_a(self):
        return self._a_test_a

    @a_test_a.setter
    def a_test_a(self, value):
        self._a_test_a = value
    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value
    @property
    def com_a(self):
        return self._com_a

    @com_a.setter
    def com_a(self, value):
        if isinstance(value, JhjTestNew):
            self._com_a = value
        else:
            self._com_a = JhjTestNew.from_alipay_dict(value)
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def input_a(self):
        return self._input_a

    @input_a.setter
    def input_a(self, value):
        self._input_a = value
    @property
    def new_a(self):
        return self._new_a

    @new_a.setter
    def new_a(self, value):
        self._new_a = value


    def to_alipay_dict(self):
        params = dict()
        if self.a_open_id:
            if hasattr(self.a_open_id, 'to_alipay_dict'):
                params['a_open_id'] = self.a_open_id.to_alipay_dict()
            else:
                params['a_open_id'] = self.a_open_id
        if self.a_test_a:
            if hasattr(self.a_test_a, 'to_alipay_dict'):
                params['a_test_a'] = self.a_test_a.to_alipay_dict()
            else:
                params['a_test_a'] = self.a_test_a
        if self.b:
            if hasattr(self.b, 'to_alipay_dict'):
                params['b'] = self.b.to_alipay_dict()
            else:
                params['b'] = self.b
        if self.com_a:
            if hasattr(self.com_a, 'to_alipay_dict'):
                params['com_a'] = self.com_a.to_alipay_dict()
            else:
                params['com_a'] = self.com_a
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.input_a:
            if hasattr(self.input_a, 'to_alipay_dict'):
                params['input_a'] = self.input_a.to_alipay_dict()
            else:
                params['input_a'] = self.input_a
        if self.new_a:
            if hasattr(self.new_a, 'to_alipay_dict'):
                params['new_a'] = self.new_a.to_alipay_dict()
            else:
                params['new_a'] = self.new_a
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RegressionPublic()
        if 'a_open_id' in d:
            o.a_open_id = d['a_open_id']
        if 'a_test_a' in d:
            o.a_test_a = d['a_test_a']
        if 'b' in d:
            o.b = d['b']
        if 'com_a' in d:
            o.com_a = d['com_a']
        if 'date' in d:
            o.date = d['date']
        if 'input_a' in d:
            o.input_a = d['input_a']
        if 'new_a' in d:
            o.new_a = d['new_a']
        return o


