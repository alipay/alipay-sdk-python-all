#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceApplyDetail(object):

    def __init__(self):
        self._bill_no = None
        self._biz_fund_type = None
        self._invoice_amount = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def biz_fund_type(self):
        return self._biz_fund_type

    @biz_fund_type.setter
    def biz_fund_type(self, value):
        self._biz_fund_type = value
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.biz_fund_type:
            if hasattr(self.biz_fund_type, 'to_alipay_dict'):
                params['biz_fund_type'] = self.biz_fund_type.to_alipay_dict()
            else:
                params['biz_fund_type'] = self.biz_fund_type
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
        o = InvoiceApplyDetail()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'biz_fund_type' in d:
            o.biz_fund_type = d['biz_fund_type']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        return o


