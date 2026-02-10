#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AxfItemCategoryQualificationReq import AxfItemCategoryQualificationReq


class AlipayCommerceLifeserviceCategorySignModel(object):

    def __init__(self):
        self._category_code = None
        self._qualification_info = None

    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def qualification_info(self):
        return self._qualification_info

    @qualification_info.setter
    def qualification_info(self, value):
        if isinstance(value, list):
            self._qualification_info = list()
            for i in value:
                if isinstance(i, AxfItemCategoryQualificationReq):
                    self._qualification_info.append(i)
                else:
                    self._qualification_info.append(AxfItemCategoryQualificationReq.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.qualification_info:
            if isinstance(self.qualification_info, list):
                for i in range(0, len(self.qualification_info)):
                    element = self.qualification_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.qualification_info[i] = element.to_alipay_dict()
            if hasattr(self.qualification_info, 'to_alipay_dict'):
                params['qualification_info'] = self.qualification_info.to_alipay_dict()
            else:
                params['qualification_info'] = self.qualification_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLifeserviceCategorySignModel()
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'qualification_info' in d:
            o.qualification_info = d['qualification_info']
        return o


