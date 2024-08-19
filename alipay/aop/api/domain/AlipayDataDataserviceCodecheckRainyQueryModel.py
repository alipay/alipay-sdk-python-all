#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceCodecheckRainyQueryModel(object):

    def __init__(self):
        self._boolean_a = None
        self._boolean_b = None
        self._diff_boolean_b = None
        self._diff_num_c = None
        self._diff_price_d = None
        self._diff_string_a = None
        self._num_a = None
        self._num_b = None
        self._price_a = None
        self._price_b = None
        self._string_a = None
        self._string_b = None

    @property
    def boolean_a(self):
        return self._boolean_a

    @boolean_a.setter
    def boolean_a(self, value):
        self._boolean_a = value
    @property
    def boolean_b(self):
        return self._boolean_b

    @boolean_b.setter
    def boolean_b(self, value):
        self._boolean_b = value
    @property
    def diff_boolean_b(self):
        return self._diff_boolean_b

    @diff_boolean_b.setter
    def diff_boolean_b(self, value):
        self._diff_boolean_b = value
    @property
    def diff_num_c(self):
        return self._diff_num_c

    @diff_num_c.setter
    def diff_num_c(self, value):
        self._diff_num_c = value
    @property
    def diff_price_d(self):
        return self._diff_price_d

    @diff_price_d.setter
    def diff_price_d(self, value):
        self._diff_price_d = value
    @property
    def diff_string_a(self):
        return self._diff_string_a

    @diff_string_a.setter
    def diff_string_a(self, value):
        self._diff_string_a = value
    @property
    def num_a(self):
        return self._num_a

    @num_a.setter
    def num_a(self, value):
        self._num_a = value
    @property
    def num_b(self):
        return self._num_b

    @num_b.setter
    def num_b(self, value):
        self._num_b = value
    @property
    def price_a(self):
        return self._price_a

    @price_a.setter
    def price_a(self, value):
        self._price_a = value
    @property
    def price_b(self):
        return self._price_b

    @price_b.setter
    def price_b(self, value):
        self._price_b = value
    @property
    def string_a(self):
        return self._string_a

    @string_a.setter
    def string_a(self, value):
        self._string_a = value
    @property
    def string_b(self):
        return self._string_b

    @string_b.setter
    def string_b(self, value):
        self._string_b = value


    def to_alipay_dict(self):
        params = dict()
        if self.boolean_a:
            if hasattr(self.boolean_a, 'to_alipay_dict'):
                params['boolean_a'] = self.boolean_a.to_alipay_dict()
            else:
                params['boolean_a'] = self.boolean_a
        if self.boolean_b:
            if hasattr(self.boolean_b, 'to_alipay_dict'):
                params['boolean_b'] = self.boolean_b.to_alipay_dict()
            else:
                params['boolean_b'] = self.boolean_b
        if self.diff_boolean_b:
            if hasattr(self.diff_boolean_b, 'to_alipay_dict'):
                params['diff_boolean_b'] = self.diff_boolean_b.to_alipay_dict()
            else:
                params['diff_boolean_b'] = self.diff_boolean_b
        if self.diff_num_c:
            if hasattr(self.diff_num_c, 'to_alipay_dict'):
                params['diff_num_c'] = self.diff_num_c.to_alipay_dict()
            else:
                params['diff_num_c'] = self.diff_num_c
        if self.diff_price_d:
            if hasattr(self.diff_price_d, 'to_alipay_dict'):
                params['diff_price_d'] = self.diff_price_d.to_alipay_dict()
            else:
                params['diff_price_d'] = self.diff_price_d
        if self.diff_string_a:
            if hasattr(self.diff_string_a, 'to_alipay_dict'):
                params['diff_string_a'] = self.diff_string_a.to_alipay_dict()
            else:
                params['diff_string_a'] = self.diff_string_a
        if self.num_a:
            if hasattr(self.num_a, 'to_alipay_dict'):
                params['num_a'] = self.num_a.to_alipay_dict()
            else:
                params['num_a'] = self.num_a
        if self.num_b:
            if hasattr(self.num_b, 'to_alipay_dict'):
                params['num_b'] = self.num_b.to_alipay_dict()
            else:
                params['num_b'] = self.num_b
        if self.price_a:
            if hasattr(self.price_a, 'to_alipay_dict'):
                params['price_a'] = self.price_a.to_alipay_dict()
            else:
                params['price_a'] = self.price_a
        if self.price_b:
            if hasattr(self.price_b, 'to_alipay_dict'):
                params['price_b'] = self.price_b.to_alipay_dict()
            else:
                params['price_b'] = self.price_b
        if self.string_a:
            if hasattr(self.string_a, 'to_alipay_dict'):
                params['string_a'] = self.string_a.to_alipay_dict()
            else:
                params['string_a'] = self.string_a
        if self.string_b:
            if hasattr(self.string_b, 'to_alipay_dict'):
                params['string_b'] = self.string_b.to_alipay_dict()
            else:
                params['string_b'] = self.string_b
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceCodecheckRainyQueryModel()
        if 'boolean_a' in d:
            o.boolean_a = d['boolean_a']
        if 'boolean_b' in d:
            o.boolean_b = d['boolean_b']
        if 'diff_boolean_b' in d:
            o.diff_boolean_b = d['diff_boolean_b']
        if 'diff_num_c' in d:
            o.diff_num_c = d['diff_num_c']
        if 'diff_price_d' in d:
            o.diff_price_d = d['diff_price_d']
        if 'diff_string_a' in d:
            o.diff_string_a = d['diff_string_a']
        if 'num_a' in d:
            o.num_a = d['num_a']
        if 'num_b' in d:
            o.num_b = d['num_b']
        if 'price_a' in d:
            o.price_a = d['price_a']
        if 'price_b' in d:
            o.price_b = d['price_b']
        if 'string_a' in d:
            o.string_a = d['string_a']
        if 'string_b' in d:
            o.string_b = d['string_b']
        return o


