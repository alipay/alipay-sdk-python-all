#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderNsalesOrderCancelModel(object):

    def __init__(self):
        self._sales_entry_order_id = None

    @property
    def sales_entry_order_id(self):
        return self._sales_entry_order_id

    @sales_entry_order_id.setter
    def sales_entry_order_id(self, value):
        self._sales_entry_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.sales_entry_order_id:
            if hasattr(self.sales_entry_order_id, 'to_alipay_dict'):
                params['sales_entry_order_id'] = self.sales_entry_order_id.to_alipay_dict()
            else:
                params['sales_entry_order_id'] = self.sales_entry_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderNsalesOrderCancelModel()
        if 'sales_entry_order_id' in d:
            o.sales_entry_order_id = d['sales_entry_order_id']
        return o


