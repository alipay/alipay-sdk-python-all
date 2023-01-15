#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DisposalResult(object):

    def __init__(self):
        self._end_time = None
        self._entity_id = None
        self._start_time = None
        self._status = None
        self._strategy_code = None
        self._task_code = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value
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
    def strategy_code(self):
        return self._strategy_code

    @strategy_code.setter
    def strategy_code(self, value):
        self._strategy_code = value
    @property
    def task_code(self):
        return self._task_code

    @task_code.setter
    def task_code(self, value):
        self._task_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.entity_id:
            if hasattr(self.entity_id, 'to_alipay_dict'):
                params['entity_id'] = self.entity_id.to_alipay_dict()
            else:
                params['entity_id'] = self.entity_id
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
        if self.strategy_code:
            if hasattr(self.strategy_code, 'to_alipay_dict'):
                params['strategy_code'] = self.strategy_code.to_alipay_dict()
            else:
                params['strategy_code'] = self.strategy_code
        if self.task_code:
            if hasattr(self.task_code, 'to_alipay_dict'):
                params['task_code'] = self.task_code.to_alipay_dict()
            else:
                params['task_code'] = self.task_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DisposalResult()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'entity_id' in d:
            o.entity_id = d['entity_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'strategy_code' in d:
            o.strategy_code = d['strategy_code']
        if 'task_code' in d:
            o.task_code = d['task_code']
        return o


