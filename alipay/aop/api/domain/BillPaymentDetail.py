#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BillPaymentDetail(object):

    def __init__(self):
        self._bill_payment_id = None

    @property
    def bill_payment_id(self):
        return self._bill_payment_id

    @bill_payment_id.setter
    def bill_payment_id(self, value):
        self._bill_payment_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_payment_id:
            if hasattr(self.bill_payment_id, 'to_alipay_dict'):
                params['bill_payment_id'] = self.bill_payment_id.to_alipay_dict()
            else:
                params['bill_payment_id'] = self.bill_payment_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BillPaymentDetail()
        if 'bill_payment_id' in d:
            o.bill_payment_id = d['bill_payment_id']
        return o


