#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FilterTag(object):

    def __init__(self):
        self._code = None
        self._filter_items = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def filter_items(self):
        return self._filter_items

    @filter_items.setter
    def filter_items(self, value):
        self._filter_items = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.filter_items:
            if hasattr(self.filter_items, 'to_alipay_dict'):
                params['filter_items'] = self.filter_items.to_alipay_dict()
            else:
                params['filter_items'] = self.filter_items
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FilterTag()
        if 'code' in d:
            o.code = d['code']
        if 'filter_items' in d:
            o.filter_items = d['filter_items']
        return o


