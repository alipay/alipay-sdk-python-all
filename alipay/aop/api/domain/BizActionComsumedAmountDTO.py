#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizActionComsumedAmountDTO(object):

    def __init__(self):
        self._biz_budget_apply_code = None
        self._biz_uk_id = None
        self._consumed_amount = None

    @property
    def biz_budget_apply_code(self):
        return self._biz_budget_apply_code

    @biz_budget_apply_code.setter
    def biz_budget_apply_code(self, value):
        self._biz_budget_apply_code = value
    @property
    def biz_uk_id(self):
        return self._biz_uk_id

    @biz_uk_id.setter
    def biz_uk_id(self, value):
        self._biz_uk_id = value
    @property
    def consumed_amount(self):
        return self._consumed_amount

    @consumed_amount.setter
    def consumed_amount(self, value):
        self._consumed_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_budget_apply_code:
            if hasattr(self.biz_budget_apply_code, 'to_alipay_dict'):
                params['biz_budget_apply_code'] = self.biz_budget_apply_code.to_alipay_dict()
            else:
                params['biz_budget_apply_code'] = self.biz_budget_apply_code
        if self.biz_uk_id:
            if hasattr(self.biz_uk_id, 'to_alipay_dict'):
                params['biz_uk_id'] = self.biz_uk_id.to_alipay_dict()
            else:
                params['biz_uk_id'] = self.biz_uk_id
        if self.consumed_amount:
            if hasattr(self.consumed_amount, 'to_alipay_dict'):
                params['consumed_amount'] = self.consumed_amount.to_alipay_dict()
            else:
                params['consumed_amount'] = self.consumed_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizActionComsumedAmountDTO()
        if 'biz_budget_apply_code' in d:
            o.biz_budget_apply_code = d['biz_budget_apply_code']
        if 'biz_uk_id' in d:
            o.biz_uk_id = d['biz_uk_id']
        if 'consumed_amount' in d:
            o.consumed_amount = d['consumed_amount']
        return o


