#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GoodsDetail(object):

    def __init__(self):
        self._alipay_goods_id = None
        self._body = None
        self._categories_tree = None
        self._goods_category = None
        self._goods_id = None
        self._goods_name = None
        self._price = None
        self._quantity = None
        self._show_url = None

    @property
    def alipay_goods_id(self):
        return self._alipay_goods_id

    @alipay_goods_id.setter
    def alipay_goods_id(self, value):
        self._alipay_goods_id = value
    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def categories_tree(self):
        return self._categories_tree

    @categories_tree.setter
    def categories_tree(self, value):
        self._categories_tree = value
    @property
    def goods_category(self):
        return self._goods_category

    @goods_category.setter
    def goods_category(self, value):
        self._goods_category = value
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
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def show_url(self):
        return self._show_url

    @show_url.setter
    def show_url(self, value):
        self._show_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_goods_id:
            if hasattr(self.alipay_goods_id, 'to_alipay_dict'):
                params['alipay_goods_id'] = self.alipay_goods_id.to_alipay_dict()
            else:
                params['alipay_goods_id'] = self.alipay_goods_id
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.categories_tree:
            if hasattr(self.categories_tree, 'to_alipay_dict'):
                params['categories_tree'] = self.categories_tree.to_alipay_dict()
            else:
                params['categories_tree'] = self.categories_tree
        if self.goods_category:
            if hasattr(self.goods_category, 'to_alipay_dict'):
                params['goods_category'] = self.goods_category.to_alipay_dict()
            else:
                params['goods_category'] = self.goods_category
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
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.show_url:
            if hasattr(self.show_url, 'to_alipay_dict'):
                params['show_url'] = self.show_url.to_alipay_dict()
            else:
                params['show_url'] = self.show_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GoodsDetail()
        if 'alipay_goods_id' in d:
            o.alipay_goods_id = d['alipay_goods_id']
        if 'body' in d:
            o.body = d['body']
        if 'categories_tree' in d:
            o.categories_tree = d['categories_tree']
        if 'goods_category' in d:
            o.goods_category = d['goods_category']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'price' in d:
            o.price = d['price']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'show_url' in d:
            o.show_url = d['show_url']
        return o


