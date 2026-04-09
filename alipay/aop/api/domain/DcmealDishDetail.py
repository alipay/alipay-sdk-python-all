#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DcmealDishDetail(object):

    def __init__(self):
        self._desc = None
        self._dish_id = None
        self._dish_name = None
        self._dish_price = None
        self._dish_sale_amount = None
        self._nutrition = None
        self._unit = None
        self._weight = None
        self._weight_type = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def dish_name(self):
        return self._dish_name

    @dish_name.setter
    def dish_name(self, value):
        self._dish_name = value
    @property
    def dish_price(self):
        return self._dish_price

    @dish_price.setter
    def dish_price(self, value):
        self._dish_price = value
    @property
    def dish_sale_amount(self):
        return self._dish_sale_amount

    @dish_sale_amount.setter
    def dish_sale_amount(self, value):
        self._dish_sale_amount = value
    @property
    def nutrition(self):
        return self._nutrition

    @nutrition.setter
    def nutrition(self, value):
        self._nutrition = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value
    @property
    def weight_type(self):
        return self._weight_type

    @weight_type.setter
    def weight_type(self, value):
        self._weight_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.dish_name:
            if hasattr(self.dish_name, 'to_alipay_dict'):
                params['dish_name'] = self.dish_name.to_alipay_dict()
            else:
                params['dish_name'] = self.dish_name
        if self.dish_price:
            if hasattr(self.dish_price, 'to_alipay_dict'):
                params['dish_price'] = self.dish_price.to_alipay_dict()
            else:
                params['dish_price'] = self.dish_price
        if self.dish_sale_amount:
            if hasattr(self.dish_sale_amount, 'to_alipay_dict'):
                params['dish_sale_amount'] = self.dish_sale_amount.to_alipay_dict()
            else:
                params['dish_sale_amount'] = self.dish_sale_amount
        if self.nutrition:
            if hasattr(self.nutrition, 'to_alipay_dict'):
                params['nutrition'] = self.nutrition.to_alipay_dict()
            else:
                params['nutrition'] = self.nutrition
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        if self.weight:
            if hasattr(self.weight, 'to_alipay_dict'):
                params['weight'] = self.weight.to_alipay_dict()
            else:
                params['weight'] = self.weight
        if self.weight_type:
            if hasattr(self.weight_type, 'to_alipay_dict'):
                params['weight_type'] = self.weight_type.to_alipay_dict()
            else:
                params['weight_type'] = self.weight_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DcmealDishDetail()
        if 'desc' in d:
            o.desc = d['desc']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'dish_name' in d:
            o.dish_name = d['dish_name']
        if 'dish_price' in d:
            o.dish_price = d['dish_price']
        if 'dish_sale_amount' in d:
            o.dish_sale_amount = d['dish_sale_amount']
        if 'nutrition' in d:
            o.nutrition = d['nutrition']
        if 'unit' in d:
            o.unit = d['unit']
        if 'weight' in d:
            o.weight = d['weight']
        if 'weight_type' in d:
            o.weight_type = d['weight_type']
        return o


