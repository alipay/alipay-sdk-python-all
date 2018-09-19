#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PresetPayToolInfo(object):

    def __init__(self):
        self._amount = None
        self._assert_type_code = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, list):
            self._amount = list()
            for i in value:
                self._amount.append(i)
    @property
    def assert_type_code(self):
        return self._assert_type_code

    @assert_type_code.setter
    def assert_type_code(self, value):
        self._assert_type_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if isinstance(self.amount, list):
                for i in range(0, len(self.amount)):
                    element = self.amount[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.amount[i] = element.to_alipay_dict()
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.assert_type_code:
            if hasattr(self.assert_type_code, 'to_alipay_dict'):
                params['assert_type_code'] = self.assert_type_code.to_alipay_dict()
            else:
                params['assert_type_code'] = self.assert_type_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PresetPayToolInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'assert_type_code' in d:
            o.assert_type_code = d['assert_type_code']
        return o


