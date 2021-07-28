#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAssetPointPointprodBudgetlibQueryModel(object):

    def __init__(self):
        self._budget_code = None

    @property
    def budget_code(self):
        return self._budget_code

    @budget_code.setter
    def budget_code(self, value):
        self._budget_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.budget_code:
            if hasattr(self.budget_code, 'to_alipay_dict'):
                params['budget_code'] = self.budget_code.to_alipay_dict()
            else:
                params['budget_code'] = self.budget_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAssetPointPointprodBudgetlibQueryModel()
        if 'budget_code' in d:
            o.budget_code = d['budget_code']
        return o


