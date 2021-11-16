#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EnterprisePayInfo(object):

    def __init__(self):
        self._invoice_amount = None

    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_amount:
            if hasattr(self.invoice_amount, 'to_alipay_dict'):
                params['invoice_amount'] = self.invoice_amount.to_alipay_dict()
            else:
                params['invoice_amount'] = self.invoice_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnterprisePayInfo()
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        return o


