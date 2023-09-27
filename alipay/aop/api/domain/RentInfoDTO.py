#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentInfoDTO(object):

    def __init__(self):
        self._addon_period_num = None
        self._addon_real_rent_price = None
        self._buyout_price = None
        self._finish_real_rent_price = None
        self._initial_rent_price = None
        self._period_num = None
        self._period_real_rent_price = None

    @property
    def addon_period_num(self):
        return self._addon_period_num

    @addon_period_num.setter
    def addon_period_num(self, value):
        self._addon_period_num = value
    @property
    def addon_real_rent_price(self):
        return self._addon_real_rent_price

    @addon_real_rent_price.setter
    def addon_real_rent_price(self, value):
        self._addon_real_rent_price = value
    @property
    def buyout_price(self):
        return self._buyout_price

    @buyout_price.setter
    def buyout_price(self, value):
        self._buyout_price = value
    @property
    def finish_real_rent_price(self):
        return self._finish_real_rent_price

    @finish_real_rent_price.setter
    def finish_real_rent_price(self, value):
        self._finish_real_rent_price = value
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
        if self.addon_period_num:
            if hasattr(self.addon_period_num, 'to_alipay_dict'):
                params['addon_period_num'] = self.addon_period_num.to_alipay_dict()
            else:
                params['addon_period_num'] = self.addon_period_num
        if self.addon_real_rent_price:
            if hasattr(self.addon_real_rent_price, 'to_alipay_dict'):
                params['addon_real_rent_price'] = self.addon_real_rent_price.to_alipay_dict()
            else:
                params['addon_real_rent_price'] = self.addon_real_rent_price
        if self.buyout_price:
            if hasattr(self.buyout_price, 'to_alipay_dict'):
                params['buyout_price'] = self.buyout_price.to_alipay_dict()
            else:
                params['buyout_price'] = self.buyout_price
        if self.finish_real_rent_price:
            if hasattr(self.finish_real_rent_price, 'to_alipay_dict'):
                params['finish_real_rent_price'] = self.finish_real_rent_price.to_alipay_dict()
            else:
                params['finish_real_rent_price'] = self.finish_real_rent_price
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
        if 'addon_period_num' in d:
            o.addon_period_num = d['addon_period_num']
        if 'addon_real_rent_price' in d:
            o.addon_real_rent_price = d['addon_real_rent_price']
        if 'buyout_price' in d:
            o.buyout_price = d['buyout_price']
        if 'finish_real_rent_price' in d:
            o.finish_real_rent_price = d['finish_real_rent_price']
        if 'initial_rent_price' in d:
            o.initial_rent_price = d['initial_rent_price']
        if 'period_num' in d:
            o.period_num = d['period_num']
        if 'period_real_rent_price' in d:
            o.period_real_rent_price = d['period_real_rent_price']
        return o


