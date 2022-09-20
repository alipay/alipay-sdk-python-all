#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JinyouTestFive import JinyouTestFive


class AlipayPayAppXuanyitestQueryModel(object):

    def __init__(self):
        self._o_1_openid = None
        self._o_1_y = None
        self._o_2_n = None
        self._o_3_f = None

    @property
    def o_1_openid(self):
        return self._o_1_openid

    @o_1_openid.setter
    def o_1_openid(self, value):
        self._o_1_openid = value
    @property
    def o_1_y(self):
        return self._o_1_y

    @o_1_y.setter
    def o_1_y(self, value):
        self._o_1_y = value
    @property
    def o_2_n(self):
        return self._o_2_n

    @o_2_n.setter
    def o_2_n(self, value):
        self._o_2_n = value
    @property
    def o_3_f(self):
        return self._o_3_f

    @o_3_f.setter
    def o_3_f(self, value):
        if isinstance(value, JinyouTestFive):
            self._o_3_f = value
        else:
            self._o_3_f = JinyouTestFive.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.o_1_openid:
            if hasattr(self.o_1_openid, 'to_alipay_dict'):
                params['o_1_openid'] = self.o_1_openid.to_alipay_dict()
            else:
                params['o_1_openid'] = self.o_1_openid
        if self.o_1_y:
            if hasattr(self.o_1_y, 'to_alipay_dict'):
                params['o_1_y'] = self.o_1_y.to_alipay_dict()
            else:
                params['o_1_y'] = self.o_1_y
        if self.o_2_n:
            if hasattr(self.o_2_n, 'to_alipay_dict'):
                params['o_2_n'] = self.o_2_n.to_alipay_dict()
            else:
                params['o_2_n'] = self.o_2_n
        if self.o_3_f:
            if hasattr(self.o_3_f, 'to_alipay_dict'):
                params['o_3_f'] = self.o_3_f.to_alipay_dict()
            else:
                params['o_3_f'] = self.o_3_f
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayAppXuanyitestQueryModel()
        if 'o_1_openid' in d:
            o.o_1_openid = d['o_1_openid']
        if 'o_1_y' in d:
            o.o_1_y = d['o_1_y']
        if 'o_2_n' in d:
            o.o_2_n = d['o_2_n']
        if 'o_3_f' in d:
            o.o_3_f = d['o_3_f']
        return o


