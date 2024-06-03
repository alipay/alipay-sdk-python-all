#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExpenseBillItem import ExpenseBillItem


class ExpenseBillQueryItem(object):

    def __init__(self):
        self._expense_list = None
        self._trade_no = None

    @property
    def expense_list(self):
        return self._expense_list

    @expense_list.setter
    def expense_list(self, value):
        if isinstance(value, ExpenseBillItem):
            self._expense_list = value
        else:
            self._expense_list = ExpenseBillItem.from_alipay_dict(value)
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.expense_list:
            if hasattr(self.expense_list, 'to_alipay_dict'):
                params['expense_list'] = self.expense_list.to_alipay_dict()
            else:
                params['expense_list'] = self.expense_list
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExpenseBillQueryItem()
        if 'expense_list' in d:
            o.expense_list = d['expense_list']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


