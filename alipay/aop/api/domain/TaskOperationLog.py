#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskOperationLog(object):

    def __init__(self):
        self._gmt_opration = None
        self._operation_desc = None
        self._operation_memo = None
        self._operation_type = None
        self._operator_id = None
        self._operator_nick = None

    @property
    def gmt_opration(self):
        return self._gmt_opration

    @gmt_opration.setter
    def gmt_opration(self, value):
        self._gmt_opration = value
    @property
    def operation_desc(self):
        return self._operation_desc

    @operation_desc.setter
    def operation_desc(self, value):
        self._operation_desc = value
    @property
    def operation_memo(self):
        return self._operation_memo

    @operation_memo.setter
    def operation_memo(self, value):
        self._operation_memo = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_nick(self):
        return self._operator_nick

    @operator_nick.setter
    def operator_nick(self, value):
        self._operator_nick = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_opration:
            if hasattr(self.gmt_opration, 'to_alipay_dict'):
                params['gmt_opration'] = self.gmt_opration.to_alipay_dict()
            else:
                params['gmt_opration'] = self.gmt_opration
        if self.operation_desc:
            if hasattr(self.operation_desc, 'to_alipay_dict'):
                params['operation_desc'] = self.operation_desc.to_alipay_dict()
            else:
                params['operation_desc'] = self.operation_desc
        if self.operation_memo:
            if hasattr(self.operation_memo, 'to_alipay_dict'):
                params['operation_memo'] = self.operation_memo.to_alipay_dict()
            else:
                params['operation_memo'] = self.operation_memo
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_nick:
            if hasattr(self.operator_nick, 'to_alipay_dict'):
                params['operator_nick'] = self.operator_nick.to_alipay_dict()
            else:
                params['operator_nick'] = self.operator_nick
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskOperationLog()
        if 'gmt_opration' in d:
            o.gmt_opration = d['gmt_opration']
        if 'operation_desc' in d:
            o.operation_desc = d['operation_desc']
        if 'operation_memo' in d:
            o.operation_memo = d['operation_memo']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_nick' in d:
            o.operator_nick = d['operator_nick']
        return o


