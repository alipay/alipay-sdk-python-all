#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingActivityDeductConsultModel(object):

    def __init__(self):
        self._available_app_id = None
        self._mini_trace_info = None
        self._order_amount = None

    @property
    def available_app_id(self):
        return self._available_app_id

    @available_app_id.setter
    def available_app_id(self, value):
        self._available_app_id = value
    @property
    def mini_trace_info(self):
        return self._mini_trace_info

    @mini_trace_info.setter
    def mini_trace_info(self, value):
        self._mini_trace_info = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_app_id:
            if hasattr(self.available_app_id, 'to_alipay_dict'):
                params['available_app_id'] = self.available_app_id.to_alipay_dict()
            else:
                params['available_app_id'] = self.available_app_id
        if self.mini_trace_info:
            if hasattr(self.mini_trace_info, 'to_alipay_dict'):
                params['mini_trace_info'] = self.mini_trace_info.to_alipay_dict()
            else:
                params['mini_trace_info'] = self.mini_trace_info
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingActivityDeductConsultModel()
        if 'available_app_id' in d:
            o.available_app_id = d['available_app_id']
        if 'mini_trace_info' in d:
            o.mini_trace_info = d['mini_trace_info']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        return o


