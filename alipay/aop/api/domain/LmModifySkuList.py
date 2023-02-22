#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LmModifySkuList(object):

    def __init__(self):
        self._can_sell = None
        self._points = None
        self._points_amount = None
        self._price_cent = None
        self._sku_id = None

    @property
    def can_sell(self):
        return self._can_sell

    @can_sell.setter
    def can_sell(self, value):
        self._can_sell = value
    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points = value
    @property
    def points_amount(self):
        return self._points_amount

    @points_amount.setter
    def points_amount(self, value):
        self._points_amount = value
    @property
    def price_cent(self):
        return self._price_cent

    @price_cent.setter
    def price_cent(self, value):
        self._price_cent = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_sell:
            if hasattr(self.can_sell, 'to_alipay_dict'):
                params['can_sell'] = self.can_sell.to_alipay_dict()
            else:
                params['can_sell'] = self.can_sell
        if self.points:
            if hasattr(self.points, 'to_alipay_dict'):
                params['points'] = self.points.to_alipay_dict()
            else:
                params['points'] = self.points
        if self.points_amount:
            if hasattr(self.points_amount, 'to_alipay_dict'):
                params['points_amount'] = self.points_amount.to_alipay_dict()
            else:
                params['points_amount'] = self.points_amount
        if self.price_cent:
            if hasattr(self.price_cent, 'to_alipay_dict'):
                params['price_cent'] = self.price_cent.to_alipay_dict()
            else:
                params['price_cent'] = self.price_cent
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LmModifySkuList()
        if 'can_sell' in d:
            o.can_sell = d['can_sell']
        if 'points' in d:
            o.points = d['points']
        if 'points_amount' in d:
            o.points_amount = d['points_amount']
        if 'price_cent' in d:
            o.price_cent = d['price_cent']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


