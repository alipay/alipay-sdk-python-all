#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubAccountInfoQueryOrder import SubAccountInfoQueryOrder


class AlipayBossFncSubaccountAccountQueryModel(object):

    def __init__(self):
        self._sub_account_info_query_order = None

    @property
    def sub_account_info_query_order(self):
        return self._sub_account_info_query_order

    @sub_account_info_query_order.setter
    def sub_account_info_query_order(self, value):
        if isinstance(value, SubAccountInfoQueryOrder):
            self._sub_account_info_query_order = value
        else:
            self._sub_account_info_query_order = SubAccountInfoQueryOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.sub_account_info_query_order:
            if hasattr(self.sub_account_info_query_order, 'to_alipay_dict'):
                params['sub_account_info_query_order'] = self.sub_account_info_query_order.to_alipay_dict()
            else:
                params['sub_account_info_query_order'] = self.sub_account_info_query_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncSubaccountAccountQueryModel()
        if 'sub_account_info_query_order' in d:
            o.sub_account_info_query_order = d['sub_account_info_query_order']
        return o


