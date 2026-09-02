#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExpenseDetail(object):

    def __init__(self):
        self._expense_detail_url = None
        self._settlement_id = None

    @property
    def expense_detail_url(self):
        return self._expense_detail_url

    @expense_detail_url.setter
    def expense_detail_url(self, value):
        self._expense_detail_url = value
    @property
    def settlement_id(self):
        return self._settlement_id

    @settlement_id.setter
    def settlement_id(self, value):
        self._settlement_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.expense_detail_url:
            if hasattr(self.expense_detail_url, 'to_alipay_dict'):
                params['expense_detail_url'] = self.expense_detail_url.to_alipay_dict()
            else:
                params['expense_detail_url'] = self.expense_detail_url
        if self.settlement_id:
            if hasattr(self.settlement_id, 'to_alipay_dict'):
                params['settlement_id'] = self.settlement_id.to_alipay_dict()
            else:
                params['settlement_id'] = self.settlement_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExpenseDetail()
        if 'expense_detail_url' in d:
            o.expense_detail_url = d['expense_detail_url']
        if 'settlement_id' in d:
            o.settlement_id = d['settlement_id']
        return o


