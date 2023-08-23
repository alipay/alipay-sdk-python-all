#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceSubTaskCreateOpenapiResult(object):

    def __init__(self):
        self._sub_task_id = None
        self._sub_task_type = None
        self._task_index = None

    @property
    def sub_task_id(self):
        return self._sub_task_id

    @sub_task_id.setter
    def sub_task_id(self, value):
        self._sub_task_id = value
    @property
    def sub_task_type(self):
        return self._sub_task_type

    @sub_task_type.setter
    def sub_task_type(self, value):
        self._sub_task_type = value
    @property
    def task_index(self):
        return self._task_index

    @task_index.setter
    def task_index(self, value):
        self._task_index = value


    def to_alipay_dict(self):
        params = dict()
        if self.sub_task_id:
            if hasattr(self.sub_task_id, 'to_alipay_dict'):
                params['sub_task_id'] = self.sub_task_id.to_alipay_dict()
            else:
                params['sub_task_id'] = self.sub_task_id
        if self.sub_task_type:
            if hasattr(self.sub_task_type, 'to_alipay_dict'):
                params['sub_task_type'] = self.sub_task_type.to_alipay_dict()
            else:
                params['sub_task_type'] = self.sub_task_type
        if self.task_index:
            if hasattr(self.task_index, 'to_alipay_dict'):
                params['task_index'] = self.task_index.to_alipay_dict()
            else:
                params['task_index'] = self.task_index
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceSubTaskCreateOpenapiResult()
        if 'sub_task_id' in d:
            o.sub_task_id = d['sub_task_id']
        if 'sub_task_type' in d:
            o.sub_task_type = d['sub_task_type']
        if 'task_index' in d:
            o.task_index = d['task_index']
        return o


