#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RemitTransferQuotew(object):

    def __init__(self):
        self._base_currency = None
        self._quote_currency_pair = None
        self._quote_expiry_time = None
        self._quote_id = None
        self._quote_price = None
        self._quote_start_time = None
        self._quote_unit = None

    @property
    def base_currency(self):
        return self._base_currency

    @base_currency.setter
    def base_currency(self, value):
        self._base_currency = value
    @property
    def quote_currency_pair(self):
        return self._quote_currency_pair

    @quote_currency_pair.setter
    def quote_currency_pair(self, value):
        self._quote_currency_pair = value
    @property
    def quote_expiry_time(self):
        return self._quote_expiry_time

    @quote_expiry_time.setter
    def quote_expiry_time(self, value):
        self._quote_expiry_time = value
    @property
    def quote_id(self):
        return self._quote_id

    @quote_id.setter
    def quote_id(self, value):
        self._quote_id = value
    @property
    def quote_price(self):
        return self._quote_price

    @quote_price.setter
    def quote_price(self, value):
        self._quote_price = value
    @property
    def quote_start_time(self):
        return self._quote_start_time

    @quote_start_time.setter
    def quote_start_time(self, value):
        self._quote_start_time = value
    @property
    def quote_unit(self):
        return self._quote_unit

    @quote_unit.setter
    def quote_unit(self, value):
        self._quote_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_currency:
            if hasattr(self.base_currency, 'to_alipay_dict'):
                params['base_currency'] = self.base_currency.to_alipay_dict()
            else:
                params['base_currency'] = self.base_currency
        if self.quote_currency_pair:
            if hasattr(self.quote_currency_pair, 'to_alipay_dict'):
                params['quote_currency_pair'] = self.quote_currency_pair.to_alipay_dict()
            else:
                params['quote_currency_pair'] = self.quote_currency_pair
        if self.quote_expiry_time:
            if hasattr(self.quote_expiry_time, 'to_alipay_dict'):
                params['quote_expiry_time'] = self.quote_expiry_time.to_alipay_dict()
            else:
                params['quote_expiry_time'] = self.quote_expiry_time
        if self.quote_id:
            if hasattr(self.quote_id, 'to_alipay_dict'):
                params['quote_id'] = self.quote_id.to_alipay_dict()
            else:
                params['quote_id'] = self.quote_id
        if self.quote_price:
            if hasattr(self.quote_price, 'to_alipay_dict'):
                params['quote_price'] = self.quote_price.to_alipay_dict()
            else:
                params['quote_price'] = self.quote_price
        if self.quote_start_time:
            if hasattr(self.quote_start_time, 'to_alipay_dict'):
                params['quote_start_time'] = self.quote_start_time.to_alipay_dict()
            else:
                params['quote_start_time'] = self.quote_start_time
        if self.quote_unit:
            if hasattr(self.quote_unit, 'to_alipay_dict'):
                params['quote_unit'] = self.quote_unit.to_alipay_dict()
            else:
                params['quote_unit'] = self.quote_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RemitTransferQuotew()
        if 'base_currency' in d:
            o.base_currency = d['base_currency']
        if 'quote_currency_pair' in d:
            o.quote_currency_pair = d['quote_currency_pair']
        if 'quote_expiry_time' in d:
            o.quote_expiry_time = d['quote_expiry_time']
        if 'quote_id' in d:
            o.quote_id = d['quote_id']
        if 'quote_price' in d:
            o.quote_price = d['quote_price']
        if 'quote_start_time' in d:
            o.quote_start_time = d['quote_start_time']
        if 'quote_unit' in d:
            o.quote_unit = d['quote_unit']
        return o


