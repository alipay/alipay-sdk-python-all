#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderStatus(object):

    def __init__(self):
        self._order_code = None
        self._order_desc = None

    @property
    def order_code(self):
        return self._order_code

    @order_code.setter
    def order_code(self, value):
        self._order_code = value
    @property
    def order_desc(self):
        return self._order_desc

    @order_desc.setter
    def order_desc(self, value):
        self._order_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_code:
            if hasattr(self.order_code, 'to_alipay_dict'):
                params['order_code'] = self.order_code.to_alipay_dict()
            else:
                params['order_code'] = self.order_code
        if self.order_desc:
            if hasattr(self.order_desc, 'to_alipay_dict'):
                params['order_desc'] = self.order_desc.to_alipay_dict()
            else:
                params['order_desc'] = self.order_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderStatus()
        if 'order_code' in d:
            o.order_code = d['order_code']
        if 'order_desc' in d:
            o.order_desc = d['order_desc']
        return o


