#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenServicemarketOrderUpgradeModel(object):

    def __init__(self):
        self._commodity_order_id = None
        self._product_codes = None

    @property
    def commodity_order_id(self):
        return self._commodity_order_id

    @commodity_order_id.setter
    def commodity_order_id(self, value):
        self._commodity_order_id = value
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
        if self.commodity_order_id:
            if hasattr(self.commodity_order_id, 'to_alipay_dict'):
                params['commodity_order_id'] = self.commodity_order_id.to_alipay_dict()
            else:
                params['commodity_order_id'] = self.commodity_order_id
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
        o = AlipayOpenServicemarketOrderUpgradeModel()
        if 'commodity_order_id' in d:
            o.commodity_order_id = d['commodity_order_id']
        if 'product_codes' in d:
            o.product_codes = d['product_codes']
        return o


