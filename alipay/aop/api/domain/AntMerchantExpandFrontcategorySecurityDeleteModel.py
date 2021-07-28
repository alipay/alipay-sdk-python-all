#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandFrontcategorySecurityDeleteModel(object):

    def __init__(self):
        self._front_category_id = None

    @property
    def front_category_id(self):
        return self._front_category_id

    @front_category_id.setter
    def front_category_id(self, value):
        self._front_category_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.front_category_id:
            if hasattr(self.front_category_id, 'to_alipay_dict'):
                params['front_category_id'] = self.front_category_id.to_alipay_dict()
            else:
                params['front_category_id'] = self.front_category_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandFrontcategorySecurityDeleteModel()
        if 'front_category_id' in d:
            o.front_category_id = d['front_category_id']
        return o


