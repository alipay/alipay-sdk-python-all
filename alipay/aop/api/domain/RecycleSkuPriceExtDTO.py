#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleSkuCustomPriceDTO import RecycleSkuCustomPriceDTO


class RecycleSkuPriceExtDTO(object):

    def __init__(self):
        self._custom_prices = None

    @property
    def custom_prices(self):
        return self._custom_prices

    @custom_prices.setter
    def custom_prices(self, value):
        if isinstance(value, list):
            self._custom_prices = list()
            for i in value:
                if isinstance(i, RecycleSkuCustomPriceDTO):
                    self._custom_prices.append(i)
                else:
                    self._custom_prices.append(RecycleSkuCustomPriceDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.custom_prices:
            if isinstance(self.custom_prices, list):
                for i in range(0, len(self.custom_prices)):
                    element = self.custom_prices[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.custom_prices[i] = element.to_alipay_dict()
            if hasattr(self.custom_prices, 'to_alipay_dict'):
                params['custom_prices'] = self.custom_prices.to_alipay_dict()
            else:
                params['custom_prices'] = self.custom_prices
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleSkuPriceExtDTO()
        if 'custom_prices' in d:
            o.custom_prices = d['custom_prices']
        return o


