#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DcmealDishArrangeDetail(object):

    def __init__(self):
        self._arrange_id = None
        self._campus_id = None
        self._campus_name = None
        self._food_id = None
        self._food_name = None
        self._meal_type = None
        self._price = None
        self._restaurant_id = None
        self._restaurant_name = None
        self._terminal_id = None
        self._terminal_name = None

    @property
    def arrange_id(self):
        return self._arrange_id

    @arrange_id.setter
    def arrange_id(self, value):
        self._arrange_id = value
    @property
    def campus_id(self):
        return self._campus_id

    @campus_id.setter
    def campus_id(self, value):
        self._campus_id = value
    @property
    def campus_name(self):
        return self._campus_name

    @campus_name.setter
    def campus_name(self, value):
        self._campus_name = value
    @property
    def food_id(self):
        return self._food_id

    @food_id.setter
    def food_id(self, value):
        self._food_id = value
    @property
    def food_name(self):
        return self._food_name

    @food_name.setter
    def food_name(self, value):
        self._food_name = value
    @property
    def meal_type(self):
        return self._meal_type

    @meal_type.setter
    def meal_type(self, value):
        self._meal_type = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def restaurant_id(self):
        return self._restaurant_id

    @restaurant_id.setter
    def restaurant_id(self, value):
        self._restaurant_id = value
    @property
    def restaurant_name(self):
        return self._restaurant_name

    @restaurant_name.setter
    def restaurant_name(self, value):
        self._restaurant_name = value
    @property
    def terminal_id(self):
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, value):
        self._terminal_id = value
    @property
    def terminal_name(self):
        return self._terminal_name

    @terminal_name.setter
    def terminal_name(self, value):
        self._terminal_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.arrange_id:
            if hasattr(self.arrange_id, 'to_alipay_dict'):
                params['arrange_id'] = self.arrange_id.to_alipay_dict()
            else:
                params['arrange_id'] = self.arrange_id
        if self.campus_id:
            if hasattr(self.campus_id, 'to_alipay_dict'):
                params['campus_id'] = self.campus_id.to_alipay_dict()
            else:
                params['campus_id'] = self.campus_id
        if self.campus_name:
            if hasattr(self.campus_name, 'to_alipay_dict'):
                params['campus_name'] = self.campus_name.to_alipay_dict()
            else:
                params['campus_name'] = self.campus_name
        if self.food_id:
            if hasattr(self.food_id, 'to_alipay_dict'):
                params['food_id'] = self.food_id.to_alipay_dict()
            else:
                params['food_id'] = self.food_id
        if self.food_name:
            if hasattr(self.food_name, 'to_alipay_dict'):
                params['food_name'] = self.food_name.to_alipay_dict()
            else:
                params['food_name'] = self.food_name
        if self.meal_type:
            if hasattr(self.meal_type, 'to_alipay_dict'):
                params['meal_type'] = self.meal_type.to_alipay_dict()
            else:
                params['meal_type'] = self.meal_type
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.restaurant_id:
            if hasattr(self.restaurant_id, 'to_alipay_dict'):
                params['restaurant_id'] = self.restaurant_id.to_alipay_dict()
            else:
                params['restaurant_id'] = self.restaurant_id
        if self.restaurant_name:
            if hasattr(self.restaurant_name, 'to_alipay_dict'):
                params['restaurant_name'] = self.restaurant_name.to_alipay_dict()
            else:
                params['restaurant_name'] = self.restaurant_name
        if self.terminal_id:
            if hasattr(self.terminal_id, 'to_alipay_dict'):
                params['terminal_id'] = self.terminal_id.to_alipay_dict()
            else:
                params['terminal_id'] = self.terminal_id
        if self.terminal_name:
            if hasattr(self.terminal_name, 'to_alipay_dict'):
                params['terminal_name'] = self.terminal_name.to_alipay_dict()
            else:
                params['terminal_name'] = self.terminal_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DcmealDishArrangeDetail()
        if 'arrange_id' in d:
            o.arrange_id = d['arrange_id']
        if 'campus_id' in d:
            o.campus_id = d['campus_id']
        if 'campus_name' in d:
            o.campus_name = d['campus_name']
        if 'food_id' in d:
            o.food_id = d['food_id']
        if 'food_name' in d:
            o.food_name = d['food_name']
        if 'meal_type' in d:
            o.meal_type = d['meal_type']
        if 'price' in d:
            o.price = d['price']
        if 'restaurant_id' in d:
            o.restaurant_id = d['restaurant_id']
        if 'restaurant_name' in d:
            o.restaurant_name = d['restaurant_name']
        if 'terminal_id' in d:
            o.terminal_id = d['terminal_id']
        if 'terminal_name' in d:
            o.terminal_name = d['terminal_name']
        return o


