#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppxCategoryVO import AppxCategoryVO


class CategoryAndParentVO(object):

    def __init__(self):
        self._cat_and_parent = None

    @property
    def cat_and_parent(self):
        return self._cat_and_parent

    @cat_and_parent.setter
    def cat_and_parent(self, value):
        if isinstance(value, list):
            self._cat_and_parent = list()
            for i in value:
                if isinstance(i, AppxCategoryVO):
                    self._cat_and_parent.append(i)
                else:
                    self._cat_and_parent.append(AppxCategoryVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.cat_and_parent:
            if isinstance(self.cat_and_parent, list):
                for i in range(0, len(self.cat_and_parent)):
                    element = self.cat_and_parent[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cat_and_parent[i] = element.to_alipay_dict()
            if hasattr(self.cat_and_parent, 'to_alipay_dict'):
                params['cat_and_parent'] = self.cat_and_parent.to_alipay_dict()
            else:
                params['cat_and_parent'] = self.cat_and_parent
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CategoryAndParentVO()
        if 'cat_and_parent' in d:
            o.cat_and_parent = d['cat_and_parent']
        return o


