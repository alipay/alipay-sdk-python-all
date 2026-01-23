#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubsidyCurrency import SubsidyCurrency


class SubsidyMoney(object):

    def __init__(self):
        self._cent = None
        self._currency = None

    @property
    def cent(self):
        return self._cent

    @cent.setter
    def cent(self, value):
        self._cent = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        if isinstance(value, SubsidyCurrency):
            self._currency = value
        else:
            self._currency = SubsidyCurrency.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.cent:
            if hasattr(self.cent, 'to_alipay_dict'):
                params['cent'] = self.cent.to_alipay_dict()
            else:
                params['cent'] = self.cent
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubsidyMoney()
        if 'cent' in d:
            o.cent = d['cent']
        if 'currency' in d:
            o.currency = d['currency']
        return o


