#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HealthServiceSku(object):

    def __init__(self):
        self._merchant_item_sku_bar_code = None
        self._sku_id = None

    @property
    def merchant_item_sku_bar_code(self):
        return self._merchant_item_sku_bar_code

    @merchant_item_sku_bar_code.setter
    def merchant_item_sku_bar_code(self, value):
        self._merchant_item_sku_bar_code = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_item_sku_bar_code:
            if hasattr(self.merchant_item_sku_bar_code, 'to_alipay_dict'):
                params['merchant_item_sku_bar_code'] = self.merchant_item_sku_bar_code.to_alipay_dict()
            else:
                params['merchant_item_sku_bar_code'] = self.merchant_item_sku_bar_code
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HealthServiceSku()
        if 'merchant_item_sku_bar_code' in d:
            o.merchant_item_sku_bar_code = d['merchant_item_sku_bar_code']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


