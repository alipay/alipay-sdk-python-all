#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FlightPromotionInfo(object):

    def __init__(self):
        self._amount_currency = None
        self._name = None
        self._promotion_amount_cent = None
        self._type = None

    @property
    def amount_currency(self):
        return self._amount_currency

    @amount_currency.setter
    def amount_currency(self, value):
        self._amount_currency = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def promotion_amount_cent(self):
        return self._promotion_amount_cent

    @promotion_amount_cent.setter
    def promotion_amount_cent(self, value):
        self._promotion_amount_cent = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_currency:
            if hasattr(self.amount_currency, 'to_alipay_dict'):
                params['amount_currency'] = self.amount_currency.to_alipay_dict()
            else:
                params['amount_currency'] = self.amount_currency
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.promotion_amount_cent:
            if hasattr(self.promotion_amount_cent, 'to_alipay_dict'):
                params['promotion_amount_cent'] = self.promotion_amount_cent.to_alipay_dict()
            else:
                params['promotion_amount_cent'] = self.promotion_amount_cent
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FlightPromotionInfo()
        if 'amount_currency' in d:
            o.amount_currency = d['amount_currency']
        if 'name' in d:
            o.name = d['name']
        if 'promotion_amount_cent' in d:
            o.promotion_amount_cent = d['promotion_amount_cent']
        if 'type' in d:
            o.type = d['type']
        return o


