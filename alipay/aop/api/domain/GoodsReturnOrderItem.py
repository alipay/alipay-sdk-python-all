#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GoodsReturnOrderItem(object):

    def __init__(self):
        self._ext_info = None
        self._price = None
        self._qty = None
        self._sku_name = None
        self._sku_no = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def qty(self):
        return self._qty

    @qty.setter
    def qty(self, value):
        self._qty = value
    @property
    def sku_name(self):
        return self._sku_name

    @sku_name.setter
    def sku_name(self, value):
        self._sku_name = value
    @property
    def sku_no(self):
        return self._sku_no

    @sku_no.setter
    def sku_no(self, value):
        self._sku_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.qty:
            if hasattr(self.qty, 'to_alipay_dict'):
                params['qty'] = self.qty.to_alipay_dict()
            else:
                params['qty'] = self.qty
        if self.sku_name:
            if hasattr(self.sku_name, 'to_alipay_dict'):
                params['sku_name'] = self.sku_name.to_alipay_dict()
            else:
                params['sku_name'] = self.sku_name
        if self.sku_no:
            if hasattr(self.sku_no, 'to_alipay_dict'):
                params['sku_no'] = self.sku_no.to_alipay_dict()
            else:
                params['sku_no'] = self.sku_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GoodsReturnOrderItem()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'price' in d:
            o.price = d['price']
        if 'qty' in d:
            o.qty = d['qty']
        if 'sku_name' in d:
            o.sku_name = d['sku_name']
        if 'sku_no' in d:
            o.sku_no = d['sku_no']
        return o


