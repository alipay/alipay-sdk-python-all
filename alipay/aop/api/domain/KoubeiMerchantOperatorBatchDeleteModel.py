#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMerchantOperatorBatchDeleteModel(object):

    def __init__(self):
        self._auth_code = None
        self._operators = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def operators(self):
        return self._operators

    @operators.setter
    def operators(self, value):
        if isinstance(value, list):
            self._operators = list()
            for i in value:
                self._operators.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.operators:
            if isinstance(self.operators, list):
                for i in range(0, len(self.operators)):
                    element = self.operators[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operators[i] = element.to_alipay_dict()
            if hasattr(self.operators, 'to_alipay_dict'):
                params['operators'] = self.operators.to_alipay_dict()
            else:
                params['operators'] = self.operators
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMerchantOperatorBatchDeleteModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'operators' in d:
            o.operators = d['operators']
        return o


