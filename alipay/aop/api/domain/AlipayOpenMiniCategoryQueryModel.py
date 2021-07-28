#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniCategoryQueryModel(object):

    def __init__(self):
        self._is_filter = None

    @property
    def is_filter(self):
        return self._is_filter

    @is_filter.setter
    def is_filter(self, value):
        self._is_filter = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_filter:
            if hasattr(self.is_filter, 'to_alipay_dict'):
                params['is_filter'] = self.is_filter.to_alipay_dict()
            else:
                params['is_filter'] = self.is_filter
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniCategoryQueryModel()
        if 'is_filter' in d:
            o.is_filter = d['is_filter']
        return o


