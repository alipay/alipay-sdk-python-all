#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaidOuterCardCycleSellConfDTO(object):

    def __init__(self):
        self._cycle_selling_url = None
        self._cycle_type = None
        self._support_cycle_sell = None

    @property
    def cycle_selling_url(self):
        return self._cycle_selling_url

    @cycle_selling_url.setter
    def cycle_selling_url(self, value):
        self._cycle_selling_url = value
    @property
    def cycle_type(self):
        return self._cycle_type

    @cycle_type.setter
    def cycle_type(self, value):
        if isinstance(value, list):
            self._cycle_type = list()
            for i in value:
                self._cycle_type.append(i)
    @property
    def support_cycle_sell(self):
        return self._support_cycle_sell

    @support_cycle_sell.setter
    def support_cycle_sell(self, value):
        self._support_cycle_sell = value


    def to_alipay_dict(self):
        params = dict()
        if self.cycle_selling_url:
            if hasattr(self.cycle_selling_url, 'to_alipay_dict'):
                params['cycle_selling_url'] = self.cycle_selling_url.to_alipay_dict()
            else:
                params['cycle_selling_url'] = self.cycle_selling_url
        if self.cycle_type:
            if isinstance(self.cycle_type, list):
                for i in range(0, len(self.cycle_type)):
                    element = self.cycle_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cycle_type[i] = element.to_alipay_dict()
            if hasattr(self.cycle_type, 'to_alipay_dict'):
                params['cycle_type'] = self.cycle_type.to_alipay_dict()
            else:
                params['cycle_type'] = self.cycle_type
        if self.support_cycle_sell:
            if hasattr(self.support_cycle_sell, 'to_alipay_dict'):
                params['support_cycle_sell'] = self.support_cycle_sell.to_alipay_dict()
            else:
                params['support_cycle_sell'] = self.support_cycle_sell
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaidOuterCardCycleSellConfDTO()
        if 'cycle_selling_url' in d:
            o.cycle_selling_url = d['cycle_selling_url']
        if 'cycle_type' in d:
            o.cycle_type = d['cycle_type']
        if 'support_cycle_sell' in d:
            o.support_cycle_sell = d['support_cycle_sell']
        return o


