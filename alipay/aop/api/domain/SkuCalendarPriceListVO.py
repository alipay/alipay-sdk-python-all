#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemCalendarPriceVO import ItemCalendarPriceVO


class SkuCalendarPriceListVO(object):

    def __init__(self):
        self._calendar_prices = None
        self._out_sku_id = None

    @property
    def calendar_prices(self):
        return self._calendar_prices

    @calendar_prices.setter
    def calendar_prices(self, value):
        if isinstance(value, list):
            self._calendar_prices = list()
            for i in value:
                if isinstance(i, ItemCalendarPriceVO):
                    self._calendar_prices.append(i)
                else:
                    self._calendar_prices.append(ItemCalendarPriceVO.from_alipay_dict(i))
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.calendar_prices:
            if isinstance(self.calendar_prices, list):
                for i in range(0, len(self.calendar_prices)):
                    element = self.calendar_prices[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.calendar_prices[i] = element.to_alipay_dict()
            if hasattr(self.calendar_prices, 'to_alipay_dict'):
                params['calendar_prices'] = self.calendar_prices.to_alipay_dict()
            else:
                params['calendar_prices'] = self.calendar_prices
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SkuCalendarPriceListVO()
        if 'calendar_prices' in d:
            o.calendar_prices = d['calendar_prices']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        return o


