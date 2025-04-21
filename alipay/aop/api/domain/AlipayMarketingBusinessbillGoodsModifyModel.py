#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingBusinessbillGoodsModifyModel(object):

    def __init__(self):
        self._activity_scene = None
        self._category = None
        self._energy_efficiency_level = None
        self._goods_id = None
        self._goods_model_number = None
        self._goods_title = None
        self._open_id = None
        self._price = None
        self._sub_category = None
        self._user_id = None

    @property
    def activity_scene(self):
        return self._activity_scene

    @activity_scene.setter
    def activity_scene(self, value):
        self._activity_scene = value
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
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
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
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_scene:
            if hasattr(self.activity_scene, 'to_alipay_dict'):
                params['activity_scene'] = self.activity_scene.to_alipay_dict()
            else:
                params['activity_scene'] = self.activity_scene
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
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
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
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingBusinessbillGoodsModifyModel()
        if 'activity_scene' in d:
            o.activity_scene = d['activity_scene']
        if 'category' in d:
            o.category = d['category']
        if 'energy_efficiency_level' in d:
            o.energy_efficiency_level = d['energy_efficiency_level']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_model_number' in d:
            o.goods_model_number = d['goods_model_number']
        if 'goods_title' in d:
            o.goods_title = d['goods_title']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'price' in d:
            o.price = d['price']
        if 'sub_category' in d:
            o.sub_category = d['sub_category']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


