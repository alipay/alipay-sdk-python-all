#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OverseasExtendParams import OverseasExtendParams


class AlipayTradeOverseasSettleModel(object):

    def __init__(self):
        self._amount = None
        self._extend_params = None
        self._foreign_settle_currency = None
        self._out_request_no = None
        self._trade_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        if isinstance(value, OverseasExtendParams):
            self._extend_params = value
        else:
            self._extend_params = OverseasExtendParams.from_alipay_dict(value)
    @property
    def foreign_settle_currency(self):
        return self._foreign_settle_currency

    @foreign_settle_currency.setter
    def foreign_settle_currency(self, value):
        self._foreign_settle_currency = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
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
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.foreign_settle_currency:
            if hasattr(self.foreign_settle_currency, 'to_alipay_dict'):
                params['foreign_settle_currency'] = self.foreign_settle_currency.to_alipay_dict()
            else:
                params['foreign_settle_currency'] = self.foreign_settle_currency
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
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
        o = AlipayTradeOverseasSettleModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'foreign_settle_currency' in d:
            o.foreign_settle_currency = d['foreign_settle_currency']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


