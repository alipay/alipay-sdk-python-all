#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PosCookDishQryDetailModel(object):

    def __init__(self):
        self._category_big_id = None
        self._dish_id = None
        self._dish_img = None
        self._dish_name = None
        self._dish_stall_ref = None
        self._min_price = None
        self._multi_spec = None
        self._special_tag = None
        self._spicy_tag = None
        self._status = None
        self._type = None
        self._unit_name = None

    @property
    def category_big_id(self):
        return self._category_big_id

    @category_big_id.setter
    def category_big_id(self, value):
        self._category_big_id = value
    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def dish_img(self):
        return self._dish_img

    @dish_img.setter
    def dish_img(self, value):
        self._dish_img = value
    @property
    def dish_name(self):
        return self._dish_name

    @dish_name.setter
    def dish_name(self, value):
        self._dish_name = value
    @property
    def dish_stall_ref(self):
        return self._dish_stall_ref

    @dish_stall_ref.setter
    def dish_stall_ref(self, value):
        self._dish_stall_ref = value
    @property
    def min_price(self):
        return self._min_price

    @min_price.setter
    def min_price(self, value):
        self._min_price = value
    @property
    def multi_spec(self):
        return self._multi_spec

    @multi_spec.setter
    def multi_spec(self, value):
        self._multi_spec = value
    @property
    def special_tag(self):
        return self._special_tag

    @special_tag.setter
    def special_tag(self, value):
        self._special_tag = value
    @property
    def spicy_tag(self):
        return self._spicy_tag

    @spicy_tag.setter
    def spicy_tag(self, value):
        self._spicy_tag = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, value):
        self._unit_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_big_id:
            if hasattr(self.category_big_id, 'to_alipay_dict'):
                params['category_big_id'] = self.category_big_id.to_alipay_dict()
            else:
                params['category_big_id'] = self.category_big_id
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.dish_img:
            if hasattr(self.dish_img, 'to_alipay_dict'):
                params['dish_img'] = self.dish_img.to_alipay_dict()
            else:
                params['dish_img'] = self.dish_img
        if self.dish_name:
            if hasattr(self.dish_name, 'to_alipay_dict'):
                params['dish_name'] = self.dish_name.to_alipay_dict()
            else:
                params['dish_name'] = self.dish_name
        if self.dish_stall_ref:
            if hasattr(self.dish_stall_ref, 'to_alipay_dict'):
                params['dish_stall_ref'] = self.dish_stall_ref.to_alipay_dict()
            else:
                params['dish_stall_ref'] = self.dish_stall_ref
        if self.min_price:
            if hasattr(self.min_price, 'to_alipay_dict'):
                params['min_price'] = self.min_price.to_alipay_dict()
            else:
                params['min_price'] = self.min_price
        if self.multi_spec:
            if hasattr(self.multi_spec, 'to_alipay_dict'):
                params['multi_spec'] = self.multi_spec.to_alipay_dict()
            else:
                params['multi_spec'] = self.multi_spec
        if self.special_tag:
            if hasattr(self.special_tag, 'to_alipay_dict'):
                params['special_tag'] = self.special_tag.to_alipay_dict()
            else:
                params['special_tag'] = self.special_tag
        if self.spicy_tag:
            if hasattr(self.spicy_tag, 'to_alipay_dict'):
                params['spicy_tag'] = self.spicy_tag.to_alipay_dict()
            else:
                params['spicy_tag'] = self.spicy_tag
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.unit_name:
            if hasattr(self.unit_name, 'to_alipay_dict'):
                params['unit_name'] = self.unit_name.to_alipay_dict()
            else:
                params['unit_name'] = self.unit_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PosCookDishQryDetailModel()
        if 'category_big_id' in d:
            o.category_big_id = d['category_big_id']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'dish_img' in d:
            o.dish_img = d['dish_img']
        if 'dish_name' in d:
            o.dish_name = d['dish_name']
        if 'dish_stall_ref' in d:
            o.dish_stall_ref = d['dish_stall_ref']
        if 'min_price' in d:
            o.min_price = d['min_price']
        if 'multi_spec' in d:
            o.multi_spec = d['multi_spec']
        if 'special_tag' in d:
            o.special_tag = d['special_tag']
        if 'spicy_tag' in d:
            o.spicy_tag = d['spicy_tag']
        if 'status' in d:
            o.status = d['status']
        if 'type' in d:
            o.type = d['type']
        if 'unit_name' in d:
            o.unit_name = d['unit_name']
        return o


