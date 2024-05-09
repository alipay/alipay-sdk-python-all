#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemCalendarPriceVO import ItemCalendarPriceVO
from alipay.aop.api.domain.SkuCalendarPriceListVO import SkuCalendarPriceListVO


class AlipayOpenAppLocalitemCalendarpriceSaveModel(object):

    def __init__(self):
        self._calendar_prices = None
        self._item_id = None
        self._out_item_id = None
        self._sku_calendar_prices = None

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
    def sku_calendar_prices(self):
        return self._sku_calendar_prices

    @sku_calendar_prices.setter
    def sku_calendar_prices(self, value):
        if isinstance(value, list):
            self._sku_calendar_prices = list()
            for i in value:
                if isinstance(i, SkuCalendarPriceListVO):
                    self._sku_calendar_prices.append(i)
                else:
                    self._sku_calendar_prices.append(SkuCalendarPriceListVO.from_alipay_dict(i))


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
        if self.sku_calendar_prices:
            if isinstance(self.sku_calendar_prices, list):
                for i in range(0, len(self.sku_calendar_prices)):
                    element = self.sku_calendar_prices[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_calendar_prices[i] = element.to_alipay_dict()
            if hasattr(self.sku_calendar_prices, 'to_alipay_dict'):
                params['sku_calendar_prices'] = self.sku_calendar_prices.to_alipay_dict()
            else:
                params['sku_calendar_prices'] = self.sku_calendar_prices
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppLocalitemCalendarpriceSaveModel()
        if 'calendar_prices' in d:
            o.calendar_prices = d['calendar_prices']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'sku_calendar_prices' in d:
            o.sku_calendar_prices = d['sku_calendar_prices']
        return o


