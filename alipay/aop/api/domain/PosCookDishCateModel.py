#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PosCookDishCateModel(object):

    def __init__(self):
        self._cate_dish_num = None
        self._cate_id = None
        self._cate_name = None
        self._cate_sort = None

    @property
    def cate_dish_num(self):
        return self._cate_dish_num

    @cate_dish_num.setter
    def cate_dish_num(self, value):
        self._cate_dish_num = value
    @property
    def cate_id(self):
        return self._cate_id

    @cate_id.setter
    def cate_id(self, value):
        self._cate_id = value
    @property
    def cate_name(self):
        return self._cate_name

    @cate_name.setter
    def cate_name(self, value):
        self._cate_name = value
    @property
    def cate_sort(self):
        return self._cate_sort

    @cate_sort.setter
    def cate_sort(self, value):
        self._cate_sort = value


    def to_alipay_dict(self):
        params = dict()
        if self.cate_dish_num:
            if hasattr(self.cate_dish_num, 'to_alipay_dict'):
                params['cate_dish_num'] = self.cate_dish_num.to_alipay_dict()
            else:
                params['cate_dish_num'] = self.cate_dish_num
        if self.cate_id:
            if hasattr(self.cate_id, 'to_alipay_dict'):
                params['cate_id'] = self.cate_id.to_alipay_dict()
            else:
                params['cate_id'] = self.cate_id
        if self.cate_name:
            if hasattr(self.cate_name, 'to_alipay_dict'):
                params['cate_name'] = self.cate_name.to_alipay_dict()
            else:
                params['cate_name'] = self.cate_name
        if self.cate_sort:
            if hasattr(self.cate_sort, 'to_alipay_dict'):
                params['cate_sort'] = self.cate_sort.to_alipay_dict()
            else:
                params['cate_sort'] = self.cate_sort
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PosCookDishCateModel()
        if 'cate_dish_num' in d:
            o.cate_dish_num = d['cate_dish_num']
        if 'cate_id' in d:
            o.cate_id = d['cate_id']
        if 'cate_name' in d:
            o.cate_name = d['cate_name']
        if 'cate_sort' in d:
            o.cate_sort = d['cate_sort']
        return o


