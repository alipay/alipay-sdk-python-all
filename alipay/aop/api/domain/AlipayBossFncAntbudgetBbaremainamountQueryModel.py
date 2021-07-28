#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncAntbudgetBbaremainamountQueryModel(object):

    def __init__(self):
        self._biz_budget_apply_code = None

    @property
    def biz_budget_apply_code(self):
        return self._biz_budget_apply_code

    @biz_budget_apply_code.setter
    def biz_budget_apply_code(self, value):
        self._biz_budget_apply_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_budget_apply_code:
            if hasattr(self.biz_budget_apply_code, 'to_alipay_dict'):
                params['biz_budget_apply_code'] = self.biz_budget_apply_code.to_alipay_dict()
            else:
                params['biz_budget_apply_code'] = self.biz_budget_apply_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncAntbudgetBbaremainamountQueryModel()
        if 'biz_budget_apply_code' in d:
            o.biz_budget_apply_code = d['biz_budget_apply_code']
        return o


