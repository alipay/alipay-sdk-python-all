#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemOrderBillRefundResponse(object):

    def __init__(self):
        self._refund_fee = None
        self._refund_type = None

    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value
    @property
    def refund_type(self):
        return self._refund_type

    @refund_type.setter
    def refund_type(self, value):
        self._refund_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.refund_fee:
            if hasattr(self.refund_fee, 'to_alipay_dict'):
                params['refund_fee'] = self.refund_fee.to_alipay_dict()
            else:
                params['refund_fee'] = self.refund_fee
        if self.refund_type:
            if hasattr(self.refund_type, 'to_alipay_dict'):
                params['refund_type'] = self.refund_type.to_alipay_dict()
            else:
                params['refund_type'] = self.refund_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemOrderBillRefundResponse()
        if 'refund_fee' in d:
            o.refund_fee = d['refund_fee']
        if 'refund_type' in d:
            o.refund_type = d['refund_type']
        return o


