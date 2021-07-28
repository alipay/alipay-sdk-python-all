#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishVirtualDishSimplifyInfo(object):

    def __init__(self):
        self._out_dish_id = None
        self._sort = None

    @property
    def out_dish_id(self):
        return self._out_dish_id

    @out_dish_id.setter
    def out_dish_id(self, value):
        self._out_dish_id = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_dish_id:
            if hasattr(self.out_dish_id, 'to_alipay_dict'):
                params['out_dish_id'] = self.out_dish_id.to_alipay_dict()
            else:
                params['out_dish_id'] = self.out_dish_id
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishVirtualDishSimplifyInfo()
        if 'out_dish_id' in d:
            o.out_dish_id = d['out_dish_id']
        if 'sort' in d:
            o.sort = d['sort']
        return o


