#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheFirstTwo import RainyComplexTypesTheFirstTwo


class UserInfoDemo(object):

    def __init__(self):
        self._second_level = None

    @property
    def second_level(self):
        return self._second_level

    @second_level.setter
    def second_level(self, value):
        if isinstance(value, RainyComplexTypesTheFirstTwo):
            self._second_level = value
        else:
            self._second_level = RainyComplexTypesTheFirstTwo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.second_level:
            if hasattr(self.second_level, 'to_alipay_dict'):
                params['second_level'] = self.second_level.to_alipay_dict()
            else:
                params['second_level'] = self.second_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserInfoDemo()
        if 'second_level' in d:
            o.second_level = d['second_level']
        return o


