#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConditionEntry import ConditionEntry


class MultiDimAuthAmountQuery(object):

    def __init__(self):
        self._auth_biz_type = None
        self._dim_conditions = None
        self._package_code = None

    @property
    def auth_biz_type(self):
        return self._auth_biz_type

    @auth_biz_type.setter
    def auth_biz_type(self, value):
        self._auth_biz_type = value
    @property
    def dim_conditions(self):
        return self._dim_conditions

    @dim_conditions.setter
    def dim_conditions(self, value):
        if isinstance(value, list):
            self._dim_conditions = list()
            for i in value:
                if isinstance(i, ConditionEntry):
                    self._dim_conditions.append(i)
                else:
                    self._dim_conditions.append(ConditionEntry.from_alipay_dict(i))
    @property
    def package_code(self):
        return self._package_code

    @package_code.setter
    def package_code(self, value):
        self._package_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_biz_type:
            if hasattr(self.auth_biz_type, 'to_alipay_dict'):
                params['auth_biz_type'] = self.auth_biz_type.to_alipay_dict()
            else:
                params['auth_biz_type'] = self.auth_biz_type
        if self.dim_conditions:
            if isinstance(self.dim_conditions, list):
                for i in range(0, len(self.dim_conditions)):
                    element = self.dim_conditions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dim_conditions[i] = element.to_alipay_dict()
            if hasattr(self.dim_conditions, 'to_alipay_dict'):
                params['dim_conditions'] = self.dim_conditions.to_alipay_dict()
            else:
                params['dim_conditions'] = self.dim_conditions
        if self.package_code:
            if hasattr(self.package_code, 'to_alipay_dict'):
                params['package_code'] = self.package_code.to_alipay_dict()
            else:
                params['package_code'] = self.package_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MultiDimAuthAmountQuery()
        if 'auth_biz_type' in d:
            o.auth_biz_type = d['auth_biz_type']
        if 'dim_conditions' in d:
            o.dim_conditions = d['dim_conditions']
        if 'package_code' in d:
            o.package_code = d['package_code']
        return o


