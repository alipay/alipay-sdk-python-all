#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAccountExrateConfigSyncModel(object):

    def __init__(self):
        self._task_context = None
        self._task_status = None
        self._task_type = None

    @property
    def task_context(self):
        return self._task_context

    @task_context.setter
    def task_context(self, value):
        self._task_context = value
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.task_context:
            if hasattr(self.task_context, 'to_alipay_dict'):
                params['task_context'] = self.task_context.to_alipay_dict()
            else:
                params['task_context'] = self.task_context
        if self.task_status:
            if hasattr(self.task_status, 'to_alipay_dict'):
                params['task_status'] = self.task_status.to_alipay_dict()
            else:
                params['task_status'] = self.task_status
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = self.task_type.to_alipay_dict()
            else:
                params['task_type'] = self.task_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountExrateConfigSyncModel()
        if 'task_context' in d:
            o.task_context = d['task_context']
        if 'task_status' in d:
            o.task_status = d['task_status']
        if 'task_type' in d:
            o.task_type = d['task_type']
        return o


