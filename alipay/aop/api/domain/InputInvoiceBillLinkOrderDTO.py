#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class InputInvoiceBillLinkOrderDTO(object):

    def __init__(self):
        self._bill_no = None
        self._out_bill_type = None
        self._relate_amount = None
        self._tax_amt = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def out_bill_type(self):
        return self._out_bill_type

    @out_bill_type.setter
    def out_bill_type(self, value):
        self._out_bill_type = value
    @property
    def relate_amount(self):
        return self._relate_amount

    @relate_amount.setter
    def relate_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._relate_amount = value
        else:
            self._relate_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def tax_amt(self):
        return self._tax_amt

    @tax_amt.setter
    def tax_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._tax_amt = value
        else:
            self._tax_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.out_bill_type:
            if hasattr(self.out_bill_type, 'to_alipay_dict'):
                params['out_bill_type'] = self.out_bill_type.to_alipay_dict()
            else:
                params['out_bill_type'] = self.out_bill_type
        if self.relate_amount:
            if hasattr(self.relate_amount, 'to_alipay_dict'):
                params['relate_amount'] = self.relate_amount.to_alipay_dict()
            else:
                params['relate_amount'] = self.relate_amount
        if self.tax_amt:
            if hasattr(self.tax_amt, 'to_alipay_dict'):
                params['tax_amt'] = self.tax_amt.to_alipay_dict()
            else:
                params['tax_amt'] = self.tax_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InputInvoiceBillLinkOrderDTO()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'out_bill_type' in d:
            o.out_bill_type = d['out_bill_type']
        if 'relate_amount' in d:
            o.relate_amount = d['relate_amount']
        if 'tax_amt' in d:
            o.tax_amt = d['tax_amt']
        return o


