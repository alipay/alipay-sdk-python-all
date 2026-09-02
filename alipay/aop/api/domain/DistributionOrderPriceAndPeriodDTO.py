#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DistributionOrderPriceAndPeriodDTO(object):

    def __init__(self):
        self._deposit_price = None
        self._freight = None
        self._rent_end_time = None
        self._rent_price = None
        self._rent_start_time = None

    @property
    def deposit_price(self):
        return self._deposit_price

    @deposit_price.setter
    def deposit_price(self, value):
        self._deposit_price = value
    @property
    def freight(self):
        return self._freight

    @freight.setter
    def freight(self, value):
        self._freight = value
    @property
    def rent_end_time(self):
        return self._rent_end_time

    @rent_end_time.setter
    def rent_end_time(self, value):
        self._rent_end_time = value
    @property
    def rent_price(self):
        return self._rent_price

    @rent_price.setter
    def rent_price(self, value):
        self._rent_price = value
    @property
    def rent_start_time(self):
        return self._rent_start_time

    @rent_start_time.setter
    def rent_start_time(self, value):
        self._rent_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.deposit_price:
            if hasattr(self.deposit_price, 'to_alipay_dict'):
                params['deposit_price'] = self.deposit_price.to_alipay_dict()
            else:
                params['deposit_price'] = self.deposit_price
        if self.freight:
            if hasattr(self.freight, 'to_alipay_dict'):
                params['freight'] = self.freight.to_alipay_dict()
            else:
                params['freight'] = self.freight
        if self.rent_end_time:
            if hasattr(self.rent_end_time, 'to_alipay_dict'):
                params['rent_end_time'] = self.rent_end_time.to_alipay_dict()
            else:
                params['rent_end_time'] = self.rent_end_time
        if self.rent_price:
            if hasattr(self.rent_price, 'to_alipay_dict'):
                params['rent_price'] = self.rent_price.to_alipay_dict()
            else:
                params['rent_price'] = self.rent_price
        if self.rent_start_time:
            if hasattr(self.rent_start_time, 'to_alipay_dict'):
                params['rent_start_time'] = self.rent_start_time.to_alipay_dict()
            else:
                params['rent_start_time'] = self.rent_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DistributionOrderPriceAndPeriodDTO()
        if 'deposit_price' in d:
            o.deposit_price = d['deposit_price']
        if 'freight' in d:
            o.freight = d['freight']
        if 'rent_end_time' in d:
            o.rent_end_time = d['rent_end_time']
        if 'rent_price' in d:
            o.rent_price = d['rent_price']
        if 'rent_start_time' in d:
            o.rent_start_time = d['rent_start_time']
        return o


