#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IsvSkuItem(object):

    def __init__(self):
        self._expire_time = None
        self._guarantee_duration = None
        self._guarantee_mileage = None
        self._marked_price = None
        self._quote_id = None
        self._quote_time = None
        self._sale_price = None
        self._sku_id = None

    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def guarantee_duration(self):
        return self._guarantee_duration

    @guarantee_duration.setter
    def guarantee_duration(self, value):
        self._guarantee_duration = value
    @property
    def guarantee_mileage(self):
        return self._guarantee_mileage

    @guarantee_mileage.setter
    def guarantee_mileage(self, value):
        self._guarantee_mileage = value
    @property
    def marked_price(self):
        return self._marked_price

    @marked_price.setter
    def marked_price(self, value):
        self._marked_price = value
    @property
    def quote_id(self):
        return self._quote_id

    @quote_id.setter
    def quote_id(self, value):
        self._quote_id = value
    @property
    def quote_time(self):
        return self._quote_time

    @quote_time.setter
    def quote_time(self, value):
        self._quote_time = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.guarantee_duration:
            if hasattr(self.guarantee_duration, 'to_alipay_dict'):
                params['guarantee_duration'] = self.guarantee_duration.to_alipay_dict()
            else:
                params['guarantee_duration'] = self.guarantee_duration
        if self.guarantee_mileage:
            if hasattr(self.guarantee_mileage, 'to_alipay_dict'):
                params['guarantee_mileage'] = self.guarantee_mileage.to_alipay_dict()
            else:
                params['guarantee_mileage'] = self.guarantee_mileage
        if self.marked_price:
            if hasattr(self.marked_price, 'to_alipay_dict'):
                params['marked_price'] = self.marked_price.to_alipay_dict()
            else:
                params['marked_price'] = self.marked_price
        if self.quote_id:
            if hasattr(self.quote_id, 'to_alipay_dict'):
                params['quote_id'] = self.quote_id.to_alipay_dict()
            else:
                params['quote_id'] = self.quote_id
        if self.quote_time:
            if hasattr(self.quote_time, 'to_alipay_dict'):
                params['quote_time'] = self.quote_time.to_alipay_dict()
            else:
                params['quote_time'] = self.quote_time
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
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
        o = IsvSkuItem()
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'guarantee_duration' in d:
            o.guarantee_duration = d['guarantee_duration']
        if 'guarantee_mileage' in d:
            o.guarantee_mileage = d['guarantee_mileage']
        if 'marked_price' in d:
            o.marked_price = d['marked_price']
        if 'quote_id' in d:
            o.quote_id = d['quote_id']
        if 'quote_time' in d:
            o.quote_time = d['quote_time']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


