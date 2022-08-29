#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Singltem(object):

    def __init__(self):
        self._biz_item_id = None
        self._brand = None
        self._gmt_end = None
        self._gmt_start = None
        self._item_name = None
        self._item_redirect_url = None
        self._item_url = None
        self._original_price = None
        self._partner_id = None
        self._price = None
        self._remain_stock = None
        self._total_stock = None

    @property
    def biz_item_id(self):
        return self._biz_item_id

    @biz_item_id.setter
    def biz_item_id(self, value):
        self._biz_item_id = value
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_redirect_url(self):
        return self._item_redirect_url

    @item_redirect_url.setter
    def item_redirect_url(self, value):
        self._item_redirect_url = value
    @property
    def item_url(self):
        return self._item_url

    @item_url.setter
    def item_url(self, value):
        self._item_url = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def remain_stock(self):
        return self._remain_stock

    @remain_stock.setter
    def remain_stock(self, value):
        self._remain_stock = value
    @property
    def total_stock(self):
        return self._total_stock

    @total_stock.setter
    def total_stock(self, value):
        self._total_stock = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_item_id:
            if hasattr(self.biz_item_id, 'to_alipay_dict'):
                params['biz_item_id'] = self.biz_item_id.to_alipay_dict()
            else:
                params['biz_item_id'] = self.biz_item_id
        if self.brand:
            if hasattr(self.brand, 'to_alipay_dict'):
                params['brand'] = self.brand.to_alipay_dict()
            else:
                params['brand'] = self.brand
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_redirect_url:
            if hasattr(self.item_redirect_url, 'to_alipay_dict'):
                params['item_redirect_url'] = self.item_redirect_url.to_alipay_dict()
            else:
                params['item_redirect_url'] = self.item_redirect_url
        if self.item_url:
            if hasattr(self.item_url, 'to_alipay_dict'):
                params['item_url'] = self.item_url.to_alipay_dict()
            else:
                params['item_url'] = self.item_url
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.remain_stock:
            if hasattr(self.remain_stock, 'to_alipay_dict'):
                params['remain_stock'] = self.remain_stock.to_alipay_dict()
            else:
                params['remain_stock'] = self.remain_stock
        if self.total_stock:
            if hasattr(self.total_stock, 'to_alipay_dict'):
                params['total_stock'] = self.total_stock.to_alipay_dict()
            else:
                params['total_stock'] = self.total_stock
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Singltem()
        if 'biz_item_id' in d:
            o.biz_item_id = d['biz_item_id']
        if 'brand' in d:
            o.brand = d['brand']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_redirect_url' in d:
            o.item_redirect_url = d['item_redirect_url']
        if 'item_url' in d:
            o.item_url = d['item_url']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'price' in d:
            o.price = d['price']
        if 'remain_stock' in d:
            o.remain_stock = d['remain_stock']
        if 'total_stock' in d:
            o.total_stock = d['total_stock']
        return o


