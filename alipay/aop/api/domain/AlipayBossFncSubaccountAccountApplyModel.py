#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApplySubAccountAndBindOrder import ApplySubAccountAndBindOrder


class AlipayBossFncSubaccountAccountApplyModel(object):

    def __init__(self):
        self._apply_sub_account_and_bind_order = None

    @property
    def apply_sub_account_and_bind_order(self):
        return self._apply_sub_account_and_bind_order

    @apply_sub_account_and_bind_order.setter
    def apply_sub_account_and_bind_order(self, value):
        if isinstance(value, ApplySubAccountAndBindOrder):
            self._apply_sub_account_and_bind_order = value
        else:
            self._apply_sub_account_and_bind_order = ApplySubAccountAndBindOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.apply_sub_account_and_bind_order:
            if hasattr(self.apply_sub_account_and_bind_order, 'to_alipay_dict'):
                params['apply_sub_account_and_bind_order'] = self.apply_sub_account_and_bind_order.to_alipay_dict()
            else:
                params['apply_sub_account_and_bind_order'] = self.apply_sub_account_and_bind_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncSubaccountAccountApplyModel()
        if 'apply_sub_account_and_bind_order' in d:
            o.apply_sub_account_and_bind_order = d['apply_sub_account_and_bind_order']
        return o


