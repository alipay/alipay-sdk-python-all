#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TestResult(object):

    def __init__(self):
        self._c_i_lower = None
        self._c_i_upper = None
        self._diff = None
        self._p_val = None
        self._significance = None
        self._value = None

    @property
    def c_i_lower(self):
        return self._c_i_lower

    @c_i_lower.setter
    def c_i_lower(self, value):
        self._c_i_lower = value
    @property
    def c_i_upper(self):
        return self._c_i_upper

    @c_i_upper.setter
    def c_i_upper(self, value):
        self._c_i_upper = value
    @property
    def diff(self):
        return self._diff

    @diff.setter
    def diff(self, value):
        self._diff = value
    @property
    def p_val(self):
        return self._p_val

    @p_val.setter
    def p_val(self, value):
        self._p_val = value
    @property
    def significance(self):
        return self._significance

    @significance.setter
    def significance(self, value):
        self._significance = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.c_i_lower:
            if hasattr(self.c_i_lower, 'to_alipay_dict'):
                params['c_i_lower'] = self.c_i_lower.to_alipay_dict()
            else:
                params['c_i_lower'] = self.c_i_lower
        if self.c_i_upper:
            if hasattr(self.c_i_upper, 'to_alipay_dict'):
                params['c_i_upper'] = self.c_i_upper.to_alipay_dict()
            else:
                params['c_i_upper'] = self.c_i_upper
        if self.diff:
            if hasattr(self.diff, 'to_alipay_dict'):
                params['diff'] = self.diff.to_alipay_dict()
            else:
                params['diff'] = self.diff
        if self.p_val:
            if hasattr(self.p_val, 'to_alipay_dict'):
                params['p_val'] = self.p_val.to_alipay_dict()
            else:
                params['p_val'] = self.p_val
        if self.significance:
            if hasattr(self.significance, 'to_alipay_dict'):
                params['significance'] = self.significance.to_alipay_dict()
            else:
                params['significance'] = self.significance
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TestResult()
        if 'c_i_lower' in d:
            o.c_i_lower = d['c_i_lower']
        if 'c_i_upper' in d:
            o.c_i_upper = d['c_i_upper']
        if 'diff' in d:
            o.diff = d['diff']
        if 'p_val' in d:
            o.p_val = d['p_val']
        if 'significance' in d:
            o.significance = d['significance']
        if 'value' in d:
            o.value = d['value']
        return o


