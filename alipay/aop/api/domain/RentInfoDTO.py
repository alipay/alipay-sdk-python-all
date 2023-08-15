#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentInfoDTO(object):

    def __init__(self):
        self._buyout_price = None
        self._initial_rent_price = None
        self._period_num = None
        self._period_real_rent_price = None

    @property
    def buyout_price(self):
        return self._buyout_price

    @buyout_price.setter
    def buyout_price(self, value):
        self._buyout_price = value
    @property
    def initial_rent_price(self):
        return self._initial_rent_price

    @initial_rent_price.setter
    def initial_rent_price(self, value):
        self._initial_rent_price = value
    @property
    def period_num(self):
        return self._period_num

    @period_num.setter
    def period_num(self, value):
        self._period_num = value
    @property
    def period_real_rent_price(self):
        return self._period_real_rent_price

    @period_real_rent_price.setter
    def period_real_rent_price(self, value):
        self._period_real_rent_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyout_price:
            if hasattr(self.buyout_price, 'to_alipay_dict'):
                params['buyout_price'] = self.buyout_price.to_alipay_dict()
            else:
                params['buyout_price'] = self.buyout_price
        if self.initial_rent_price:
            if hasattr(self.initial_rent_price, 'to_alipay_dict'):
                params['initial_rent_price'] = self.initial_rent_price.to_alipay_dict()
            else:
                params['initial_rent_price'] = self.initial_rent_price
        if self.period_num:
            if hasattr(self.period_num, 'to_alipay_dict'):
                params['period_num'] = self.period_num.to_alipay_dict()
            else:
                params['period_num'] = self.period_num
        if self.period_real_rent_price:
            if hasattr(self.period_real_rent_price, 'to_alipay_dict'):
                params['period_real_rent_price'] = self.period_real_rent_price.to_alipay_dict()
            else:
                params['period_real_rent_price'] = self.period_real_rent_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentInfoDTO()
        if 'buyout_price' in d:
            o.buyout_price = d['buyout_price']
        if 'initial_rent_price' in d:
            o.initial_rent_price = d['initial_rent_price']
        if 'period_num' in d:
            o.period_num = d['period_num']
        if 'period_real_rent_price' in d:
            o.period_real_rent_price = d['period_real_rent_price']
        return o


