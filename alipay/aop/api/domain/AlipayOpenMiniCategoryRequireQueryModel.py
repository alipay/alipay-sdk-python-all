#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniCategoryRequireQueryModel(object):

    def __init__(self):
        self._category_code_list = None

    @property
    def category_code_list(self):
        return self._category_code_list

    @category_code_list.setter
    def category_code_list(self, value):
        if isinstance(value, list):
            self._category_code_list = list()
            for i in value:
                self._category_code_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.category_code_list:
            if isinstance(self.category_code_list, list):
                for i in range(0, len(self.category_code_list)):
                    element = self.category_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_code_list[i] = element.to_alipay_dict()
            if hasattr(self.category_code_list, 'to_alipay_dict'):
                params['category_code_list'] = self.category_code_list.to_alipay_dict()
            else:
                params['category_code_list'] = self.category_code_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniCategoryRequireQueryModel()
        if 'category_code_list' in d:
            o.category_code_list = d['category_code_list']
        return o


