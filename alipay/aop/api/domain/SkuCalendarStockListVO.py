#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemCalendarStockVO import ItemCalendarStockVO


class SkuCalendarStockListVO(object):

    def __init__(self):
        self._calendar_stocks = None
        self._out_sku_id = None

    @property
    def calendar_stocks(self):
        return self._calendar_stocks

    @calendar_stocks.setter
    def calendar_stocks(self, value):
        if isinstance(value, list):
            self._calendar_stocks = list()
            for i in value:
                if isinstance(i, ItemCalendarStockVO):
                    self._calendar_stocks.append(i)
                else:
                    self._calendar_stocks.append(ItemCalendarStockVO.from_alipay_dict(i))
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.calendar_stocks:
            if isinstance(self.calendar_stocks, list):
                for i in range(0, len(self.calendar_stocks)):
                    element = self.calendar_stocks[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.calendar_stocks[i] = element.to_alipay_dict()
            if hasattr(self.calendar_stocks, 'to_alipay_dict'):
                params['calendar_stocks'] = self.calendar_stocks.to_alipay_dict()
            else:
                params['calendar_stocks'] = self.calendar_stocks
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
        o = SkuCalendarStockListVO()
        if 'calendar_stocks' in d:
            o.calendar_stocks = d['calendar_stocks']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        return o


