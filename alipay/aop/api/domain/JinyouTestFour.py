#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JinyouTestThree import JinyouTestThree


class JinyouTestFour(object):

    def __init__(self):
        self._f_1_openid = None
        self._f_1_y = None
        self._f_2_f = None
        self._f_3_openid = None
        self._f_3_y = None

    @property
    def f_1_openid(self):
        return self._f_1_openid

    @f_1_openid.setter
    def f_1_openid(self, value):
        self._f_1_openid = value
    @property
    def f_1_y(self):
        return self._f_1_y

    @f_1_y.setter
    def f_1_y(self, value):
        self._f_1_y = value
    @property
    def f_2_f(self):
        return self._f_2_f

    @f_2_f.setter
    def f_2_f(self, value):
        if isinstance(value, JinyouTestThree):
            self._f_2_f = value
        else:
            self._f_2_f = JinyouTestThree.from_alipay_dict(value)
    @property
    def f_3_openid(self):
        return self._f_3_openid

    @f_3_openid.setter
    def f_3_openid(self, value):
        self._f_3_openid = value
    @property
    def f_3_y(self):
        return self._f_3_y

    @f_3_y.setter
    def f_3_y(self, value):
        self._f_3_y = value


    def to_alipay_dict(self):
        params = dict()
        if self.f_1_openid:
            if hasattr(self.f_1_openid, 'to_alipay_dict'):
                params['f_1_openid'] = self.f_1_openid.to_alipay_dict()
            else:
                params['f_1_openid'] = self.f_1_openid
        if self.f_1_y:
            if hasattr(self.f_1_y, 'to_alipay_dict'):
                params['f_1_y'] = self.f_1_y.to_alipay_dict()
            else:
                params['f_1_y'] = self.f_1_y
        if self.f_2_f:
            if hasattr(self.f_2_f, 'to_alipay_dict'):
                params['f_2_f'] = self.f_2_f.to_alipay_dict()
            else:
                params['f_2_f'] = self.f_2_f
        if self.f_3_openid:
            if hasattr(self.f_3_openid, 'to_alipay_dict'):
                params['f_3_openid'] = self.f_3_openid.to_alipay_dict()
            else:
                params['f_3_openid'] = self.f_3_openid
        if self.f_3_y:
            if hasattr(self.f_3_y, 'to_alipay_dict'):
                params['f_3_y'] = self.f_3_y.to_alipay_dict()
            else:
                params['f_3_y'] = self.f_3_y
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JinyouTestFour()
        if 'f_1_openid' in d:
            o.f_1_openid = d['f_1_openid']
        if 'f_1_y' in d:
            o.f_1_y = d['f_1_y']
        if 'f_2_f' in d:
            o.f_2_f = d['f_2_f']
        if 'f_3_openid' in d:
            o.f_3_openid = d['f_3_openid']
        if 'f_3_y' in d:
            o.f_3_y = d['f_3_y']
        return o


