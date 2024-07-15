#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoMallCategoryQueryModel(object):

    def __init__(self):
        self._category_ids = None
        self._parent_category_id = None

    @property
    def category_ids(self):
        return self._category_ids

    @category_ids.setter
    def category_ids(self, value):
        if isinstance(value, list):
            self._category_ids = list()
            for i in value:
                self._category_ids.append(i)
    @property
    def parent_category_id(self):
        return self._parent_category_id

    @parent_category_id.setter
    def parent_category_id(self, value):
        self._parent_category_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_ids:
            if isinstance(self.category_ids, list):
                for i in range(0, len(self.category_ids)):
                    element = self.category_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_ids[i] = element.to_alipay_dict()
            if hasattr(self.category_ids, 'to_alipay_dict'):
                params['category_ids'] = self.category_ids.to_alipay_dict()
            else:
                params['category_ids'] = self.category_ids
        if self.parent_category_id:
            if hasattr(self.parent_category_id, 'to_alipay_dict'):
                params['parent_category_id'] = self.parent_category_id.to_alipay_dict()
            else:
                params['parent_category_id'] = self.parent_category_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoMallCategoryQueryModel()
        if 'category_ids' in d:
            o.category_ids = d['category_ids']
        if 'parent_category_id' in d:
            o.parent_category_id = d['parent_category_id']
        return o


