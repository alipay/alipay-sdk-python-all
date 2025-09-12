#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpInteopOpauthCreateModel(object):

    def __init__(self):
        self._inteop_order_no = None
        self._product_codes = None

    @property
    def inteop_order_no(self):
        return self._inteop_order_no

    @inteop_order_no.setter
    def inteop_order_no(self, value):
        self._inteop_order_no = value
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
        if self.inteop_order_no:
            if hasattr(self.inteop_order_no, 'to_alipay_dict'):
                params['inteop_order_no'] = self.inteop_order_no.to_alipay_dict()
            else:
                params['inteop_order_no'] = self.inteop_order_no
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
        o = AlipayOpenSpInteopOpauthCreateModel()
        if 'inteop_order_no' in d:
            o.inteop_order_no = d['inteop_order_no']
        if 'product_codes' in d:
            o.product_codes = d['product_codes']
        return o


