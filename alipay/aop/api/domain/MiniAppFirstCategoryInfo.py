#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniAppSecondCategoryInfo import MiniAppSecondCategoryInfo


class MiniAppFirstCategoryInfo(object):

    def __init__(self):
        self._category_id = None
        self._category_name = None
        self._child_category = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def child_category(self):
        return self._child_category

    @child_category.setter
    def child_category(self, value):
        if isinstance(value, list):
            self._child_category = list()
            for i in value:
                if isinstance(i, MiniAppSecondCategoryInfo):
                    self._child_category.append(i)
                else:
                    self._child_category.append(MiniAppSecondCategoryInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.child_category:
            if isinstance(self.child_category, list):
                for i in range(0, len(self.child_category)):
                    element = self.child_category[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.child_category[i] = element.to_alipay_dict()
            if hasattr(self.child_category, 'to_alipay_dict'):
                params['child_category'] = self.child_category.to_alipay_dict()
            else:
                params['child_category'] = self.child_category
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppFirstCategoryInfo()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'child_category' in d:
            o.child_category = d['child_category']
        return o


