#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyVO import MultiCurrencyMoneyVO
from alipay.aop.api.domain.MultiCurrencyMoneyVO import MultiCurrencyMoneyVO
from alipay.aop.api.domain.MultiCurrencyMoneyVO import MultiCurrencyMoneyVO
from alipay.aop.api.domain.MultiCurrencyMoneyVO import MultiCurrencyMoneyVO


class BillRepayBudgetVO(object):

    def __init__(self):
        self._apply_amount = None
        self._bill_no = None
        self._should_repay_int_amt = None
        self._should_repay_pen_amt = None
        self._should_repay_prin_amt = None

    @property
    def apply_amount(self):
        return self._apply_amount

    @apply_amount.setter
    def apply_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyVO):
            self._apply_amount = value
        else:
            self._apply_amount = MultiCurrencyMoneyVO.from_alipay_dict(value)
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def should_repay_int_amt(self):
        return self._should_repay_int_amt

    @should_repay_int_amt.setter
    def should_repay_int_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyVO):
            self._should_repay_int_amt = value
        else:
            self._should_repay_int_amt = MultiCurrencyMoneyVO.from_alipay_dict(value)
    @property
    def should_repay_pen_amt(self):
        return self._should_repay_pen_amt

    @should_repay_pen_amt.setter
    def should_repay_pen_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyVO):
            self._should_repay_pen_amt = value
        else:
            self._should_repay_pen_amt = MultiCurrencyMoneyVO.from_alipay_dict(value)
    @property
    def should_repay_prin_amt(self):
        return self._should_repay_prin_amt

    @should_repay_prin_amt.setter
    def should_repay_prin_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyVO):
            self._should_repay_prin_amt = value
        else:
            self._should_repay_prin_amt = MultiCurrencyMoneyVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.apply_amount:
            if hasattr(self.apply_amount, 'to_alipay_dict'):
                params['apply_amount'] = self.apply_amount.to_alipay_dict()
            else:
                params['apply_amount'] = self.apply_amount
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.should_repay_int_amt:
            if hasattr(self.should_repay_int_amt, 'to_alipay_dict'):
                params['should_repay_int_amt'] = self.should_repay_int_amt.to_alipay_dict()
            else:
                params['should_repay_int_amt'] = self.should_repay_int_amt
        if self.should_repay_pen_amt:
            if hasattr(self.should_repay_pen_amt, 'to_alipay_dict'):
                params['should_repay_pen_amt'] = self.should_repay_pen_amt.to_alipay_dict()
            else:
                params['should_repay_pen_amt'] = self.should_repay_pen_amt
        if self.should_repay_prin_amt:
            if hasattr(self.should_repay_prin_amt, 'to_alipay_dict'):
                params['should_repay_prin_amt'] = self.should_repay_prin_amt.to_alipay_dict()
            else:
                params['should_repay_prin_amt'] = self.should_repay_prin_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BillRepayBudgetVO()
        if 'apply_amount' in d:
            o.apply_amount = d['apply_amount']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'should_repay_int_amt' in d:
            o.should_repay_int_amt = d['should_repay_int_amt']
        if 'should_repay_pen_amt' in d:
            o.should_repay_pen_amt = d['should_repay_pen_amt']
        if 'should_repay_prin_amt' in d:
            o.should_repay_prin_amt = d['should_repay_prin_amt']
        return o


