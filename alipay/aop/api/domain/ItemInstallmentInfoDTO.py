#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemInstallmentInfoDTO(object):

    def __init__(self):
        self._period_max_price = None
        self._period_num = None
        self._period_price = None

    @property
    def period_max_price(self):
        return self._period_max_price

    @period_max_price.setter
    def period_max_price(self, value):
        self._period_max_price = value
    @property
    def period_num(self):
        return self._period_num

    @period_num.setter
    def period_num(self, value):
        self._period_num = value
    @property
    def period_price(self):
        return self._period_price

    @period_price.setter
    def period_price(self, value):
        self._period_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.period_max_price:
            if hasattr(self.period_max_price, 'to_alipay_dict'):
                params['period_max_price'] = self.period_max_price.to_alipay_dict()
            else:
                params['period_max_price'] = self.period_max_price
        if self.period_num:
            if hasattr(self.period_num, 'to_alipay_dict'):
                params['period_num'] = self.period_num.to_alipay_dict()
            else:
                params['period_num'] = self.period_num
        if self.period_price:
            if hasattr(self.period_price, 'to_alipay_dict'):
                params['period_price'] = self.period_price.to_alipay_dict()
            else:
                params['period_price'] = self.period_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemInstallmentInfoDTO()
        if 'period_max_price' in d:
            o.period_max_price = d['period_max_price']
        if 'period_num' in d:
            o.period_num = d['period_num']
        if 'period_price' in d:
            o.period_price = d['period_price']
        return o


