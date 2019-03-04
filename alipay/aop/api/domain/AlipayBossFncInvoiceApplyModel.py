#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class AlipayBossFncInvoiceApplyModel(object):

    def __init__(self):
        self._biz_id = None
        self._biz_no = None
        self._invoice_amt = None
        self._invoice_type = None
        self._memo = None
        self._mthtly_bill_nos = None
        self._operator = None
        self._out_biz_type = None

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
    def mthtly_bill_nos(self):
        return self._mthtly_bill_nos

    @mthtly_bill_nos.setter
    def mthtly_bill_nos(self, value):
        if isinstance(value, list):
            self._mthtly_bill_nos = list()
            for i in value:
                self._mthtly_bill_nos.append(i)
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value


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
        if self.mthtly_bill_nos:
            if isinstance(self.mthtly_bill_nos, list):
                for i in range(0, len(self.mthtly_bill_nos)):
                    element = self.mthtly_bill_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mthtly_bill_nos[i] = element.to_alipay_dict()
            if hasattr(self.mthtly_bill_nos, 'to_alipay_dict'):
                params['mthtly_bill_nos'] = self.mthtly_bill_nos.to_alipay_dict()
            else:
                params['mthtly_bill_nos'] = self.mthtly_bill_nos
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncInvoiceApplyModel()
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
        if 'mthtly_bill_nos' in d:
            o.mthtly_bill_nos = d['mthtly_bill_nos']
        if 'operator' in d:
            o.operator = d['operator']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        return o


