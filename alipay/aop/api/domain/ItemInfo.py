#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemInfo(object):

    def __init__(self):
        self._item_ids = None
        self._item_imgs = None
        self._item_link = None
        self._item_name = None
        self._item_text = None
        self._max_discount_num = None
        self._min_consume_num = None
        self._original_price = None
        self._sku_min_consume = None
        self._total_max_discount_num = None

    @property
    def item_ids(self):
        return self._item_ids

    @item_ids.setter
    def item_ids(self, value):
        if isinstance(value, list):
            self._item_ids = list()
            for i in value:
                self._item_ids.append(i)
    @property
    def item_imgs(self):
        return self._item_imgs

    @item_imgs.setter
    def item_imgs(self, value):
        if isinstance(value, list):
            self._item_imgs = list()
            for i in value:
                self._item_imgs.append(i)
    @property
    def item_link(self):
        return self._item_link

    @item_link.setter
    def item_link(self, value):
        self._item_link = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_text(self):
        return self._item_text

    @item_text.setter
    def item_text(self, value):
        self._item_text = value
    @property
    def max_discount_num(self):
        return self._max_discount_num

    @max_discount_num.setter
    def max_discount_num(self, value):
        self._max_discount_num = value
    @property
    def min_consume_num(self):
        return self._min_consume_num

    @min_consume_num.setter
    def min_consume_num(self, value):
        self._min_consume_num = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def sku_min_consume(self):
        return self._sku_min_consume

    @sku_min_consume.setter
    def sku_min_consume(self, value):
        self._sku_min_consume = value
    @property
    def total_max_discount_num(self):
        return self._total_max_discount_num

    @total_max_discount_num.setter
    def total_max_discount_num(self, value):
        self._total_max_discount_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_ids:
            if isinstance(self.item_ids, list):
                for i in range(0, len(self.item_ids)):
                    element = self.item_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_ids[i] = element.to_alipay_dict()
            if hasattr(self.item_ids, 'to_alipay_dict'):
                params['item_ids'] = self.item_ids.to_alipay_dict()
            else:
                params['item_ids'] = self.item_ids
        if self.item_imgs:
            if isinstance(self.item_imgs, list):
                for i in range(0, len(self.item_imgs)):
                    element = self.item_imgs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_imgs[i] = element.to_alipay_dict()
            if hasattr(self.item_imgs, 'to_alipay_dict'):
                params['item_imgs'] = self.item_imgs.to_alipay_dict()
            else:
                params['item_imgs'] = self.item_imgs
        if self.item_link:
            if hasattr(self.item_link, 'to_alipay_dict'):
                params['item_link'] = self.item_link.to_alipay_dict()
            else:
                params['item_link'] = self.item_link
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_text:
            if hasattr(self.item_text, 'to_alipay_dict'):
                params['item_text'] = self.item_text.to_alipay_dict()
            else:
                params['item_text'] = self.item_text
        if self.max_discount_num:
            if hasattr(self.max_discount_num, 'to_alipay_dict'):
                params['max_discount_num'] = self.max_discount_num.to_alipay_dict()
            else:
                params['max_discount_num'] = self.max_discount_num
        if self.min_consume_num:
            if hasattr(self.min_consume_num, 'to_alipay_dict'):
                params['min_consume_num'] = self.min_consume_num.to_alipay_dict()
            else:
                params['min_consume_num'] = self.min_consume_num
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.sku_min_consume:
            if hasattr(self.sku_min_consume, 'to_alipay_dict'):
                params['sku_min_consume'] = self.sku_min_consume.to_alipay_dict()
            else:
                params['sku_min_consume'] = self.sku_min_consume
        if self.total_max_discount_num:
            if hasattr(self.total_max_discount_num, 'to_alipay_dict'):
                params['total_max_discount_num'] = self.total_max_discount_num.to_alipay_dict()
            else:
                params['total_max_discount_num'] = self.total_max_discount_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemInfo()
        if 'item_ids' in d:
            o.item_ids = d['item_ids']
        if 'item_imgs' in d:
            o.item_imgs = d['item_imgs']
        if 'item_link' in d:
            o.item_link = d['item_link']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_text' in d:
            o.item_text = d['item_text']
        if 'max_discount_num' in d:
            o.max_discount_num = d['max_discount_num']
        if 'min_consume_num' in d:
            o.min_consume_num = d['min_consume_num']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'sku_min_consume' in d:
            o.sku_min_consume = d['sku_min_consume']
        if 'total_max_discount_num' in d:
            o.total_max_discount_num = d['total_max_discount_num']
        return o


