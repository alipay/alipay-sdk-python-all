#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Moneyq import Moneyq


class Promo(object):

    def __init__(self):
        self._description = None
        self._discount_amount = None
        self._discount_rate = None
        self._effective_time = None
        self._expiry_time = None
        self._promo_id = None
        self._promo_request_id = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        if isinstance(value, Moneyq):
            self._discount_amount = value
        else:
            self._discount_amount = Moneyq.from_alipay_dict(value)
    @property
    def discount_rate(self):
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, value):
        self._discount_rate = value
    @property
    def effective_time(self):
        return self._effective_time

    @effective_time.setter
    def effective_time(self, value):
        self._effective_time = value
    @property
    def expiry_time(self):
        return self._expiry_time

    @expiry_time.setter
    def expiry_time(self, value):
        self._expiry_time = value
    @property
    def promo_id(self):
        return self._promo_id

    @promo_id.setter
    def promo_id(self, value):
        self._promo_id = value
    @property
    def promo_request_id(self):
        return self._promo_request_id

    @promo_request_id.setter
    def promo_request_id(self, value):
        self._promo_request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.discount_rate:
            if hasattr(self.discount_rate, 'to_alipay_dict'):
                params['discount_rate'] = self.discount_rate.to_alipay_dict()
            else:
                params['discount_rate'] = self.discount_rate
        if self.effective_time:
            if hasattr(self.effective_time, 'to_alipay_dict'):
                params['effective_time'] = self.effective_time.to_alipay_dict()
            else:
                params['effective_time'] = self.effective_time
        if self.expiry_time:
            if hasattr(self.expiry_time, 'to_alipay_dict'):
                params['expiry_time'] = self.expiry_time.to_alipay_dict()
            else:
                params['expiry_time'] = self.expiry_time
        if self.promo_id:
            if hasattr(self.promo_id, 'to_alipay_dict'):
                params['promo_id'] = self.promo_id.to_alipay_dict()
            else:
                params['promo_id'] = self.promo_id
        if self.promo_request_id:
            if hasattr(self.promo_request_id, 'to_alipay_dict'):
                params['promo_request_id'] = self.promo_request_id.to_alipay_dict()
            else:
                params['promo_request_id'] = self.promo_request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Promo()
        if 'description' in d:
            o.description = d['description']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'discount_rate' in d:
            o.discount_rate = d['discount_rate']
        if 'effective_time' in d:
            o.effective_time = d['effective_time']
        if 'expiry_time' in d:
            o.expiry_time = d['expiry_time']
        if 'promo_id' in d:
            o.promo_id = d['promo_id']
        if 'promo_request_id' in d:
            o.promo_request_id = d['promo_request_id']
        return o


