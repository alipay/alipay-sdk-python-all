#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReceiptQuoteInfo(object):

    def __init__(self):
        self._base_currency = None
        self._base_currency_unit = None
        self._expiry_time = None
        self._fx_rate = None
        self._quote_id = None
        self._source_currency = None
        self._start_time = None
        self._target_currency = None

    @property
    def base_currency(self):
        return self._base_currency

    @base_currency.setter
    def base_currency(self, value):
        self._base_currency = value
    @property
    def base_currency_unit(self):
        return self._base_currency_unit

    @base_currency_unit.setter
    def base_currency_unit(self, value):
        self._base_currency_unit = value
    @property
    def expiry_time(self):
        return self._expiry_time

    @expiry_time.setter
    def expiry_time(self, value):
        self._expiry_time = value
    @property
    def fx_rate(self):
        return self._fx_rate

    @fx_rate.setter
    def fx_rate(self, value):
        self._fx_rate = value
    @property
    def quote_id(self):
        return self._quote_id

    @quote_id.setter
    def quote_id(self, value):
        self._quote_id = value
    @property
    def source_currency(self):
        return self._source_currency

    @source_currency.setter
    def source_currency(self, value):
        self._source_currency = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def target_currency(self):
        return self._target_currency

    @target_currency.setter
    def target_currency(self, value):
        self._target_currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_currency:
            if hasattr(self.base_currency, 'to_alipay_dict'):
                params['base_currency'] = self.base_currency.to_alipay_dict()
            else:
                params['base_currency'] = self.base_currency
        if self.base_currency_unit:
            if hasattr(self.base_currency_unit, 'to_alipay_dict'):
                params['base_currency_unit'] = self.base_currency_unit.to_alipay_dict()
            else:
                params['base_currency_unit'] = self.base_currency_unit
        if self.expiry_time:
            if hasattr(self.expiry_time, 'to_alipay_dict'):
                params['expiry_time'] = self.expiry_time.to_alipay_dict()
            else:
                params['expiry_time'] = self.expiry_time
        if self.fx_rate:
            if hasattr(self.fx_rate, 'to_alipay_dict'):
                params['fx_rate'] = self.fx_rate.to_alipay_dict()
            else:
                params['fx_rate'] = self.fx_rate
        if self.quote_id:
            if hasattr(self.quote_id, 'to_alipay_dict'):
                params['quote_id'] = self.quote_id.to_alipay_dict()
            else:
                params['quote_id'] = self.quote_id
        if self.source_currency:
            if hasattr(self.source_currency, 'to_alipay_dict'):
                params['source_currency'] = self.source_currency.to_alipay_dict()
            else:
                params['source_currency'] = self.source_currency
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
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
        o = ReceiptQuoteInfo()
        if 'base_currency' in d:
            o.base_currency = d['base_currency']
        if 'base_currency_unit' in d:
            o.base_currency_unit = d['base_currency_unit']
        if 'expiry_time' in d:
            o.expiry_time = d['expiry_time']
        if 'fx_rate' in d:
            o.fx_rate = d['fx_rate']
        if 'quote_id' in d:
            o.quote_id = d['quote_id']
        if 'source_currency' in d:
            o.source_currency = d['source_currency']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'target_currency' in d:
            o.target_currency = d['target_currency']
        return o


