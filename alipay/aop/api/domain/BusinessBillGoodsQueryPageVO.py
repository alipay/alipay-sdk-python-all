#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessBillGoodsQueryPageVO(object):

    def __init__(self):
        self._category = None
        self._energy_efficiency_level = None
        self._gmt_create = None
        self._gmt_modified = None
        self._goods_code = None
        self._goods_model_number = None
        self._goods_title = None
        self._id = None
        self._price = None
        self._sub_category = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def energy_efficiency_level(self):
        return self._energy_efficiency_level

    @energy_efficiency_level.setter
    def energy_efficiency_level(self, value):
        self._energy_efficiency_level = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def goods_code(self):
        return self._goods_code

    @goods_code.setter
    def goods_code(self, value):
        self._goods_code = value
    @property
    def goods_model_number(self):
        return self._goods_model_number

    @goods_model_number.setter
    def goods_model_number(self, value):
        self._goods_model_number = value
    @property
    def goods_title(self):
        return self._goods_title

    @goods_title.setter
    def goods_title(self, value):
        self._goods_title = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def sub_category(self):
        return self._sub_category

    @sub_category.setter
    def sub_category(self, value):
        self._sub_category = value


    def to_alipay_dict(self):
        params = dict()
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.energy_efficiency_level:
            if hasattr(self.energy_efficiency_level, 'to_alipay_dict'):
                params['energy_efficiency_level'] = self.energy_efficiency_level.to_alipay_dict()
            else:
                params['energy_efficiency_level'] = self.energy_efficiency_level
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.goods_code:
            if hasattr(self.goods_code, 'to_alipay_dict'):
                params['goods_code'] = self.goods_code.to_alipay_dict()
            else:
                params['goods_code'] = self.goods_code
        if self.goods_model_number:
            if hasattr(self.goods_model_number, 'to_alipay_dict'):
                params['goods_model_number'] = self.goods_model_number.to_alipay_dict()
            else:
                params['goods_model_number'] = self.goods_model_number
        if self.goods_title:
            if hasattr(self.goods_title, 'to_alipay_dict'):
                params['goods_title'] = self.goods_title.to_alipay_dict()
            else:
                params['goods_title'] = self.goods_title
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.sub_category:
            if hasattr(self.sub_category, 'to_alipay_dict'):
                params['sub_category'] = self.sub_category.to_alipay_dict()
            else:
                params['sub_category'] = self.sub_category
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessBillGoodsQueryPageVO()
        if 'category' in d:
            o.category = d['category']
        if 'energy_efficiency_level' in d:
            o.energy_efficiency_level = d['energy_efficiency_level']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'goods_code' in d:
            o.goods_code = d['goods_code']
        if 'goods_model_number' in d:
            o.goods_model_number = d['goods_model_number']
        if 'goods_title' in d:
            o.goods_title = d['goods_title']
        if 'id' in d:
            o.id = d['id']
        if 'price' in d:
            o.price = d['price']
        if 'sub_category' in d:
            o.sub_category = d['sub_category']
        return o


