#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLifeserviceCategoryBatchqueryModel(object):

    def __init__(self):
        self._parent_category_code = None

    @property
    def parent_category_code(self):
        return self._parent_category_code

    @parent_category_code.setter
    def parent_category_code(self, value):
        self._parent_category_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.parent_category_code:
            if hasattr(self.parent_category_code, 'to_alipay_dict'):
                params['parent_category_code'] = self.parent_category_code.to_alipay_dict()
            else:
                params['parent_category_code'] = self.parent_category_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLifeserviceCategoryBatchqueryModel()
        if 'parent_category_code' in d:
            o.parent_category_code = d['parent_category_code']
        return o


