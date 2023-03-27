#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemQueryInfo(object):

    def __init__(self):
        self._brand = None
        self._buy_url = None
        self._currency_type = None
        self._goods_id = None
        self._goods_name = None
        self._lanch_time = None
        self._monetary_unit = None
        self._price = None
        self._promo_pic_url_list = None
        self._score = None
        self._tags = None

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
    @property
    def buy_url(self):
        return self._buy_url

    @buy_url.setter
    def buy_url(self, value):
        self._buy_url = value
    @property
    def currency_type(self):
        return self._currency_type

    @currency_type.setter
    def currency_type(self, value):
        self._currency_type = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def lanch_time(self):
        return self._lanch_time

    @lanch_time.setter
    def lanch_time(self, value):
        self._lanch_time = value
    @property
    def monetary_unit(self):
        return self._monetary_unit

    @monetary_unit.setter
    def monetary_unit(self, value):
        self._monetary_unit = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def promo_pic_url_list(self):
        return self._promo_pic_url_list

    @promo_pic_url_list.setter
    def promo_pic_url_list(self, value):
        if isinstance(value, list):
            self._promo_pic_url_list = list()
            for i in value:
                self._promo_pic_url_list.append(i)
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand:
            if hasattr(self.brand, 'to_alipay_dict'):
                params['brand'] = self.brand.to_alipay_dict()
            else:
                params['brand'] = self.brand
        if self.buy_url:
            if hasattr(self.buy_url, 'to_alipay_dict'):
                params['buy_url'] = self.buy_url.to_alipay_dict()
            else:
                params['buy_url'] = self.buy_url
        if self.currency_type:
            if hasattr(self.currency_type, 'to_alipay_dict'):
                params['currency_type'] = self.currency_type.to_alipay_dict()
            else:
                params['currency_type'] = self.currency_type
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.lanch_time:
            if hasattr(self.lanch_time, 'to_alipay_dict'):
                params['lanch_time'] = self.lanch_time.to_alipay_dict()
            else:
                params['lanch_time'] = self.lanch_time
        if self.monetary_unit:
            if hasattr(self.monetary_unit, 'to_alipay_dict'):
                params['monetary_unit'] = self.monetary_unit.to_alipay_dict()
            else:
                params['monetary_unit'] = self.monetary_unit
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.promo_pic_url_list:
            if isinstance(self.promo_pic_url_list, list):
                for i in range(0, len(self.promo_pic_url_list)):
                    element = self.promo_pic_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promo_pic_url_list[i] = element.to_alipay_dict()
            if hasattr(self.promo_pic_url_list, 'to_alipay_dict'):
                params['promo_pic_url_list'] = self.promo_pic_url_list.to_alipay_dict()
            else:
                params['promo_pic_url_list'] = self.promo_pic_url_list
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.tags:
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemQueryInfo()
        if 'brand' in d:
            o.brand = d['brand']
        if 'buy_url' in d:
            o.buy_url = d['buy_url']
        if 'currency_type' in d:
            o.currency_type = d['currency_type']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'lanch_time' in d:
            o.lanch_time = d['lanch_time']
        if 'monetary_unit' in d:
            o.monetary_unit = d['monetary_unit']
        if 'price' in d:
            o.price = d['price']
        if 'promo_pic_url_list' in d:
            o.promo_pic_url_list = d['promo_pic_url_list']
        if 'score' in d:
            o.score = d['score']
        if 'tags' in d:
            o.tags = d['tags']
        return o


