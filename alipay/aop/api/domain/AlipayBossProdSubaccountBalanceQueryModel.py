#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubAccountBalanceQueryOrder import SubAccountBalanceQueryOrder


class AlipayBossProdSubaccountBalanceQueryModel(object):

    def __init__(self):
        self._sub_account_balance_query_order = None

    @property
    def sub_account_balance_query_order(self):
        return self._sub_account_balance_query_order

    @sub_account_balance_query_order.setter
    def sub_account_balance_query_order(self, value):
        if isinstance(value, SubAccountBalanceQueryOrder):
            self._sub_account_balance_query_order = value
        else:
            self._sub_account_balance_query_order = SubAccountBalanceQueryOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.sub_account_balance_query_order:
            if hasattr(self.sub_account_balance_query_order, 'to_alipay_dict'):
                params['sub_account_balance_query_order'] = self.sub_account_balance_query_order.to_alipay_dict()
            else:
                params['sub_account_balance_query_order'] = self.sub_account_balance_query_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdSubaccountBalanceQueryModel()
        if 'sub_account_balance_query_order' in d:
            o.sub_account_balance_query_order = d['sub_account_balance_query_order']
        return o


