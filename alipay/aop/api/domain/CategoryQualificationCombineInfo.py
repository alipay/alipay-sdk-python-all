#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CategoryQualificationInfo import CategoryQualificationInfo
from alipay.aop.api.domain.GroupPurchaseCategoryInfo import GroupPurchaseCategoryInfo


class CategoryQualificationCombineInfo(object):

    def __init__(self):
        self._qualification_list = None
        self._rel_category_list = None

    @property
    def qualification_list(self):
        return self._qualification_list

    @qualification_list.setter
    def qualification_list(self, value):
        if isinstance(value, list):
            self._qualification_list = list()
            for i in value:
                if isinstance(i, CategoryQualificationInfo):
                    self._qualification_list.append(i)
                else:
                    self._qualification_list.append(CategoryQualificationInfo.from_alipay_dict(i))
    @property
    def rel_category_list(self):
        return self._rel_category_list

    @rel_category_list.setter
    def rel_category_list(self, value):
        if isinstance(value, list):
            self._rel_category_list = list()
            for i in value:
                if isinstance(i, GroupPurchaseCategoryInfo):
                    self._rel_category_list.append(i)
                else:
                    self._rel_category_list.append(GroupPurchaseCategoryInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.qualification_list:
            if isinstance(self.qualification_list, list):
                for i in range(0, len(self.qualification_list)):
                    element = self.qualification_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.qualification_list[i] = element.to_alipay_dict()
            if hasattr(self.qualification_list, 'to_alipay_dict'):
                params['qualification_list'] = self.qualification_list.to_alipay_dict()
            else:
                params['qualification_list'] = self.qualification_list
        if self.rel_category_list:
            if isinstance(self.rel_category_list, list):
                for i in range(0, len(self.rel_category_list)):
                    element = self.rel_category_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rel_category_list[i] = element.to_alipay_dict()
            if hasattr(self.rel_category_list, 'to_alipay_dict'):
                params['rel_category_list'] = self.rel_category_list.to_alipay_dict()
            else:
                params['rel_category_list'] = self.rel_category_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CategoryQualificationCombineInfo()
        if 'qualification_list' in d:
            o.qualification_list = d['qualification_list']
        if 'rel_category_list' in d:
            o.rel_category_list = d['rel_category_list']
        return o


