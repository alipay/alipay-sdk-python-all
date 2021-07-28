#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class AlipayBossFncInvoiceStatementbillApplyModel(object):

    def __init__(self):
        self._biz_id = None
        self._biz_no = None
        self._invoice_amt = None
        self._invoice_type = None
        self._memo = None
        self._operator = None
        self._statement_bill_list = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def invoice_amt(self):
        return self._invoice_amt

    @invoice_amt.setter
    def invoice_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._invoice_amt = value
        else:
            self._invoice_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def statement_bill_list(self):
        return self._statement_bill_list

    @statement_bill_list.setter
    def statement_bill_list(self, value):
        self._statement_bill_list = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.invoice_amt:
            if hasattr(self.invoice_amt, 'to_alipay_dict'):
                params['invoice_amt'] = self.invoice_amt.to_alipay_dict()
            else:
                params['invoice_amt'] = self.invoice_amt
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.statement_bill_list:
            if hasattr(self.statement_bill_list, 'to_alipay_dict'):
                params['statement_bill_list'] = self.statement_bill_list.to_alipay_dict()
            else:
                params['statement_bill_list'] = self.statement_bill_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncInvoiceStatementbillApplyModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'statement_bill_list' in d:
            o.statement_bill_list = d['statement_bill_list']
        return o


