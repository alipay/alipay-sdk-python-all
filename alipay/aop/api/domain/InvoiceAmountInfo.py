#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceAmountInfo(object):

    def __init__(self):
        self._bill_amount = None
        self._biz_app_id = None
        self._currency = None
        self._invoiced_amount = None
        self._oid = None
        self._real_amount = None
        self._uninvoice_amount = None

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def invoiced_amount(self):
        return self._invoiced_amount

    @invoiced_amount.setter
    def invoiced_amount(self, value):
        self._invoiced_amount = value
    @property
    def oid(self):
        return self._oid

    @oid.setter
    def oid(self, value):
        self._oid = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def uninvoice_amount(self):
        return self._uninvoice_amount

    @uninvoice_amount.setter
    def uninvoice_amount(self, value):
        self._uninvoice_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.invoiced_amount:
            if hasattr(self.invoiced_amount, 'to_alipay_dict'):
                params['invoiced_amount'] = self.invoiced_amount.to_alipay_dict()
            else:
                params['invoiced_amount'] = self.invoiced_amount
        if self.oid:
            if hasattr(self.oid, 'to_alipay_dict'):
                params['oid'] = self.oid.to_alipay_dict()
            else:
                params['oid'] = self.oid
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        if self.uninvoice_amount:
            if hasattr(self.uninvoice_amount, 'to_alipay_dict'):
                params['uninvoice_amount'] = self.uninvoice_amount.to_alipay_dict()
            else:
                params['uninvoice_amount'] = self.uninvoice_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceAmountInfo()
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'currency' in d:
            o.currency = d['currency']
        if 'invoiced_amount' in d:
            o.invoiced_amount = d['invoiced_amount']
        if 'oid' in d:
            o.oid = d['oid']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        if 'uninvoice_amount' in d:
            o.uninvoice_amount = d['uninvoice_amount']
        return o


