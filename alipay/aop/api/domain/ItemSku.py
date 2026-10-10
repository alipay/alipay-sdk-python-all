#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemSkuAttr import ItemSkuAttr


class ItemSku(object):

    def __init__(self):
        self._original_price = None
        self._out_sku_code = None
        self._sale_price = None
        self._sku_attrs = None
        self._sku_code = None

    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def out_sku_code(self):
        return self._out_sku_code

    @out_sku_code.setter
    def out_sku_code(self, value):
        self._out_sku_code = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def sku_attrs(self):
        return self._sku_attrs

    @sku_attrs.setter
    def sku_attrs(self, value):
        if isinstance(value, list):
            self._sku_attrs = list()
            for i in value:
                if isinstance(i, ItemSkuAttr):
                    self._sku_attrs.append(i)
                else:
                    self._sku_attrs.append(ItemSkuAttr.from_alipay_dict(i))
    @property
    def sku_code(self):
        return self._sku_code

    @sku_code.setter
    def sku_code(self, value):
        self._sku_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.out_sku_code:
            if hasattr(self.out_sku_code, 'to_alipay_dict'):
                params['out_sku_code'] = self.out_sku_code.to_alipay_dict()
            else:
                params['out_sku_code'] = self.out_sku_code
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.sku_attrs:
            if isinstance(self.sku_attrs, list):
                for i in range(0, len(self.sku_attrs)):
                    element = self.sku_attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_attrs[i] = element.to_alipay_dict()
            if hasattr(self.sku_attrs, 'to_alipay_dict'):
                params['sku_attrs'] = self.sku_attrs.to_alipay_dict()
            else:
                params['sku_attrs'] = self.sku_attrs
        if self.sku_code:
            if hasattr(self.sku_code, 'to_alipay_dict'):
                params['sku_code'] = self.sku_code.to_alipay_dict()
            else:
                params['sku_code'] = self.sku_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemSku()
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'out_sku_code' in d:
            o.out_sku_code = d['out_sku_code']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'sku_attrs' in d:
            o.sku_attrs = d['sku_attrs']
        if 'sku_code' in d:
            o.sku_code = d['sku_code']
        return o


