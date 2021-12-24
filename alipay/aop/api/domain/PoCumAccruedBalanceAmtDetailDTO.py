#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PoCumAccruedBalanceAmtDetailDTO(object):

    def __init__(self):
        self._cum_accrued_balance_amt = None
        self._currency = None
        self._po_key = None
        self._po_line_no = None
        self._po_no = None

    @property
    def cum_accrued_balance_amt(self):
        return self._cum_accrued_balance_amt

    @cum_accrued_balance_amt.setter
    def cum_accrued_balance_amt(self, value):
        self._cum_accrued_balance_amt = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def po_key(self):
        return self._po_key

    @po_key.setter
    def po_key(self, value):
        self._po_key = value
    @property
    def po_line_no(self):
        return self._po_line_no

    @po_line_no.setter
    def po_line_no(self, value):
        self._po_line_no = value
    @property
    def po_no(self):
        return self._po_no

    @po_no.setter
    def po_no(self, value):
        self._po_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.cum_accrued_balance_amt:
            if hasattr(self.cum_accrued_balance_amt, 'to_alipay_dict'):
                params['cum_accrued_balance_amt'] = self.cum_accrued_balance_amt.to_alipay_dict()
            else:
                params['cum_accrued_balance_amt'] = self.cum_accrued_balance_amt
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.po_key:
            if hasattr(self.po_key, 'to_alipay_dict'):
                params['po_key'] = self.po_key.to_alipay_dict()
            else:
                params['po_key'] = self.po_key
        if self.po_line_no:
            if hasattr(self.po_line_no, 'to_alipay_dict'):
                params['po_line_no'] = self.po_line_no.to_alipay_dict()
            else:
                params['po_line_no'] = self.po_line_no
        if self.po_no:
            if hasattr(self.po_no, 'to_alipay_dict'):
                params['po_no'] = self.po_no.to_alipay_dict()
            else:
                params['po_no'] = self.po_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PoCumAccruedBalanceAmtDetailDTO()
        if 'cum_accrued_balance_amt' in d:
            o.cum_accrued_balance_amt = d['cum_accrued_balance_amt']
        if 'currency' in d:
            o.currency = d['currency']
        if 'po_key' in d:
            o.po_key = d['po_key']
        if 'po_line_no' in d:
            o.po_line_no = d['po_line_no']
        if 'po_no' in d:
            o.po_no = d['po_no']
        return o


