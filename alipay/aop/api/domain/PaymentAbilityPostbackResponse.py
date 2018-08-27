#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentAbilityPostbackResponse(object):

    def __init__(self):
        self._error_order = None
        self._order_ids = None

    @property
    def error_order(self):
        return self._error_order

    @error_order.setter
    def error_order(self, value):
        self._error_order = value
    @property
    def order_ids(self):
        return self._order_ids

    @order_ids.setter
    def order_ids(self, value):
        self._order_ids = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_order:
            if hasattr(self.error_order, 'to_alipay_dict'):
                params['error_order'] = self.error_order.to_alipay_dict()
            else:
                params['error_order'] = self.error_order
        if self.order_ids:
            if hasattr(self.order_ids, 'to_alipay_dict'):
                params['order_ids'] = self.order_ids.to_alipay_dict()
            else:
                params['order_ids'] = self.order_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentAbilityPostbackResponse()
        if 'error_order' in d:
            o.error_order = d['error_order']
        if 'order_ids' in d:
            o.order_ids = d['order_ids']
        return o


