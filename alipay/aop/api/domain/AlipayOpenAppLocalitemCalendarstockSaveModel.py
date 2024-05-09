#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemCalendarStockVO import ItemCalendarStockVO
from alipay.aop.api.domain.SkuCalendarStockListVO import SkuCalendarStockListVO


class AlipayOpenAppLocalitemCalendarstockSaveModel(object):

    def __init__(self):
        self._calendar_stocks = None
        self._item_id = None
        self._out_item_id = None
        self._sku_calendar_stocks = None

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
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def sku_calendar_stocks(self):
        return self._sku_calendar_stocks

    @sku_calendar_stocks.setter
    def sku_calendar_stocks(self, value):
        if isinstance(value, list):
            self._sku_calendar_stocks = list()
            for i in value:
                if isinstance(i, SkuCalendarStockListVO):
                    self._sku_calendar_stocks.append(i)
                else:
                    self._sku_calendar_stocks.append(SkuCalendarStockListVO.from_alipay_dict(i))


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
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.sku_calendar_stocks:
            if isinstance(self.sku_calendar_stocks, list):
                for i in range(0, len(self.sku_calendar_stocks)):
                    element = self.sku_calendar_stocks[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_calendar_stocks[i] = element.to_alipay_dict()
            if hasattr(self.sku_calendar_stocks, 'to_alipay_dict'):
                params['sku_calendar_stocks'] = self.sku_calendar_stocks.to_alipay_dict()
            else:
                params['sku_calendar_stocks'] = self.sku_calendar_stocks
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppLocalitemCalendarstockSaveModel()
        if 'calendar_stocks' in d:
            o.calendar_stocks = d['calendar_stocks']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'sku_calendar_stocks' in d:
            o.sku_calendar_stocks = d['sku_calendar_stocks']
        return o


