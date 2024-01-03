#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RegressionInDomian import RegressionInDomian
from alipay.aop.api.domain.PubNestPub import PubNestPub
from alipay.aop.api.domain.RegressionPublic import RegressionPublic


class AlipaySecurityJhjtestRegtoantApplyModel(object):

    def __init__(self):
        self._a_open_id = None
        self._a_test_a = None
        self._boolean_a = None
        self._comp_a = None
        self._comp_nest = None
        self._comp_pub = None
        self._date_a = None
        self._number_a = None
        self._string_a = None

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
    def boolean_a(self):
        return self._boolean_a

    @boolean_a.setter
    def boolean_a(self, value):
        self._boolean_a = value
    @property
    def comp_a(self):
        return self._comp_a

    @comp_a.setter
    def comp_a(self, value):
        if isinstance(value, RegressionInDomian):
            self._comp_a = value
        else:
            self._comp_a = RegressionInDomian.from_alipay_dict(value)
    @property
    def comp_nest(self):
        return self._comp_nest

    @comp_nest.setter
    def comp_nest(self, value):
        if isinstance(value, PubNestPub):
            self._comp_nest = value
        else:
            self._comp_nest = PubNestPub.from_alipay_dict(value)
    @property
    def comp_pub(self):
        return self._comp_pub

    @comp_pub.setter
    def comp_pub(self, value):
        if isinstance(value, RegressionPublic):
            self._comp_pub = value
        else:
            self._comp_pub = RegressionPublic.from_alipay_dict(value)
    @property
    def date_a(self):
        return self._date_a

    @date_a.setter
    def date_a(self, value):
        self._date_a = value
    @property
    def number_a(self):
        return self._number_a

    @number_a.setter
    def number_a(self, value):
        self._number_a = value
    @property
    def string_a(self):
        return self._string_a

    @string_a.setter
    def string_a(self, value):
        self._string_a = value


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
        if self.boolean_a:
            if hasattr(self.boolean_a, 'to_alipay_dict'):
                params['boolean_a'] = self.boolean_a.to_alipay_dict()
            else:
                params['boolean_a'] = self.boolean_a
        if self.comp_a:
            if hasattr(self.comp_a, 'to_alipay_dict'):
                params['comp_a'] = self.comp_a.to_alipay_dict()
            else:
                params['comp_a'] = self.comp_a
        if self.comp_nest:
            if hasattr(self.comp_nest, 'to_alipay_dict'):
                params['comp_nest'] = self.comp_nest.to_alipay_dict()
            else:
                params['comp_nest'] = self.comp_nest
        if self.comp_pub:
            if hasattr(self.comp_pub, 'to_alipay_dict'):
                params['comp_pub'] = self.comp_pub.to_alipay_dict()
            else:
                params['comp_pub'] = self.comp_pub
        if self.date_a:
            if hasattr(self.date_a, 'to_alipay_dict'):
                params['date_a'] = self.date_a.to_alipay_dict()
            else:
                params['date_a'] = self.date_a
        if self.number_a:
            if hasattr(self.number_a, 'to_alipay_dict'):
                params['number_a'] = self.number_a.to_alipay_dict()
            else:
                params['number_a'] = self.number_a
        if self.string_a:
            if hasattr(self.string_a, 'to_alipay_dict'):
                params['string_a'] = self.string_a.to_alipay_dict()
            else:
                params['string_a'] = self.string_a
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityJhjtestRegtoantApplyModel()
        if 'a_open_id' in d:
            o.a_open_id = d['a_open_id']
        if 'a_test_a' in d:
            o.a_test_a = d['a_test_a']
        if 'boolean_a' in d:
            o.boolean_a = d['boolean_a']
        if 'comp_a' in d:
            o.comp_a = d['comp_a']
        if 'comp_nest' in d:
            o.comp_nest = d['comp_nest']
        if 'comp_pub' in d:
            o.comp_pub = d['comp_pub']
        if 'date_a' in d:
            o.date_a = d['date_a']
        if 'number_a' in d:
            o.number_a = d['number_a']
        if 'string_a' in d:
            o.string_a = d['string_a']
        return o


