#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WithdrawExtend(object):

    def __init__(self):
        self._category_condition = None

    @property
    def category_condition(self):
        return self._category_condition

    @category_condition.setter
    def category_condition(self, value):
        self._category_condition = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_condition:
            if hasattr(self.category_condition, 'to_alipay_dict'):
                params['category_condition'] = self.category_condition.to_alipay_dict()
            else:
                params['category_condition'] = self.category_condition
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WithdrawExtend()
        if 'category_condition' in d:
            o.category_condition = d['category_condition']
        return o


