#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OperateTask(object):

    def __init__(self):
        self._operation_params = None
        self._operation_type = None
        self._task_id = None

    @property
    def operation_params(self):
        return self._operation_params

    @operation_params.setter
    def operation_params(self, value):
        self._operation_params = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.operation_params:
            if hasattr(self.operation_params, 'to_alipay_dict'):
                params['operation_params'] = self.operation_params.to_alipay_dict()
            else:
                params['operation_params'] = self.operation_params
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
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
        o = OperateTask()
        if 'operation_params' in d:
            o.operation_params = d['operation_params']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


