#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JinyouTestOne import JinyouTestOne


class JinyouTestTwo(object):

    def __init__(self):
        self._t_1_openid = None
        self._t_1_y = None
        self._t_2_f = None
        self._t_3_n = None

    @property
    def t_1_openid(self):
        return self._t_1_openid

    @t_1_openid.setter
    def t_1_openid(self, value):
        self._t_1_openid = value
    @property
    def t_1_y(self):
        return self._t_1_y

    @t_1_y.setter
    def t_1_y(self, value):
        self._t_1_y = value
    @property
    def t_2_f(self):
        return self._t_2_f

    @t_2_f.setter
    def t_2_f(self, value):
        if isinstance(value, JinyouTestOne):
            self._t_2_f = value
        else:
            self._t_2_f = JinyouTestOne.from_alipay_dict(value)
    @property
    def t_3_n(self):
        return self._t_3_n

    @t_3_n.setter
    def t_3_n(self, value):
        self._t_3_n = value


    def to_alipay_dict(self):
        params = dict()
        if self.t_1_openid:
            if hasattr(self.t_1_openid, 'to_alipay_dict'):
                params['t_1_openid'] = self.t_1_openid.to_alipay_dict()
            else:
                params['t_1_openid'] = self.t_1_openid
        if self.t_1_y:
            if hasattr(self.t_1_y, 'to_alipay_dict'):
                params['t_1_y'] = self.t_1_y.to_alipay_dict()
            else:
                params['t_1_y'] = self.t_1_y
        if self.t_2_f:
            if hasattr(self.t_2_f, 'to_alipay_dict'):
                params['t_2_f'] = self.t_2_f.to_alipay_dict()
            else:
                params['t_2_f'] = self.t_2_f
        if self.t_3_n:
            if hasattr(self.t_3_n, 'to_alipay_dict'):
                params['t_3_n'] = self.t_3_n.to_alipay_dict()
            else:
                params['t_3_n'] = self.t_3_n
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JinyouTestTwo()
        if 't_1_openid' in d:
            o.t_1_openid = d['t_1_openid']
        if 't_1_y' in d:
            o.t_1_y = d['t_1_y']
        if 't_2_f' in d:
            o.t_2_f = d['t_2_f']
        if 't_3_n' in d:
            o.t_3_n = d['t_3_n']
        return o


