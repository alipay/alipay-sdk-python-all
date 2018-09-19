#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantOrderRentCompleteModel(object):

    def __init__(self):
        self._extend_info = None
        self._order_no = None
        self._pay_amount = None
        self._pay_amount_type = None
        self._product_code = None
        self._restore_shop_name = None
        self._restore_time = None

    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_amount_type(self):
        return self._pay_amount_type

    @pay_amount_type.setter
    def pay_amount_type(self, value):
        self._pay_amount_type = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def restore_shop_name(self):
        return self._restore_shop_name

    @restore_shop_name.setter
    def restore_shop_name(self, value):
        self._restore_shop_name = value
    @property
    def restore_time(self):
        return self._restore_time

    @restore_time.setter
    def restore_time(self, value):
        self._restore_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_amount_type:
            if hasattr(self.pay_amount_type, 'to_alipay_dict'):
                params['pay_amount_type'] = self.pay_amount_type.to_alipay_dict()
            else:
                params['pay_amount_type'] = self.pay_amount_type
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.restore_shop_name:
            if hasattr(self.restore_shop_name, 'to_alipay_dict'):
                params['restore_shop_name'] = self.restore_shop_name.to_alipay_dict()
            else:
                params['restore_shop_name'] = self.restore_shop_name
        if self.restore_time:
            if hasattr(self.restore_time, 'to_alipay_dict'):
                params['restore_time'] = self.restore_time.to_alipay_dict()
            else:
                params['restore_time'] = self.restore_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantOrderRentCompleteModel()
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_amount_type' in d:
            o.pay_amount_type = d['pay_amount_type']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'restore_shop_name' in d:
            o.restore_shop_name = d['restore_shop_name']
        if 'restore_time' in d:
            o.restore_time = d['restore_time']
        return o


