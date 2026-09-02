#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderNegotiatedPaymentTime(object):

    def __init__(self):
        self._installment_no = None
        self._negotiated_payment_time = None

    @property
    def installment_no(self):
        return self._installment_no

    @installment_no.setter
    def installment_no(self, value):
        self._installment_no = value
    @property
    def negotiated_payment_time(self):
        return self._negotiated_payment_time

    @negotiated_payment_time.setter
    def negotiated_payment_time(self, value):
        self._negotiated_payment_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.installment_no:
            if hasattr(self.installment_no, 'to_alipay_dict'):
                params['installment_no'] = self.installment_no.to_alipay_dict()
            else:
                params['installment_no'] = self.installment_no
        if self.negotiated_payment_time:
            if hasattr(self.negotiated_payment_time, 'to_alipay_dict'):
                params['negotiated_payment_time'] = self.negotiated_payment_time.to_alipay_dict()
            else:
                params['negotiated_payment_time'] = self.negotiated_payment_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderNegotiatedPaymentTime()
        if 'installment_no' in d:
            o.installment_no = d['installment_no']
        if 'negotiated_payment_time' in d:
            o.negotiated_payment_time = d['negotiated_payment_time']
        return o


