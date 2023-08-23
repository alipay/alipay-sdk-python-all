#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MongoTaskHistory(object):

    def __init__(self):
        self._process = None
        self._start_time = None
        self._status = None
        self._task_id = None
        self._task_type = None

    @property
    def process(self):
        return self._process

    @process.setter
    def process(self, value):
        self._process = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.process:
            if hasattr(self.process, 'to_alipay_dict'):
                params['process'] = self.process.to_alipay_dict()
            else:
                params['process'] = self.process
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
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
        o = MongoTaskHistory()
        if 'process' in d:
            o.process = d['process']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'task_type' in d:
            o.task_type = d['task_type']
        return o


