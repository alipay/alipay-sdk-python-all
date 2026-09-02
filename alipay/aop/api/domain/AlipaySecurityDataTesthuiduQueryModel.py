#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HuiDuTest import HuiDuTest


class AlipaySecurityDataTesthuiduQueryModel(object):

    def __init__(self):
        self._age = None
        self._user_info = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def user_info(self):
        return self._user_info

    @user_info.setter
    def user_info(self, value):
        if isinstance(value, HuiDuTest):
            self._user_info = value
        else:
            self._user_info = HuiDuTest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.user_info:
            if hasattr(self.user_info, 'to_alipay_dict'):
                params['user_info'] = self.user_info.to_alipay_dict()
            else:
                params['user_info'] = self.user_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataTesthuiduQueryModel()
        if 'age' in d:
            o.age = d['age']
        if 'user_info' in d:
            o.user_info = d['user_info']
        return o


