#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceOrderredinvoiceApplyModel(object):

    def __init__(self):
        self._order_id = None
        self._product_id = None
        self._tax_no = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceOrderredinvoiceApplyModel()
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


