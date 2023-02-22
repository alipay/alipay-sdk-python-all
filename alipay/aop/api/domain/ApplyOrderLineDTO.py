#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApplyOrderLineDTO(object):

    def __init__(self):
        self._fulfil_product_code = None
        self._product_property = None
        self._sales_product_code = None

    @property
    def fulfil_product_code(self):
        return self._fulfil_product_code

    @fulfil_product_code.setter
    def fulfil_product_code(self, value):
        self._fulfil_product_code = value
    @property
    def product_property(self):
        return self._product_property

    @product_property.setter
    def product_property(self, value):
        self._product_property = value
    @property
    def sales_product_code(self):
        return self._sales_product_code

    @sales_product_code.setter
    def sales_product_code(self, value):
        self._sales_product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.fulfil_product_code:
            if hasattr(self.fulfil_product_code, 'to_alipay_dict'):
                params['fulfil_product_code'] = self.fulfil_product_code.to_alipay_dict()
            else:
                params['fulfil_product_code'] = self.fulfil_product_code
        if self.product_property:
            if hasattr(self.product_property, 'to_alipay_dict'):
                params['product_property'] = self.product_property.to_alipay_dict()
            else:
                params['product_property'] = self.product_property
        if self.sales_product_code:
            if hasattr(self.sales_product_code, 'to_alipay_dict'):
                params['sales_product_code'] = self.sales_product_code.to_alipay_dict()
            else:
                params['sales_product_code'] = self.sales_product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApplyOrderLineDTO()
        if 'fulfil_product_code' in d:
            o.fulfil_product_code = d['fulfil_product_code']
        if 'product_property' in d:
            o.product_property = d['product_property']
        if 'sales_product_code' in d:
            o.sales_product_code = d['sales_product_code']
        return o


