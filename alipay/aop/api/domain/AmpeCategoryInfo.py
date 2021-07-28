#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AmpeCategoryInfo(object):

    def __init__(self):
        self._category_desc = None
        self._category_id = None

    @property
    def category_desc(self):
        return self._category_desc

    @category_desc.setter
    def category_desc(self, value):
        self._category_desc = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_desc:
            if hasattr(self.category_desc, 'to_alipay_dict'):
                params['category_desc'] = self.category_desc.to_alipay_dict()
            else:
                params['category_desc'] = self.category_desc
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AmpeCategoryInfo()
        if 'category_desc' in d:
            o.category_desc = d['category_desc']
        if 'category_id' in d:
            o.category_id = d['category_id']
        return o


