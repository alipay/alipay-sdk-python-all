#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubOrderRefundRequest(object):

    def __init__(self):
        self._refund_amount = None
        self._refund_applets_service_amount = None
        self._refund_reason = None
        self._sub_alipay_order_no = None

    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_applets_service_amount(self):
        return self._refund_applets_service_amount

    @refund_applets_service_amount.setter
    def refund_applets_service_amount(self, value):
        self._refund_applets_service_amount = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def sub_alipay_order_no(self):
        return self._sub_alipay_order_no

    @sub_alipay_order_no.setter
    def sub_alipay_order_no(self, value):
        self._sub_alipay_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_applets_service_amount:
            if hasattr(self.refund_applets_service_amount, 'to_alipay_dict'):
                params['refund_applets_service_amount'] = self.refund_applets_service_amount.to_alipay_dict()
            else:
                params['refund_applets_service_amount'] = self.refund_applets_service_amount
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.sub_alipay_order_no:
            if hasattr(self.sub_alipay_order_no, 'to_alipay_dict'):
                params['sub_alipay_order_no'] = self.sub_alipay_order_no.to_alipay_dict()
            else:
                params['sub_alipay_order_no'] = self.sub_alipay_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubOrderRefundRequest()
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_applets_service_amount' in d:
            o.refund_applets_service_amount = d['refund_applets_service_amount']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'sub_alipay_order_no' in d:
            o.sub_alipay_order_no = d['sub_alipay_order_no']
        return o


