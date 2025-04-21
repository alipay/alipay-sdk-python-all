#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LinkedMallItemBaseSku(object):

    def __init__(self):
        self._can_sell = None
        self._price_cent = None
        self._sku_id = None
        self._sku_pic_url = None
        self._sku_title = None

    @property
    def can_sell(self):
        return self._can_sell

    @can_sell.setter
    def can_sell(self, value):
        self._can_sell = value
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
    @property
    def sku_pic_url(self):
        return self._sku_pic_url

    @sku_pic_url.setter
    def sku_pic_url(self, value):
        self._sku_pic_url = value
    @property
    def sku_title(self):
        return self._sku_title

    @sku_title.setter
    def sku_title(self, value):
        self._sku_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_sell:
            if hasattr(self.can_sell, 'to_alipay_dict'):
                params['can_sell'] = self.can_sell.to_alipay_dict()
            else:
                params['can_sell'] = self.can_sell
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
        if self.sku_pic_url:
            if hasattr(self.sku_pic_url, 'to_alipay_dict'):
                params['sku_pic_url'] = self.sku_pic_url.to_alipay_dict()
            else:
                params['sku_pic_url'] = self.sku_pic_url
        if self.sku_title:
            if hasattr(self.sku_title, 'to_alipay_dict'):
                params['sku_title'] = self.sku_title.to_alipay_dict()
            else:
                params['sku_title'] = self.sku_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LinkedMallItemBaseSku()
        if 'can_sell' in d:
            o.can_sell = d['can_sell']
        if 'price_cent' in d:
            o.price_cent = d['price_cent']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sku_pic_url' in d:
            o.sku_pic_url = d['sku_pic_url']
        if 'sku_title' in d:
            o.sku_title = d['sku_title']
        return o


