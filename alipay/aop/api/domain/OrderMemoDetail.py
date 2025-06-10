#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AxfOrderMemoInfo import AxfOrderMemoInfo


class OrderMemoDetail(object):

    def __init__(self):
        self._axf_order_memo_info = None
        self._operate_time = None
        self._operate_type = None
        self._operator = None

    @property
    def axf_order_memo_info(self):
        return self._axf_order_memo_info

    @axf_order_memo_info.setter
    def axf_order_memo_info(self, value):
        if isinstance(value, AxfOrderMemoInfo):
            self._axf_order_memo_info = value
        else:
            self._axf_order_memo_info = AxfOrderMemoInfo.from_alipay_dict(value)
    @property
    def operate_time(self):
        return self._operate_time

    @operate_time.setter
    def operate_time(self, value):
        self._operate_time = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value


    def to_alipay_dict(self):
        params = dict()
        if self.axf_order_memo_info:
            if hasattr(self.axf_order_memo_info, 'to_alipay_dict'):
                params['axf_order_memo_info'] = self.axf_order_memo_info.to_alipay_dict()
            else:
                params['axf_order_memo_info'] = self.axf_order_memo_info
        if self.operate_time:
            if hasattr(self.operate_time, 'to_alipay_dict'):
                params['operate_time'] = self.operate_time.to_alipay_dict()
            else:
                params['operate_time'] = self.operate_time
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderMemoDetail()
        if 'axf_order_memo_info' in d:
            o.axf_order_memo_info = d['axf_order_memo_info']
        if 'operate_time' in d:
            o.operate_time = d['operate_time']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'operator' in d:
            o.operator = d['operator']
        return o


