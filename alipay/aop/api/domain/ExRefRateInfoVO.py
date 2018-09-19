#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExRefRateInfoVO(object):

    def __init__(self):
        self._currency_pair = None
        self._datum_currency = None
        self._price_type = None
        self._pub_date = None
        self._pub_time = None
        self._rate = None
        self._target_currency = None

    @property
    def currency_pair(self):
        return self._currency_pair

    @currency_pair.setter
    def currency_pair(self, value):
        self._currency_pair = value
    @property
    def datum_currency(self):
        return self._datum_currency

    @datum_currency.setter
    def datum_currency(self, value):
        self._datum_currency = value
    @property
    def price_type(self):
        return self._price_type

    @price_type.setter
    def price_type(self, value):
        self._price_type = value
    @property
    def pub_date(self):
        return self._pub_date

    @pub_date.setter
    def pub_date(self, value):
        self._pub_date = value
    @property
    def pub_time(self):
        return self._pub_time

    @pub_time.setter
    def pub_time(self, value):
        self._pub_time = value
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def target_currency(self):
        return self._target_currency

    @target_currency.setter
    def target_currency(self, value):
        self._target_currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.currency_pair:
            if hasattr(self.currency_pair, 'to_alipay_dict'):
                params['currency_pair'] = self.currency_pair.to_alipay_dict()
            else:
                params['currency_pair'] = self.currency_pair
        if self.datum_currency:
            if hasattr(self.datum_currency, 'to_alipay_dict'):
                params['datum_currency'] = self.datum_currency.to_alipay_dict()
            else:
                params['datum_currency'] = self.datum_currency
        if self.price_type:
            if hasattr(self.price_type, 'to_alipay_dict'):
                params['price_type'] = self.price_type.to_alipay_dict()
            else:
                params['price_type'] = self.price_type
        if self.pub_date:
            if hasattr(self.pub_date, 'to_alipay_dict'):
                params['pub_date'] = self.pub_date.to_alipay_dict()
            else:
                params['pub_date'] = self.pub_date
        if self.pub_time:
            if hasattr(self.pub_time, 'to_alipay_dict'):
                params['pub_time'] = self.pub_time.to_alipay_dict()
            else:
                params['pub_time'] = self.pub_time
        if self.rate:
            if hasattr(self.rate, 'to_alipay_dict'):
                params['rate'] = self.rate.to_alipay_dict()
            else:
                params['rate'] = self.rate
        if self.target_currency:
            if hasattr(self.target_currency, 'to_alipay_dict'):
                params['target_currency'] = self.target_currency.to_alipay_dict()
            else:
                params['target_currency'] = self.target_currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExRefRateInfoVO()
        if 'currency_pair' in d:
            o.currency_pair = d['currency_pair']
        if 'datum_currency' in d:
            o.datum_currency = d['datum_currency']
        if 'price_type' in d:
            o.price_type = d['price_type']
        if 'pub_date' in d:
            o.pub_date = d['pub_date']
        if 'pub_time' in d:
            o.pub_time = d['pub_time']
        if 'rate' in d:
            o.rate = d['rate']
        if 'target_currency' in d:
            o.target_currency = d['target_currency']
        return o


