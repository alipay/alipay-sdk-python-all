#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppProdmodeUnionbankQueryModel(object):

    def __init__(self):
        self._bank_code = None

    @property
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppProdmodeUnionbankQueryModel()
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        return o


