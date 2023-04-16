#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AosGoodItem import AosGoodItem


class ShopItem(object):

    def __init__(self):
        self._goods = None
        self._score = None
        self._shop_id = None
        self._shop_name = None
        self._shop_url = None
        self._trace_id = None

    @property
    def goods(self):
        return self._goods

    @goods.setter
    def goods(self, value):
        if isinstance(value, list):
            self._goods = list()
            for i in value:
                if isinstance(i, AosGoodItem):
                    self._goods.append(i)
                else:
                    self._goods.append(AosGoodItem.from_alipay_dict(i))
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_url(self):
        return self._shop_url

    @shop_url.setter
    def shop_url(self, value):
        self._shop_url = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods:
            if isinstance(self.goods, list):
                for i in range(0, len(self.goods)):
                    element = self.goods[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods[i] = element.to_alipay_dict()
            if hasattr(self.goods, 'to_alipay_dict'):
                params['goods'] = self.goods.to_alipay_dict()
            else:
                params['goods'] = self.goods
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_url:
            if hasattr(self.shop_url, 'to_alipay_dict'):
                params['shop_url'] = self.shop_url.to_alipay_dict()
            else:
                params['shop_url'] = self.shop_url
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopItem()
        if 'goods' in d:
            o.goods = d['goods']
        if 'score' in d:
            o.score = d['score']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_url' in d:
            o.shop_url = d['shop_url']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        return o


