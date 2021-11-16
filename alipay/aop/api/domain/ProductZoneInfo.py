#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProductZoneInfo(object):

    def __init__(self):
        self._end_time = None
        self._origin_price = None
        self._out_zone_id = None
        self._sale_price = None
        self._start_time = None
        self._stock_count = None
        self._zone_name = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def origin_price(self):
        return self._origin_price

    @origin_price.setter
    def origin_price(self, value):
        self._origin_price = value
    @property
    def out_zone_id(self):
        return self._out_zone_id

    @out_zone_id.setter
    def out_zone_id(self, value):
        self._out_zone_id = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def stock_count(self):
        return self._stock_count

    @stock_count.setter
    def stock_count(self, value):
        self._stock_count = value
    @property
    def zone_name(self):
        return self._zone_name

    @zone_name.setter
    def zone_name(self, value):
        self._zone_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.origin_price:
            if hasattr(self.origin_price, 'to_alipay_dict'):
                params['origin_price'] = self.origin_price.to_alipay_dict()
            else:
                params['origin_price'] = self.origin_price
        if self.out_zone_id:
            if hasattr(self.out_zone_id, 'to_alipay_dict'):
                params['out_zone_id'] = self.out_zone_id.to_alipay_dict()
            else:
                params['out_zone_id'] = self.out_zone_id
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.stock_count:
            if hasattr(self.stock_count, 'to_alipay_dict'):
                params['stock_count'] = self.stock_count.to_alipay_dict()
            else:
                params['stock_count'] = self.stock_count
        if self.zone_name:
            if hasattr(self.zone_name, 'to_alipay_dict'):
                params['zone_name'] = self.zone_name.to_alipay_dict()
            else:
                params['zone_name'] = self.zone_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductZoneInfo()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'origin_price' in d:
            o.origin_price = d['origin_price']
        if 'out_zone_id' in d:
            o.out_zone_id = d['out_zone_id']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'stock_count' in d:
            o.stock_count = d['stock_count']
        if 'zone_name' in d:
            o.zone_name = d['zone_name']
        return o


