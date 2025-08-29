#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleInspectDigitalProductOpenVO import RecycleInspectDigitalProductOpenVO


class RecycleInspectProductVO(object):

    def __init__(self):
        self._digital_product_info = None
        self._inspect_price = None
        self._out_sku_id = None
        self._out_sku_name = None
        self._product_category = None
        self._product_code = None

    @property
    def digital_product_info(self):
        return self._digital_product_info

    @digital_product_info.setter
    def digital_product_info(self, value):
        if isinstance(value, RecycleInspectDigitalProductOpenVO):
            self._digital_product_info = value
        else:
            self._digital_product_info = RecycleInspectDigitalProductOpenVO.from_alipay_dict(value)
    @property
    def inspect_price(self):
        return self._inspect_price

    @inspect_price.setter
    def inspect_price(self, value):
        self._inspect_price = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def out_sku_name(self):
        return self._out_sku_name

    @out_sku_name.setter
    def out_sku_name(self, value):
        self._out_sku_name = value
    @property
    def product_category(self):
        return self._product_category

    @product_category.setter
    def product_category(self, value):
        self._product_category = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.digital_product_info:
            if hasattr(self.digital_product_info, 'to_alipay_dict'):
                params['digital_product_info'] = self.digital_product_info.to_alipay_dict()
            else:
                params['digital_product_info'] = self.digital_product_info
        if self.inspect_price:
            if hasattr(self.inspect_price, 'to_alipay_dict'):
                params['inspect_price'] = self.inspect_price.to_alipay_dict()
            else:
                params['inspect_price'] = self.inspect_price
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.out_sku_name:
            if hasattr(self.out_sku_name, 'to_alipay_dict'):
                params['out_sku_name'] = self.out_sku_name.to_alipay_dict()
            else:
                params['out_sku_name'] = self.out_sku_name
        if self.product_category:
            if hasattr(self.product_category, 'to_alipay_dict'):
                params['product_category'] = self.product_category.to_alipay_dict()
            else:
                params['product_category'] = self.product_category
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleInspectProductVO()
        if 'digital_product_info' in d:
            o.digital_product_info = d['digital_product_info']
        if 'inspect_price' in d:
            o.inspect_price = d['inspect_price']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'out_sku_name' in d:
            o.out_sku_name = d['out_sku_name']
        if 'product_category' in d:
            o.product_category = d['product_category']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


