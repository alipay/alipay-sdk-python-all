#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemPrizeInfo(object):

    def __init__(self):
        self._item_can_exchange = None
        self._item_code = None
        self._item_icon_url = None
        self._item_name = None
        self._item_price = None
        self._point_amount = None

    @property
    def item_can_exchange(self):
        return self._item_can_exchange

    @item_can_exchange.setter
    def item_can_exchange(self, value):
        self._item_can_exchange = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def item_icon_url(self):
        return self._item_icon_url

    @item_icon_url.setter
    def item_icon_url(self, value):
        self._item_icon_url = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, value):
        self._item_price = value
    @property
    def point_amount(self):
        return self._point_amount

    @point_amount.setter
    def point_amount(self, value):
        self._point_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_can_exchange:
            if hasattr(self.item_can_exchange, 'to_alipay_dict'):
                params['item_can_exchange'] = self.item_can_exchange.to_alipay_dict()
            else:
                params['item_can_exchange'] = self.item_can_exchange
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.item_icon_url:
            if hasattr(self.item_icon_url, 'to_alipay_dict'):
                params['item_icon_url'] = self.item_icon_url.to_alipay_dict()
            else:
                params['item_icon_url'] = self.item_icon_url
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_price:
            if hasattr(self.item_price, 'to_alipay_dict'):
                params['item_price'] = self.item_price.to_alipay_dict()
            else:
                params['item_price'] = self.item_price
        if self.point_amount:
            if hasattr(self.point_amount, 'to_alipay_dict'):
                params['point_amount'] = self.point_amount.to_alipay_dict()
            else:
                params['point_amount'] = self.point_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemPrizeInfo()
        if 'item_can_exchange' in d:
            o.item_can_exchange = d['item_can_exchange']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'item_icon_url' in d:
            o.item_icon_url = d['item_icon_url']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_price' in d:
            o.item_price = d['item_price']
        if 'point_amount' in d:
            o.point_amount = d['point_amount']
        return o


