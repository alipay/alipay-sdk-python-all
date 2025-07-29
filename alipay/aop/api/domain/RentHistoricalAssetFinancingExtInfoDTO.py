#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentHistoricalAssetFinancingExtInfoDTO(object):

    def __init__(self):
        self._paid_period = None
        self._paid_price = None
        self._start_financing_period = None
        self._unpaid_period = None
        self._unpaid_price = None

    @property
    def paid_period(self):
        return self._paid_period

    @paid_period.setter
    def paid_period(self, value):
        self._paid_period = value
    @property
    def paid_price(self):
        return self._paid_price

    @paid_price.setter
    def paid_price(self, value):
        self._paid_price = value
    @property
    def start_financing_period(self):
        return self._start_financing_period

    @start_financing_period.setter
    def start_financing_period(self, value):
        self._start_financing_period = value
    @property
    def unpaid_period(self):
        return self._unpaid_period

    @unpaid_period.setter
    def unpaid_period(self, value):
        self._unpaid_period = value
    @property
    def unpaid_price(self):
        return self._unpaid_price

    @unpaid_price.setter
    def unpaid_price(self, value):
        self._unpaid_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.paid_period:
            if hasattr(self.paid_period, 'to_alipay_dict'):
                params['paid_period'] = self.paid_period.to_alipay_dict()
            else:
                params['paid_period'] = self.paid_period
        if self.paid_price:
            if hasattr(self.paid_price, 'to_alipay_dict'):
                params['paid_price'] = self.paid_price.to_alipay_dict()
            else:
                params['paid_price'] = self.paid_price
        if self.start_financing_period:
            if hasattr(self.start_financing_period, 'to_alipay_dict'):
                params['start_financing_period'] = self.start_financing_period.to_alipay_dict()
            else:
                params['start_financing_period'] = self.start_financing_period
        if self.unpaid_period:
            if hasattr(self.unpaid_period, 'to_alipay_dict'):
                params['unpaid_period'] = self.unpaid_period.to_alipay_dict()
            else:
                params['unpaid_period'] = self.unpaid_period
        if self.unpaid_price:
            if hasattr(self.unpaid_price, 'to_alipay_dict'):
                params['unpaid_price'] = self.unpaid_price.to_alipay_dict()
            else:
                params['unpaid_price'] = self.unpaid_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentHistoricalAssetFinancingExtInfoDTO()
        if 'paid_period' in d:
            o.paid_period = d['paid_period']
        if 'paid_price' in d:
            o.paid_price = d['paid_price']
        if 'start_financing_period' in d:
            o.start_financing_period = d['start_financing_period']
        if 'unpaid_period' in d:
            o.unpaid_period = d['unpaid_period']
        if 'unpaid_price' in d:
            o.unpaid_price = d['unpaid_price']
        return o


