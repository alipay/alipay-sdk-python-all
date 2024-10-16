#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CategoryInfoDTO import CategoryInfoDTO


class SceneCategoryDTO(object):

    def __init__(self):
        self._category_list = None
        self._scene_code = None
        self._scene_name = None

    @property
    def category_list(self):
        return self._category_list

    @category_list.setter
    def category_list(self, value):
        if isinstance(value, list):
            self._category_list = list()
            for i in value:
                if isinstance(i, CategoryInfoDTO):
                    self._category_list.append(i)
                else:
                    self._category_list.append(CategoryInfoDTO.from_alipay_dict(i))
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def scene_name(self):
        return self._scene_name

    @scene_name.setter
    def scene_name(self, value):
        self._scene_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_list:
            if isinstance(self.category_list, list):
                for i in range(0, len(self.category_list)):
                    element = self.category_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_list[i] = element.to_alipay_dict()
            if hasattr(self.category_list, 'to_alipay_dict'):
                params['category_list'] = self.category_list.to_alipay_dict()
            else:
                params['category_list'] = self.category_list
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.scene_name:
            if hasattr(self.scene_name, 'to_alipay_dict'):
                params['scene_name'] = self.scene_name.to_alipay_dict()
            else:
                params['scene_name'] = self.scene_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneCategoryDTO()
        if 'category_list' in d:
            o.category_list = d['category_list']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'scene_name' in d:
            o.scene_name = d['scene_name']
        return o


