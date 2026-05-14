#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExaminationThirdCategoryInfo import ExaminationThirdCategoryInfo


class ExaminationSecondCategoryInfo(object):

    def __init__(self):
        self._category_code = None
        self._category_name = None
        self._category_state = None
        self._category_type = None
        self._children_list = None
        self._id = None
        self._is_leaf = None
        self._level = None
        self._parent_id = None

    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def category_state(self):
        return self._category_state

    @category_state.setter
    def category_state(self, value):
        self._category_state = value
    @property
    def category_type(self):
        return self._category_type

    @category_type.setter
    def category_type(self, value):
        self._category_type = value
    @property
    def children_list(self):
        return self._children_list

    @children_list.setter
    def children_list(self, value):
        if isinstance(value, list):
            self._children_list = list()
            for i in value:
                if isinstance(i, ExaminationThirdCategoryInfo):
                    self._children_list.append(i)
                else:
                    self._children_list.append(ExaminationThirdCategoryInfo.from_alipay_dict(i))
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def is_leaf(self):
        return self._is_leaf

    @is_leaf.setter
    def is_leaf(self, value):
        self._is_leaf = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        self._parent_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.category_state:
            if hasattr(self.category_state, 'to_alipay_dict'):
                params['category_state'] = self.category_state.to_alipay_dict()
            else:
                params['category_state'] = self.category_state
        if self.category_type:
            if hasattr(self.category_type, 'to_alipay_dict'):
                params['category_type'] = self.category_type.to_alipay_dict()
            else:
                params['category_type'] = self.category_type
        if self.children_list:
            if isinstance(self.children_list, list):
                for i in range(0, len(self.children_list)):
                    element = self.children_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.children_list[i] = element.to_alipay_dict()
            if hasattr(self.children_list, 'to_alipay_dict'):
                params['children_list'] = self.children_list.to_alipay_dict()
            else:
                params['children_list'] = self.children_list
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.is_leaf:
            if hasattr(self.is_leaf, 'to_alipay_dict'):
                params['is_leaf'] = self.is_leaf.to_alipay_dict()
            else:
                params['is_leaf'] = self.is_leaf
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.parent_id:
            if hasattr(self.parent_id, 'to_alipay_dict'):
                params['parent_id'] = self.parent_id.to_alipay_dict()
            else:
                params['parent_id'] = self.parent_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExaminationSecondCategoryInfo()
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'category_state' in d:
            o.category_state = d['category_state']
        if 'category_type' in d:
            o.category_type = d['category_type']
        if 'children_list' in d:
            o.children_list = d['children_list']
        if 'id' in d:
            o.id = d['id']
        if 'is_leaf' in d:
            o.is_leaf = d['is_leaf']
        if 'level' in d:
            o.level = d['level']
        if 'parent_id' in d:
            o.parent_id = d['parent_id']
        return o


