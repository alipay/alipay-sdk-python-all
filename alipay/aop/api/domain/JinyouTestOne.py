#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JinyouTestOne(object):

    def __init__(self):
        self._o_1_n = None
        self._o_2_openid = None
        self._o_2_y = None
        self._o_3_openid = None
        self._o_3_y = None

    @property
    def o_1_n(self):
        return self._o_1_n

    @o_1_n.setter
    def o_1_n(self, value):
        self._o_1_n = value
    @property
    def o_2_openid(self):
        return self._o_2_openid

    @o_2_openid.setter
    def o_2_openid(self, value):
        self._o_2_openid = value
    @property
    def o_2_y(self):
        return self._o_2_y

    @o_2_y.setter
    def o_2_y(self, value):
        self._o_2_y = value
    @property
    def o_3_openid(self):
        return self._o_3_openid

    @o_3_openid.setter
    def o_3_openid(self, value):
        self._o_3_openid = value
    @property
    def o_3_y(self):
        return self._o_3_y

    @o_3_y.setter
    def o_3_y(self, value):
        self._o_3_y = value


    def to_alipay_dict(self):
        params = dict()
        if self.o_1_n:
            if hasattr(self.o_1_n, 'to_alipay_dict'):
                params['o_1_n'] = self.o_1_n.to_alipay_dict()
            else:
                params['o_1_n'] = self.o_1_n
        if self.o_2_openid:
            if hasattr(self.o_2_openid, 'to_alipay_dict'):
                params['o_2_openid'] = self.o_2_openid.to_alipay_dict()
            else:
                params['o_2_openid'] = self.o_2_openid
        if self.o_2_y:
            if hasattr(self.o_2_y, 'to_alipay_dict'):
                params['o_2_y'] = self.o_2_y.to_alipay_dict()
            else:
                params['o_2_y'] = self.o_2_y
        if self.o_3_openid:
            if hasattr(self.o_3_openid, 'to_alipay_dict'):
                params['o_3_openid'] = self.o_3_openid.to_alipay_dict()
            else:
                params['o_3_openid'] = self.o_3_openid
        if self.o_3_y:
            if hasattr(self.o_3_y, 'to_alipay_dict'):
                params['o_3_y'] = self.o_3_y.to_alipay_dict()
            else:
                params['o_3_y'] = self.o_3_y
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JinyouTestOne()
        if 'o_1_n' in d:
            o.o_1_n = d['o_1_n']
        if 'o_2_openid' in d:
            o.o_2_openid = d['o_2_openid']
        if 'o_2_y' in d:
            o.o_2_y = d['o_2_y']
        if 'o_3_openid' in d:
            o.o_3_openid = d['o_3_openid']
        if 'o_3_y' in d:
            o.o_3_y = d['o_3_y']
        return o


