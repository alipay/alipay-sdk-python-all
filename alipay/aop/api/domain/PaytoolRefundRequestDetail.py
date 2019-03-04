#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaytoolRefundRequestDetail(object):

    def __init__(self):
        self._paytool_bill_no = None
        self._paytool_request_no = None
        self._refund_amount = None

    @property
    def paytool_bill_no(self):
        return self._paytool_bill_no

    @paytool_bill_no.setter
    def paytool_bill_no(self, value):
        self._paytool_bill_no = value
    @property
    def paytool_request_no(self):
        return self._paytool_request_no

    @paytool_request_no.setter
    def paytool_request_no(self, value):
        self._paytool_request_no = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.paytool_bill_no:
            if hasattr(self.paytool_bill_no, 'to_alipay_dict'):
                params['paytool_bill_no'] = self.paytool_bill_no.to_alipay_dict()
            else:
                params['paytool_bill_no'] = self.paytool_bill_no
        if self.paytool_request_no:
            if hasattr(self.paytool_request_no, 'to_alipay_dict'):
                params['paytool_request_no'] = self.paytool_request_no.to_alipay_dict()
            else:
                params['paytool_request_no'] = self.paytool_request_no
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaytoolRefundRequestDetail()
        if 'paytool_bill_no' in d:
            o.paytool_bill_no = d['paytool_bill_no']
        if 'paytool_request_no' in d:
            o.paytool_request_no = d['paytool_request_no']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        return o


