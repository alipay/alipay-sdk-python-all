#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniMultiAuditModifyModel(object):

    def __init__(self):
        self._memo = None
        self._operate_result = None
        self._operate_type = None
        self._task_id = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operate_result(self):
        return self._operate_result

    @operate_result.setter
    def operate_result(self, value):
        self._operate_result = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operate_result:
            if hasattr(self.operate_result, 'to_alipay_dict'):
                params['operate_result'] = self.operate_result.to_alipay_dict()
            else:
                params['operate_result'] = self.operate_result
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniMultiAuditModifyModel()
        if 'memo' in d:
            o.memo = d['memo']
        if 'operate_result' in d:
            o.operate_result = d['operate_result']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


