#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditFinancePayAccountInfo import CreditFinancePayAccountInfo
from alipay.aop.api.domain.CreditFinancePayAccountInfo import CreditFinancePayAccountInfo


class AlipayTradeCreditFinancePayModel(object):

    def __init__(self):
        self._amount = None
        self._business_type = None
        self._currency = None
        self._extend_params = None
        self._out_request_no = None
        self._payee_info = None
        self._payer_info = None
        self._subject = None
        self._trade_buyer_id = None
        self._trade_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def payee_info(self):
        return self._payee_info

    @payee_info.setter
    def payee_info(self, value):
        if isinstance(value, CreditFinancePayAccountInfo):
            self._payee_info = value
        else:
            self._payee_info = CreditFinancePayAccountInfo.from_alipay_dict(value)
    @property
    def payer_info(self):
        return self._payer_info

    @payer_info.setter
    def payer_info(self, value):
        if isinstance(value, CreditFinancePayAccountInfo):
            self._payer_info = value
        else:
            self._payer_info = CreditFinancePayAccountInfo.from_alipay_dict(value)
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def trade_buyer_id(self):
        return self._trade_buyer_id

    @trade_buyer_id.setter
    def trade_buyer_id(self, value):
        self._trade_buyer_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.payee_info:
            if hasattr(self.payee_info, 'to_alipay_dict'):
                params['payee_info'] = self.payee_info.to_alipay_dict()
            else:
                params['payee_info'] = self.payee_info
        if self.payer_info:
            if hasattr(self.payer_info, 'to_alipay_dict'):
                params['payer_info'] = self.payer_info.to_alipay_dict()
            else:
                params['payer_info'] = self.payer_info
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.trade_buyer_id:
            if hasattr(self.trade_buyer_id, 'to_alipay_dict'):
                params['trade_buyer_id'] = self.trade_buyer_id.to_alipay_dict()
            else:
                params['trade_buyer_id'] = self.trade_buyer_id
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
        o = AlipayTradeCreditFinancePayModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'currency' in d:
            o.currency = d['currency']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'payee_info' in d:
            o.payee_info = d['payee_info']
        if 'payer_info' in d:
            o.payer_info = d['payer_info']
        if 'subject' in d:
            o.subject = d['subject']
        if 'trade_buyer_id' in d:
            o.trade_buyer_id = d['trade_buyer_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


