#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VenueProductSimpleInfo(object):

    def __init__(self):
        self._category_name = None
        self._count = None
        self._end_time = None
        self._order_product_id = None
        self._product_name = None
        self._product_type = None
        self._sale_amount = None
        self._start_time = None
        self._zone_name = None

    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def order_product_id(self):
        return self._order_product_id

    @order_product_id.setter
    def order_product_id(self, value):
        self._order_product_id = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    @property
    def sale_amount(self):
        return self._sale_amount

    @sale_amount.setter
    def sale_amount(self, value):
        self._sale_amount = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def zone_name(self):
        return self._zone_name

    @zone_name.setter
    def zone_name(self, value):
        self._zone_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.order_product_id:
            if hasattr(self.order_product_id, 'to_alipay_dict'):
                params['order_product_id'] = self.order_product_id.to_alipay_dict()
            else:
                params['order_product_id'] = self.order_product_id
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.product_type:
            if hasattr(self.product_type, 'to_alipay_dict'):
                params['product_type'] = self.product_type.to_alipay_dict()
            else:
                params['product_type'] = self.product_type
        if self.sale_amount:
            if hasattr(self.sale_amount, 'to_alipay_dict'):
                params['sale_amount'] = self.sale_amount.to_alipay_dict()
            else:
                params['sale_amount'] = self.sale_amount
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
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
        o = VenueProductSimpleInfo()
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'count' in d:
            o.count = d['count']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'order_product_id' in d:
            o.order_product_id = d['order_product_id']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'product_type' in d:
            o.product_type = d['product_type']
        if 'sale_amount' in d:
            o.sale_amount = d['sale_amount']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'zone_name' in d:
            o.zone_name = d['zone_name']
        return o


