#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLifeserviceCategorytemplateQueryModel(object):

    def __init__(self):
        self._attr_type = None
        self._category_code = None

    @property
    def attr_type(self):
        return self._attr_type

    @attr_type.setter
    def attr_type(self, value):
        self._attr_type = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.attr_type:
            if hasattr(self.attr_type, 'to_alipay_dict'):
                params['attr_type'] = self.attr_type.to_alipay_dict()
            else:
                params['attr_type'] = self.attr_type
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLifeserviceCategorytemplateQueryModel()
        if 'attr_type' in d:
            o.attr_type = d['attr_type']
        if 'category_code' in d:
            o.category_code = d['category_code']
        return o


