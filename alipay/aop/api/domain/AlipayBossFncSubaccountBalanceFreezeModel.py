#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubAccountBalanceFreezeOrder import SubAccountBalanceFreezeOrder


class AlipayBossFncSubaccountBalanceFreezeModel(object):

    def __init__(self):
        self._sub_account_balance_freeze_order = None

    @property
    def sub_account_balance_freeze_order(self):
        return self._sub_account_balance_freeze_order

    @sub_account_balance_freeze_order.setter
    def sub_account_balance_freeze_order(self, value):
        if isinstance(value, SubAccountBalanceFreezeOrder):
            self._sub_account_balance_freeze_order = value
        else:
            self._sub_account_balance_freeze_order = SubAccountBalanceFreezeOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.sub_account_balance_freeze_order:
            if hasattr(self.sub_account_balance_freeze_order, 'to_alipay_dict'):
                params['sub_account_balance_freeze_order'] = self.sub_account_balance_freeze_order.to_alipay_dict()
            else:
                params['sub_account_balance_freeze_order'] = self.sub_account_balance_freeze_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncSubaccountBalanceFreezeModel()
        if 'sub_account_balance_freeze_order' in d:
            o.sub_account_balance_freeze_order = d['sub_account_balance_freeze_order']
        return o


