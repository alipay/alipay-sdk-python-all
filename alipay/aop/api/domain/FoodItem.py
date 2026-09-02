#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FoodItem(object):

    def __init__(self):
        self._calorie = None
        self._food_name = None
        self._weight_g = None

    @property
    def calorie(self):
        return self._calorie

    @calorie.setter
    def calorie(self, value):
        self._calorie = value
    @property
    def food_name(self):
        return self._food_name

    @food_name.setter
    def food_name(self, value):
        self._food_name = value
    @property
    def weight_g(self):
        return self._weight_g

    @weight_g.setter
    def weight_g(self, value):
        self._weight_g = value


    def to_alipay_dict(self):
        params = dict()
        if self.calorie:
            if hasattr(self.calorie, 'to_alipay_dict'):
                params['calorie'] = self.calorie.to_alipay_dict()
            else:
                params['calorie'] = self.calorie
        if self.food_name:
            if hasattr(self.food_name, 'to_alipay_dict'):
                params['food_name'] = self.food_name.to_alipay_dict()
            else:
                params['food_name'] = self.food_name
        if self.weight_g:
            if hasattr(self.weight_g, 'to_alipay_dict'):
                params['weight_g'] = self.weight_g.to_alipay_dict()
            else:
                params['weight_g'] = self.weight_g
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FoodItem()
        if 'calorie' in d:
            o.calorie = d['calorie']
        if 'food_name' in d:
            o.food_name = d['food_name']
        if 'weight_g' in d:
            o.weight_g = d['weight_g']
        return o


