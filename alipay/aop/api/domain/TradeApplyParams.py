#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradeApplyParams(object):

    def __init__(self):
        self._broker_id = None
        self._buyer_name = None
        self._currency = None
        self._expire_time = None
        self._out_trade_no = None
        self._promo_params = None
        self._subject = None
        self._total_amount = None

    @property
    def broker_id(self):
        return self._broker_id

    @broker_id.setter
    def broker_id(self, value):
        self._broker_id = value
    @property
    def buyer_name(self):
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, value):
        self._buyer_name = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def promo_params(self):
        return self._promo_params

    @promo_params.setter
    def promo_params(self, value):
        self._promo_params = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.broker_id:
            if hasattr(self.broker_id, 'to_alipay_dict'):
                params['broker_id'] = self.broker_id.to_alipay_dict()
            else:
                params['broker_id'] = self.broker_id
        if self.buyer_name:
            if hasattr(self.buyer_name, 'to_alipay_dict'):
                params['buyer_name'] = self.buyer_name.to_alipay_dict()
            else:
                params['buyer_name'] = self.buyer_name
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.promo_params:
            if hasattr(self.promo_params, 'to_alipay_dict'):
                params['promo_params'] = self.promo_params.to_alipay_dict()
            else:
                params['promo_params'] = self.promo_params
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradeApplyParams()
        if 'broker_id' in d:
            o.broker_id = d['broker_id']
        if 'buyer_name' in d:
            o.buyer_name = d['buyer_name']
        if 'currency' in d:
            o.currency = d['currency']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'promo_params' in d:
            o.promo_params = d['promo_params']
        if 'subject' in d:
            o.subject = d['subject']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


