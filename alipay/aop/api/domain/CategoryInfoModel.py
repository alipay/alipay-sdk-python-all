#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CategoryInfoModel(object):

    def __init__(self):
        self._category_code = None
        self._main_name = None
        self._name_list = None

    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def main_name(self):
        return self._main_name

    @main_name.setter
    def main_name(self, value):
        self._main_name = value
    @property
    def name_list(self):
        return self._name_list

    @name_list.setter
    def name_list(self, value):
        if isinstance(value, list):
            self._name_list = list()
            for i in value:
                self._name_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.main_name:
            if hasattr(self.main_name, 'to_alipay_dict'):
                params['main_name'] = self.main_name.to_alipay_dict()
            else:
                params['main_name'] = self.main_name
        if self.name_list:
            if isinstance(self.name_list, list):
                for i in range(0, len(self.name_list)):
                    element = self.name_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.name_list[i] = element.to_alipay_dict()
            if hasattr(self.name_list, 'to_alipay_dict'):
                params['name_list'] = self.name_list.to_alipay_dict()
            else:
                params['name_list'] = self.name_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CategoryInfoModel()
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'main_name' in d:
            o.main_name = d['main_name']
        if 'name_list' in d:
            o.name_list = d['name_list']
        return o


