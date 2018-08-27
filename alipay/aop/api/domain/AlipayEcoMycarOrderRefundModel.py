#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarOrderRefundModel(object):

    def __init__(self):
        self._order_no = None
        self._refund_fee = None
        self._refund_reason = None
        self._req_no = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def req_no(self):
        return self._req_no

    @req_no.setter
    def req_no(self, value):
        self._req_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.refund_fee:
            if hasattr(self.refund_fee, 'to_alipay_dict'):
                params['refund_fee'] = self.refund_fee.to_alipay_dict()
            else:
                params['refund_fee'] = self.refund_fee
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.req_no:
            if hasattr(self.req_no, 'to_alipay_dict'):
                params['req_no'] = self.req_no.to_alipay_dict()
            else:
                params['req_no'] = self.req_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarOrderRefundModel()
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'refund_fee' in d:
            o.refund_fee = d['refund_fee']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'req_no' in d:
            o.req_no = d['req_no']
        return o


