#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EstimateDishInfo(object):

    def __init__(self):
        self._dish_id = None
        self._inventory = None
        self._out_dish_id = None

    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value
    @property
    def out_dish_id(self):
        return self._out_dish_id

    @out_dish_id.setter
    def out_dish_id(self, value):
        self._out_dish_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        if self.out_dish_id:
            if hasattr(self.out_dish_id, 'to_alipay_dict'):
                params['out_dish_id'] = self.out_dish_id.to_alipay_dict()
            else:
                params['out_dish_id'] = self.out_dish_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EstimateDishInfo()
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'inventory' in d:
            o.inventory = d['inventory']
        if 'out_dish_id' in d:
            o.out_dish_id = d['out_dish_id']
        return o


