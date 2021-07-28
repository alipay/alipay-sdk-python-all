#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InterTradeApprovalWorkflowOperateLogVO(object):

    def __init__(self):
        self._biz_type = None
        self._operate_memo = None
        self._operate_type_name = None
        self._operator = None
        self._operator_time = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def operate_memo(self):
        return self._operate_memo

    @operate_memo.setter
    def operate_memo(self, value):
        self._operate_memo = value
    @property
    def operate_type_name(self):
        return self._operate_type_name

    @operate_type_name.setter
    def operate_type_name(self, value):
        self._operate_type_name = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def operator_time(self):
        return self._operator_time

    @operator_time.setter
    def operator_time(self, value):
        self._operator_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.operate_memo:
            if hasattr(self.operate_memo, 'to_alipay_dict'):
                params['operate_memo'] = self.operate_memo.to_alipay_dict()
            else:
                params['operate_memo'] = self.operate_memo
        if self.operate_type_name:
            if hasattr(self.operate_type_name, 'to_alipay_dict'):
                params['operate_type_name'] = self.operate_type_name.to_alipay_dict()
            else:
                params['operate_type_name'] = self.operate_type_name
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.operator_time:
            if hasattr(self.operator_time, 'to_alipay_dict'):
                params['operator_time'] = self.operator_time.to_alipay_dict()
            else:
                params['operator_time'] = self.operator_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InterTradeApprovalWorkflowOperateLogVO()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'operate_memo' in d:
            o.operate_memo = d['operate_memo']
        if 'operate_type_name' in d:
            o.operate_type_name = d['operate_type_name']
        if 'operator' in d:
            o.operator = d['operator']
        if 'operator_time' in d:
            o.operator_time = d['operator_time']
        return o


