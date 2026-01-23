#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTaxTaxdataEvaluateModel(object):

    def __init__(self):
        self._evaluation_type = None
        self._final_refund_amount = None
        self._final_refund_currency = None
        self._payment_method_id = None
        self._refund_amount = None
        self._refund_currency = None

    @property
    def evaluation_type(self):
        return self._evaluation_type

    @evaluation_type.setter
    def evaluation_type(self, value):
        self._evaluation_type = value
    @property
    def final_refund_amount(self):
        return self._final_refund_amount

    @final_refund_amount.setter
    def final_refund_amount(self, value):
        self._final_refund_amount = value
    @property
    def final_refund_currency(self):
        return self._final_refund_currency

    @final_refund_currency.setter
    def final_refund_currency(self, value):
        self._final_refund_currency = value
    @property
    def payment_method_id(self):
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, value):
        self._payment_method_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_currency(self):
        return self._refund_currency

    @refund_currency.setter
    def refund_currency(self, value):
        self._refund_currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.evaluation_type:
            if hasattr(self.evaluation_type, 'to_alipay_dict'):
                params['evaluation_type'] = self.evaluation_type.to_alipay_dict()
            else:
                params['evaluation_type'] = self.evaluation_type
        if self.final_refund_amount:
            if hasattr(self.final_refund_amount, 'to_alipay_dict'):
                params['final_refund_amount'] = self.final_refund_amount.to_alipay_dict()
            else:
                params['final_refund_amount'] = self.final_refund_amount
        if self.final_refund_currency:
            if hasattr(self.final_refund_currency, 'to_alipay_dict'):
                params['final_refund_currency'] = self.final_refund_currency.to_alipay_dict()
            else:
                params['final_refund_currency'] = self.final_refund_currency
        if self.payment_method_id:
            if hasattr(self.payment_method_id, 'to_alipay_dict'):
                params['payment_method_id'] = self.payment_method_id.to_alipay_dict()
            else:
                params['payment_method_id'] = self.payment_method_id
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_currency:
            if hasattr(self.refund_currency, 'to_alipay_dict'):
                params['refund_currency'] = self.refund_currency.to_alipay_dict()
            else:
                params['refund_currency'] = self.refund_currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTaxTaxdataEvaluateModel()
        if 'evaluation_type' in d:
            o.evaluation_type = d['evaluation_type']
        if 'final_refund_amount' in d:
            o.final_refund_amount = d['final_refund_amount']
        if 'final_refund_currency' in d:
            o.final_refund_currency = d['final_refund_currency']
        if 'payment_method_id' in d:
            o.payment_method_id = d['payment_method_id']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_currency' in d:
            o.refund_currency = d['refund_currency']
        return o


