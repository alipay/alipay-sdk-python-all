#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JinyouTestFive import JinyouTestFive


class AlipayDataAiserviceJinyoutestSyncModel(object):

    def __init__(self):
        self._t_1_f = None
        self._t_1_n = None
        self._t_1_openid = None
        self._t_1_y = None

    @property
    def t_1_f(self):
        return self._t_1_f

    @t_1_f.setter
    def t_1_f(self, value):
        if isinstance(value, JinyouTestFive):
            self._t_1_f = value
        else:
            self._t_1_f = JinyouTestFive.from_alipay_dict(value)
    @property
    def t_1_n(self):
        return self._t_1_n

    @t_1_n.setter
    def t_1_n(self, value):
        self._t_1_n = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.t_1_f:
            if hasattr(self.t_1_f, 'to_alipay_dict'):
                params['t_1_f'] = self.t_1_f.to_alipay_dict()
            else:
                params['t_1_f'] = self.t_1_f
        if self.t_1_n:
            if hasattr(self.t_1_n, 'to_alipay_dict'):
                params['t_1_n'] = self.t_1_n.to_alipay_dict()
            else:
                params['t_1_n'] = self.t_1_n
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAiserviceJinyoutestSyncModel()
        if 't_1_f' in d:
            o.t_1_f = d['t_1_f']
        if 't_1_n' in d:
            o.t_1_n = d['t_1_n']
        if 't_1_openid' in d:
            o.t_1_openid = d['t_1_openid']
        if 't_1_y' in d:
            o.t_1_y = d['t_1_y']
        return o


