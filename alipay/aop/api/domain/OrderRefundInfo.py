#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderRefundInfo(object):

    def __init__(self):
        self._refund_amount = None
        self._service_order_no = None

    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def service_order_no(self):
        return self._service_order_no

    @service_order_no.setter
    def service_order_no(self, value):
        self._service_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.service_order_no:
            if hasattr(self.service_order_no, 'to_alipay_dict'):
                params['service_order_no'] = self.service_order_no.to_alipay_dict()
            else:
                params['service_order_no'] = self.service_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderRefundInfo()
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'service_order_no' in d:
            o.service_order_no = d['service_order_no']
        return o


