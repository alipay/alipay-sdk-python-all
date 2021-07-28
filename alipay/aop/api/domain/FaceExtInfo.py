#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FaceExtInfo(object):

    def __init__(self):
        self._max_age = None
        self._min_age = None
        self._query_type = None

    @property
    def max_age(self):
        return self._max_age

    @max_age.setter
    def max_age(self, value):
        self._max_age = value
    @property
    def min_age(self):
        return self._min_age

    @min_age.setter
    def min_age(self, value):
        self._min_age = value
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_age:
            if hasattr(self.max_age, 'to_alipay_dict'):
                params['max_age'] = self.max_age.to_alipay_dict()
            else:
                params['max_age'] = self.max_age
        if self.min_age:
            if hasattr(self.min_age, 'to_alipay_dict'):
                params['min_age'] = self.min_age.to_alipay_dict()
            else:
                params['min_age'] = self.min_age
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FaceExtInfo()
        if 'max_age' in d:
            o.max_age = d['max_age']
        if 'min_age' in d:
            o.min_age = d['min_age']
        if 'query_type' in d:
            o.query_type = d['query_type']
        return o


