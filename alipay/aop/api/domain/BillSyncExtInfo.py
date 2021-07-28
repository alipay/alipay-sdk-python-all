#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BillSyncExtInfo(object):

    def __init__(self):
        self._order_pay_type = None

    @property
    def order_pay_type(self):
        return self._order_pay_type

    @order_pay_type.setter
    def order_pay_type(self, value):
        self._order_pay_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_pay_type:
            if hasattr(self.order_pay_type, 'to_alipay_dict'):
                params['order_pay_type'] = self.order_pay_type.to_alipay_dict()
            else:
                params['order_pay_type'] = self.order_pay_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BillSyncExtInfo()
        if 'order_pay_type' in d:
            o.order_pay_type = d['order_pay_type']
        return o


