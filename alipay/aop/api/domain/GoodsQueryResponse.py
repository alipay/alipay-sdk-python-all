#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GoodsQueryResponse(object):

    def __init__(self):
        self._alipay_goods_id = None
        self._buying_url = None
        self._goods_comment = None
        self._goods_description_label = None
        self._goods_id = None
        self._goods_label = None
        self._goods_name = None
        self._goods_type = None
        self._main_pic_url = None
        self._mini_app_id = None
        self._order_number = None
        self._original_price = None
        self._pid = None
        self._publish_cities = None
        self._remaining_quantity = None
        self._sell_price = None
        self._sold_quantity = None
        self._total_quantity = None

    @property
    def alipay_goods_id(self):
        return self._alipay_goods_id

    @alipay_goods_id.setter
    def alipay_goods_id(self, value):
        self._alipay_goods_id = value
    @property
    def buying_url(self):
        return self._buying_url

    @buying_url.setter
    def buying_url(self, value):
        self._buying_url = value
    @property
    def goods_comment(self):
        return self._goods_comment

    @goods_comment.setter
    def goods_comment(self, value):
        self._goods_comment = value
    @property
    def goods_description_label(self):
        return self._goods_description_label

    @goods_description_label.setter
    def goods_description_label(self, value):
        self._goods_description_label = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def goods_label(self):
        return self._goods_label

    @goods_label.setter
    def goods_label(self, value):
        self._goods_label = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def goods_type(self):
        return self._goods_type

    @goods_type.setter
    def goods_type(self, value):
        self._goods_type = value
    @property
    def main_pic_url(self):
        return self._main_pic_url

    @main_pic_url.setter
    def main_pic_url(self, value):
        self._main_pic_url = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def order_number(self):
        return self._order_number

    @order_number.setter
    def order_number(self, value):
        self._order_number = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def publish_cities(self):
        return self._publish_cities

    @publish_cities.setter
    def publish_cities(self, value):
        self._publish_cities = value
    @property
    def remaining_quantity(self):
        return self._remaining_quantity

    @remaining_quantity.setter
    def remaining_quantity(self, value):
        self._remaining_quantity = value
    @property
    def sell_price(self):
        return self._sell_price

    @sell_price.setter
    def sell_price(self, value):
        self._sell_price = value
    @property
    def sold_quantity(self):
        return self._sold_quantity

    @sold_quantity.setter
    def sold_quantity(self, value):
        self._sold_quantity = value
    @property
    def total_quantity(self):
        return self._total_quantity

    @total_quantity.setter
    def total_quantity(self, value):
        self._total_quantity = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_goods_id:
            if hasattr(self.alipay_goods_id, 'to_alipay_dict'):
                params['alipay_goods_id'] = self.alipay_goods_id.to_alipay_dict()
            else:
                params['alipay_goods_id'] = self.alipay_goods_id
        if self.buying_url:
            if hasattr(self.buying_url, 'to_alipay_dict'):
                params['buying_url'] = self.buying_url.to_alipay_dict()
            else:
                params['buying_url'] = self.buying_url
        if self.goods_comment:
            if hasattr(self.goods_comment, 'to_alipay_dict'):
                params['goods_comment'] = self.goods_comment.to_alipay_dict()
            else:
                params['goods_comment'] = self.goods_comment
        if self.goods_description_label:
            if hasattr(self.goods_description_label, 'to_alipay_dict'):
                params['goods_description_label'] = self.goods_description_label.to_alipay_dict()
            else:
                params['goods_description_label'] = self.goods_description_label
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.goods_label:
            if hasattr(self.goods_label, 'to_alipay_dict'):
                params['goods_label'] = self.goods_label.to_alipay_dict()
            else:
                params['goods_label'] = self.goods_label
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.goods_type:
            if hasattr(self.goods_type, 'to_alipay_dict'):
                params['goods_type'] = self.goods_type.to_alipay_dict()
            else:
                params['goods_type'] = self.goods_type
        if self.main_pic_url:
            if hasattr(self.main_pic_url, 'to_alipay_dict'):
                params['main_pic_url'] = self.main_pic_url.to_alipay_dict()
            else:
                params['main_pic_url'] = self.main_pic_url
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.order_number:
            if hasattr(self.order_number, 'to_alipay_dict'):
                params['order_number'] = self.order_number.to_alipay_dict()
            else:
                params['order_number'] = self.order_number
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.publish_cities:
            if hasattr(self.publish_cities, 'to_alipay_dict'):
                params['publish_cities'] = self.publish_cities.to_alipay_dict()
            else:
                params['publish_cities'] = self.publish_cities
        if self.remaining_quantity:
            if hasattr(self.remaining_quantity, 'to_alipay_dict'):
                params['remaining_quantity'] = self.remaining_quantity.to_alipay_dict()
            else:
                params['remaining_quantity'] = self.remaining_quantity
        if self.sell_price:
            if hasattr(self.sell_price, 'to_alipay_dict'):
                params['sell_price'] = self.sell_price.to_alipay_dict()
            else:
                params['sell_price'] = self.sell_price
        if self.sold_quantity:
            if hasattr(self.sold_quantity, 'to_alipay_dict'):
                params['sold_quantity'] = self.sold_quantity.to_alipay_dict()
            else:
                params['sold_quantity'] = self.sold_quantity
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
        o = GoodsQueryResponse()
        if 'alipay_goods_id' in d:
            o.alipay_goods_id = d['alipay_goods_id']
        if 'buying_url' in d:
            o.buying_url = d['buying_url']
        if 'goods_comment' in d:
            o.goods_comment = d['goods_comment']
        if 'goods_description_label' in d:
            o.goods_description_label = d['goods_description_label']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_label' in d:
            o.goods_label = d['goods_label']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'goods_type' in d:
            o.goods_type = d['goods_type']
        if 'main_pic_url' in d:
            o.main_pic_url = d['main_pic_url']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'order_number' in d:
            o.order_number = d['order_number']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'pid' in d:
            o.pid = d['pid']
        if 'publish_cities' in d:
            o.publish_cities = d['publish_cities']
        if 'remaining_quantity' in d:
            o.remaining_quantity = d['remaining_quantity']
        if 'sell_price' in d:
            o.sell_price = d['sell_price']
        if 'sold_quantity' in d:
            o.sold_quantity = d['sold_quantity']
        if 'total_quantity' in d:
            o.total_quantity = d['total_quantity']
        return o


