#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantOrderRentModifyModel(object):

    def __init__(self):
        self._borrow_time = None
        self._expiry_time = None
        self._order_no = None
        self._product_code = None

    @property
    def borrow_time(self):
        return self._borrow_time

    @borrow_time.setter
    def borrow_time(self, value):
        self._borrow_time = value
    @property
    def expiry_time(self):
        return self._expiry_time

    @expiry_time.setter
    def expiry_time(self, value):
        self._expiry_time = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.borrow_time:
            if hasattr(self.borrow_time, 'to_alipay_dict'):
                params['borrow_time'] = self.borrow_time.to_alipay_dict()
            else:
                params['borrow_time'] = self.borrow_time
        if self.expiry_time:
            if hasattr(self.expiry_time, 'to_alipay_dict'):
                params['expiry_time'] = self.expiry_time.to_alipay_dict()
            else:
                params['expiry_time'] = self.expiry_time
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
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
        o = ZhimaMerchantOrderRentModifyModel()
        if 'borrow_time' in d:
            o.borrow_time = d['borrow_time']
        if 'expiry_time' in d:
            o.expiry_time = d['expiry_time']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


