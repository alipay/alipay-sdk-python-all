#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HudMarketItem(object):

    def __init__(self):
        self._change_rate_text = None
        self._data_time = None
        self._item_code = None
        self._name = None
        self._price_text = None
        self._trend = None
        self._type = None

    @property
    def change_rate_text(self):
        return self._change_rate_text

    @change_rate_text.setter
    def change_rate_text(self, value):
        self._change_rate_text = value
    @property
    def data_time(self):
        return self._data_time

    @data_time.setter
    def data_time(self, value):
        self._data_time = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def price_text(self):
        return self._price_text

    @price_text.setter
    def price_text(self, value):
        self._price_text = value
    @property
    def trend(self):
        return self._trend

    @trend.setter
    def trend(self, value):
        self._trend = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.change_rate_text:
            if hasattr(self.change_rate_text, 'to_alipay_dict'):
                params['change_rate_text'] = self.change_rate_text.to_alipay_dict()
            else:
                params['change_rate_text'] = self.change_rate_text
        if self.data_time:
            if hasattr(self.data_time, 'to_alipay_dict'):
                params['data_time'] = self.data_time.to_alipay_dict()
            else:
                params['data_time'] = self.data_time
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.price_text:
            if hasattr(self.price_text, 'to_alipay_dict'):
                params['price_text'] = self.price_text.to_alipay_dict()
            else:
                params['price_text'] = self.price_text
        if self.trend:
            if hasattr(self.trend, 'to_alipay_dict'):
                params['trend'] = self.trend.to_alipay_dict()
            else:
                params['trend'] = self.trend
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HudMarketItem()
        if 'change_rate_text' in d:
            o.change_rate_text = d['change_rate_text']
        if 'data_time' in d:
            o.data_time = d['data_time']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'name' in d:
            o.name = d['name']
        if 'price_text' in d:
            o.price_text = d['price_text']
        if 'trend' in d:
            o.trend = d['trend']
        if 'type' in d:
            o.type = d['type']
        return o


