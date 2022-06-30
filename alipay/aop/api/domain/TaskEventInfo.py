#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskEventInfo(object):

    def __init__(self):
        self._task_event_id = None
        self._task_event_type = None

    @property
    def task_event_id(self):
        return self._task_event_id

    @task_event_id.setter
    def task_event_id(self, value):
        self._task_event_id = value
    @property
    def task_event_type(self):
        return self._task_event_type

    @task_event_type.setter
    def task_event_type(self, value):
        self._task_event_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.task_event_id:
            if hasattr(self.task_event_id, 'to_alipay_dict'):
                params['task_event_id'] = self.task_event_id.to_alipay_dict()
            else:
                params['task_event_id'] = self.task_event_id
        if self.task_event_type:
            if hasattr(self.task_event_type, 'to_alipay_dict'):
                params['task_event_type'] = self.task_event_type.to_alipay_dict()
            else:
                params['task_event_type'] = self.task_event_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskEventInfo()
        if 'task_event_id' in d:
            o.task_event_id = d['task_event_id']
        if 'task_event_type' in d:
            o.task_event_type = d['task_event_type']
        return o


