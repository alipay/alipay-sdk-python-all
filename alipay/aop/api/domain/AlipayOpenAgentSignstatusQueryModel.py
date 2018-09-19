#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAgentSignstatusQueryModel(object):

    def __init__(self):
        self._pid = None
        self._product_codes = None

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def product_codes(self):
        return self._product_codes

    @product_codes.setter
    def product_codes(self, value):
        if isinstance(value, list):
            self._product_codes = list()
            for i in value:
                self._product_codes.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.product_codes:
            if isinstance(self.product_codes, list):
                for i in range(0, len(self.product_codes)):
                    element = self.product_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_codes[i] = element.to_alipay_dict()
            if hasattr(self.product_codes, 'to_alipay_dict'):
                params['product_codes'] = self.product_codes.to_alipay_dict()
            else:
                params['product_codes'] = self.product_codes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAgentSignstatusQueryModel()
        if 'pid' in d:
            o.pid = d['pid']
        if 'product_codes' in d:
            o.product_codes = d['product_codes']
        return o


