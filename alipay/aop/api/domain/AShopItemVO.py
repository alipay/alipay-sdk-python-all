#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AShopItemVO(object):

    def __init__(self):
        self._item_id = None
        self._item_sub_type = None
        self._out_item_id = None
        self._price_unit = None
        self._sale_price = None
        self._sell_status = None
        self._sold_end_time = None
        self._sold_start_time = None
        self._title = None
        self._total_quantity = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_sub_type(self):
        return self._item_sub_type

    @item_sub_type.setter
    def item_sub_type(self, value):
        self._item_sub_type = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def price_unit(self):
        return self._price_unit

    @price_unit.setter
    def price_unit(self, value):
        self._price_unit = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def sell_status(self):
        return self._sell_status

    @sell_status.setter
    def sell_status(self, value):
        self._sell_status = value
    @property
    def sold_end_time(self):
        return self._sold_end_time

    @sold_end_time.setter
    def sold_end_time(self, value):
        self._sold_end_time = value
    @property
    def sold_start_time(self):
        return self._sold_start_time

    @sold_start_time.setter
    def sold_start_time(self, value):
        self._sold_start_time = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def total_quantity(self):
        return self._total_quantity

    @total_quantity.setter
    def total_quantity(self, value):
        self._total_quantity = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_sub_type:
            if hasattr(self.item_sub_type, 'to_alipay_dict'):
                params['item_sub_type'] = self.item_sub_type.to_alipay_dict()
            else:
                params['item_sub_type'] = self.item_sub_type
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.price_unit:
            if hasattr(self.price_unit, 'to_alipay_dict'):
                params['price_unit'] = self.price_unit.to_alipay_dict()
            else:
                params['price_unit'] = self.price_unit
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.sell_status:
            if hasattr(self.sell_status, 'to_alipay_dict'):
                params['sell_status'] = self.sell_status.to_alipay_dict()
            else:
                params['sell_status'] = self.sell_status
        if self.sold_end_time:
            if hasattr(self.sold_end_time, 'to_alipay_dict'):
                params['sold_end_time'] = self.sold_end_time.to_alipay_dict()
            else:
                params['sold_end_time'] = self.sold_end_time
        if self.sold_start_time:
            if hasattr(self.sold_start_time, 'to_alipay_dict'):
                params['sold_start_time'] = self.sold_start_time.to_alipay_dict()
            else:
                params['sold_start_time'] = self.sold_start_time
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.total_quantity:
            if hasattr(self.total_quantity, 'to_alipay_dict'):
                params['total_quantity'] = self.total_quantity.to_alipay_dict()
            else:
                params['total_quantity'] = self.total_quantity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AShopItemVO()
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_sub_type' in d:
            o.item_sub_type = d['item_sub_type']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'price_unit' in d:
            o.price_unit = d['price_unit']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'sell_status' in d:
            o.sell_status = d['sell_status']
        if 'sold_end_time' in d:
            o.sold_end_time = d['sold_end_time']
        if 'sold_start_time' in d:
            o.sold_start_time = d['sold_start_time']
        if 'title' in d:
            o.title = d['title']
        if 'total_quantity' in d:
            o.total_quantity = d['total_quantity']
        return o


