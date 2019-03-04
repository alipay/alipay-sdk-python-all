#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemCategoryInfo(object):

    def __init__(self):
        self._category_id = None
        self._category_level = None

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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemCategoryInfo()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'category_level' in d:
            o.category_level = d['category_level']
        return o


