#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishPropertyValueInfo(object):

    def __init__(self):
        self._sort = None
        self._value = None

    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishPropertyValueInfo()
        if 'sort' in d:
            o.sort = d['sort']
        if 'value' in d:
            o.value = d['value']
        return o


