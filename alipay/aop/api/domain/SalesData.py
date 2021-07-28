#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SalesData(object):

    def __init__(self):
        self._dt = None
        self._order_count = None
        self._refund_order_count = None
        self._refund_sales_amount = None
        self._sales_amount = None

    @property
    def dt(self):
        return self._dt

    @dt.setter
    def dt(self, value):
        self._dt = value
    @property
    def order_count(self):
        return self._order_count

    @order_count.setter
    def order_count(self, value):
        self._order_count = value
    @property
    def refund_order_count(self):
        return self._refund_order_count

    @refund_order_count.setter
    def refund_order_count(self, value):
        self._refund_order_count = value
    @property
    def refund_sales_amount(self):
        return self._refund_sales_amount

    @refund_sales_amount.setter
    def refund_sales_amount(self, value):
        self._refund_sales_amount = value
    @property
    def sales_amount(self):
        return self._sales_amount

    @sales_amount.setter
    def sales_amount(self, value):
        self._sales_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.dt:
            if hasattr(self.dt, 'to_alipay_dict'):
                params['dt'] = self.dt.to_alipay_dict()
            else:
                params['dt'] = self.dt
        if self.order_count:
            if hasattr(self.order_count, 'to_alipay_dict'):
                params['order_count'] = self.order_count.to_alipay_dict()
            else:
                params['order_count'] = self.order_count
        if self.refund_order_count:
            if hasattr(self.refund_order_count, 'to_alipay_dict'):
                params['refund_order_count'] = self.refund_order_count.to_alipay_dict()
            else:
                params['refund_order_count'] = self.refund_order_count
        if self.refund_sales_amount:
            if hasattr(self.refund_sales_amount, 'to_alipay_dict'):
                params['refund_sales_amount'] = self.refund_sales_amount.to_alipay_dict()
            else:
                params['refund_sales_amount'] = self.refund_sales_amount
        if self.sales_amount:
            if hasattr(self.sales_amount, 'to_alipay_dict'):
                params['sales_amount'] = self.sales_amount.to_alipay_dict()
            else:
                params['sales_amount'] = self.sales_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SalesData()
        if 'dt' in d:
            o.dt = d['dt']
        if 'order_count' in d:
            o.order_count = d['order_count']
        if 'refund_order_count' in d:
            o.refund_order_count = d['refund_order_count']
        if 'refund_sales_amount' in d:
            o.refund_sales_amount = d['refund_sales_amount']
        if 'sales_amount' in d:
            o.sales_amount = d['sales_amount']
        return o


