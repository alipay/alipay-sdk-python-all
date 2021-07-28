#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceAmountLimitInfo(object):

    def __init__(self):
        self._amount_limit = None
        self._invoice_kind = None
        self._month_amount_limit = None

    @property
    def amount_limit(self):
        return self._amount_limit

    @amount_limit.setter
    def amount_limit(self, value):
        self._amount_limit = value
    @property
    def invoice_kind(self):
        return self._invoice_kind

    @invoice_kind.setter
    def invoice_kind(self, value):
        self._invoice_kind = value
    @property
    def month_amount_limit(self):
        return self._month_amount_limit

    @month_amount_limit.setter
    def month_amount_limit(self, value):
        self._month_amount_limit = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_limit:
            if hasattr(self.amount_limit, 'to_alipay_dict'):
                params['amount_limit'] = self.amount_limit.to_alipay_dict()
            else:
                params['amount_limit'] = self.amount_limit
        if self.invoice_kind:
            if hasattr(self.invoice_kind, 'to_alipay_dict'):
                params['invoice_kind'] = self.invoice_kind.to_alipay_dict()
            else:
                params['invoice_kind'] = self.invoice_kind
        if self.month_amount_limit:
            if hasattr(self.month_amount_limit, 'to_alipay_dict'):
                params['month_amount_limit'] = self.month_amount_limit.to_alipay_dict()
            else:
                params['month_amount_limit'] = self.month_amount_limit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceAmountLimitInfo()
        if 'amount_limit' in d:
            o.amount_limit = d['amount_limit']
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'month_amount_limit' in d:
            o.month_amount_limit = d['month_amount_limit']
        return o


