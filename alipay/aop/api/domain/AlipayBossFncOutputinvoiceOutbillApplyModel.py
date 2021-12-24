#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.InvoiceApplyOpenApi import InvoiceApplyOpenApi


class AlipayBossFncOutputinvoiceOutbillApplyModel(object):

    def __init__(self):
        self._biz_id = None
        self._biz_no = None
        self._invoice_amt = None
        self._invoice_applys = None
        self._invoice_note = None
        self._memo = None
        self._operator = None
        self._source = None

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
    def invoice_applys(self):
        return self._invoice_applys

    @invoice_applys.setter
    def invoice_applys(self, value):
        if isinstance(value, list):
            self._invoice_applys = list()
            for i in value:
                if isinstance(i, InvoiceApplyOpenApi):
                    self._invoice_applys.append(i)
                else:
                    self._invoice_applys.append(InvoiceApplyOpenApi.from_alipay_dict(i))
    @property
    def invoice_note(self):
        return self._invoice_note

    @invoice_note.setter
    def invoice_note(self, value):
        self._invoice_note = value
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
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


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
        if self.invoice_applys:
            if isinstance(self.invoice_applys, list):
                for i in range(0, len(self.invoice_applys)):
                    element = self.invoice_applys[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_applys[i] = element.to_alipay_dict()
            if hasattr(self.invoice_applys, 'to_alipay_dict'):
                params['invoice_applys'] = self.invoice_applys.to_alipay_dict()
            else:
                params['invoice_applys'] = self.invoice_applys
        if self.invoice_note:
            if hasattr(self.invoice_note, 'to_alipay_dict'):
                params['invoice_note'] = self.invoice_note.to_alipay_dict()
            else:
                params['invoice_note'] = self.invoice_note
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
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncOutputinvoiceOutbillApplyModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'invoice_applys' in d:
            o.invoice_applys = d['invoice_applys']
        if 'invoice_note' in d:
            o.invoice_note = d['invoice_note']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'source' in d:
            o.source = d['source']
        return o


