#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvestigCategoryData import InvestigCategoryData


class InvestigCategoryResult(object):

    def __init__(self):
        self._category = None
        self._category_result = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def category_result(self):
        return self._category_result

    @category_result.setter
    def category_result(self, value):
        if isinstance(value, list):
            self._category_result = list()
            for i in value:
                if isinstance(i, InvestigCategoryData):
                    self._category_result.append(i)
                else:
                    self._category_result.append(InvestigCategoryData.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.category_result:
            if isinstance(self.category_result, list):
                for i in range(0, len(self.category_result)):
                    element = self.category_result[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_result[i] = element.to_alipay_dict()
            if hasattr(self.category_result, 'to_alipay_dict'):
                params['category_result'] = self.category_result.to_alipay_dict()
            else:
                params['category_result'] = self.category_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvestigCategoryResult()
        if 'category' in d:
            o.category = d['category']
        if 'category_result' in d:
            o.category_result = d['category_result']
        return o


