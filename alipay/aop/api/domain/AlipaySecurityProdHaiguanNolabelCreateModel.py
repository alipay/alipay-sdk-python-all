#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdHaiguanNolabelCreateModel(object):

    def __init__(self):
        self._one = None

    @property
    def one(self):
        return self._one

    @one.setter
    def one(self, value):
        self._one = value


    def to_alipay_dict(self):
        params = dict()
        if self.one:
            if hasattr(self.one, 'to_alipay_dict'):
                params['one'] = self.one.to_alipay_dict()
            else:
                params['one'] = self.one
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdHaiguanNolabelCreateModel()
        if 'one' in d:
            o.one = d['one']
        return o


