#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FeatureVO import FeatureVO


class QueryCityResp(object):

    def __init__(self):
        self._city_code = None
        self._feature = None
        self._name = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def feature(self):
        return self._feature

    @feature.setter
    def feature(self, value):
        if isinstance(value, FeatureVO):
            self._feature = value
        else:
            self._feature = FeatureVO.from_alipay_dict(value)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.feature:
            if hasattr(self.feature, 'to_alipay_dict'):
                params['feature'] = self.feature.to_alipay_dict()
            else:
                params['feature'] = self.feature
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryCityResp()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'feature' in d:
            o.feature = d['feature']
        if 'name' in d:
            o.name = d['name']
        return o


