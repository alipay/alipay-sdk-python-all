#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CategoryLeafDTO import CategoryLeafDTO


class CategoryDTO(object):

    def __init__(self):
        self._id = None
        self._leaf_cates = None
        self._name = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def leaf_cates(self):
        return self._leaf_cates

    @leaf_cates.setter
    def leaf_cates(self, value):
        if isinstance(value, list):
            self._leaf_cates = list()
            for i in value:
                if isinstance(i, CategoryLeafDTO):
                    self._leaf_cates.append(i)
                else:
                    self._leaf_cates.append(CategoryLeafDTO.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.leaf_cates:
            if isinstance(self.leaf_cates, list):
                for i in range(0, len(self.leaf_cates)):
                    element = self.leaf_cates[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.leaf_cates[i] = element.to_alipay_dict()
            if hasattr(self.leaf_cates, 'to_alipay_dict'):
                params['leaf_cates'] = self.leaf_cates.to_alipay_dict()
            else:
                params['leaf_cates'] = self.leaf_cates
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CategoryDTO()
        if 'id' in d:
            o.id = d['id']
        if 'leaf_cates' in d:
            o.leaf_cates = d['leaf_cates']
        if 'name' in d:
            o.name = d['name']
        return o


