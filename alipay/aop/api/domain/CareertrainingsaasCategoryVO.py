#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CareertrainingsaasCategoryVO(object):

    def __init__(self):
        self._category_id = None
        self._category_level = None
        self._category_name = None
        self._category_parent_id = None
        self._category_sort = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def category_level(self):
        return self._category_level

    @category_level.setter
    def category_level(self, value):
        self._category_level = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def category_parent_id(self):
        return self._category_parent_id

    @category_parent_id.setter
    def category_parent_id(self, value):
        self._category_parent_id = value
    @property
    def category_sort(self):
        return self._category_sort

    @category_sort.setter
    def category_sort(self, value):
        self._category_sort = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.category_level:
            if hasattr(self.category_level, 'to_alipay_dict'):
                params['category_level'] = self.category_level.to_alipay_dict()
            else:
                params['category_level'] = self.category_level
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.category_parent_id:
            if hasattr(self.category_parent_id, 'to_alipay_dict'):
                params['category_parent_id'] = self.category_parent_id.to_alipay_dict()
            else:
                params['category_parent_id'] = self.category_parent_id
        if self.category_sort:
            if hasattr(self.category_sort, 'to_alipay_dict'):
                params['category_sort'] = self.category_sort.to_alipay_dict()
            else:
                params['category_sort'] = self.category_sort
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CareertrainingsaasCategoryVO()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'category_level' in d:
            o.category_level = d['category_level']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'category_parent_id' in d:
            o.category_parent_id = d['category_parent_id']
        if 'category_sort' in d:
            o.category_sort = d['category_sort']
        return o


