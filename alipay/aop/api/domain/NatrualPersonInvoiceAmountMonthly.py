#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NatrualPersonInvoiceAmountMonthly(object):

    def __init__(self):
        self._invoice_total_amount_monthly = None
        self._month = None

    @property
    def invoice_total_amount_monthly(self):
        return self._invoice_total_amount_monthly

    @invoice_total_amount_monthly.setter
    def invoice_total_amount_monthly(self, value):
        self._invoice_total_amount_monthly = value
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_total_amount_monthly:
            if hasattr(self.invoice_total_amount_monthly, 'to_alipay_dict'):
                params['invoice_total_amount_monthly'] = self.invoice_total_amount_monthly.to_alipay_dict()
            else:
                params['invoice_total_amount_monthly'] = self.invoice_total_amount_monthly
        if self.month:
            if hasattr(self.month, 'to_alipay_dict'):
                params['month'] = self.month.to_alipay_dict()
            else:
                params['month'] = self.month
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NatrualPersonInvoiceAmountMonthly()
        if 'invoice_total_amount_monthly' in d:
            o.invoice_total_amount_monthly = d['invoice_total_amount_monthly']
        if 'month' in d:
            o.month = d['month']
        return o


