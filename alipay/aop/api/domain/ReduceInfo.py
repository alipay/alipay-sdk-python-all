#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReduceInfo(object):

    def __init__(self):
        self._brand_name = None
        self._consume_amt = None
        self._consume_store_name = None
        self._payment_time = None
        self._promo_amt = None
        self._user_name = None

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def consume_amt(self):
        return self._consume_amt

    @consume_amt.setter
    def consume_amt(self, value):
        self._consume_amt = value
    @property
    def consume_store_name(self):
        return self._consume_store_name

    @consume_store_name.setter
    def consume_store_name(self, value):
        self._consume_store_name = value
    @property
    def payment_time(self):
        return self._payment_time

    @payment_time.setter
    def payment_time(self, value):
        self._payment_time = value
    @property
    def promo_amt(self):
        return self._promo_amt

    @promo_amt.setter
    def promo_amt(self, value):
        self._promo_amt = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.consume_amt:
            if hasattr(self.consume_amt, 'to_alipay_dict'):
                params['consume_amt'] = self.consume_amt.to_alipay_dict()
            else:
                params['consume_amt'] = self.consume_amt
        if self.consume_store_name:
            if hasattr(self.consume_store_name, 'to_alipay_dict'):
                params['consume_store_name'] = self.consume_store_name.to_alipay_dict()
            else:
                params['consume_store_name'] = self.consume_store_name
        if self.payment_time:
            if hasattr(self.payment_time, 'to_alipay_dict'):
                params['payment_time'] = self.payment_time.to_alipay_dict()
            else:
                params['payment_time'] = self.payment_time
        if self.promo_amt:
            if hasattr(self.promo_amt, 'to_alipay_dict'):
                params['promo_amt'] = self.promo_amt.to_alipay_dict()
            else:
                params['promo_amt'] = self.promo_amt
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReduceInfo()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'consume_amt' in d:
            o.consume_amt = d['consume_amt']
        if 'consume_store_name' in d:
            o.consume_store_name = d['consume_store_name']
        if 'payment_time' in d:
            o.payment_time = d['payment_time']
        if 'promo_amt' in d:
            o.promo_amt = d['promo_amt']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


