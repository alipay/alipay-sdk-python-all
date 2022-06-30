#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskPrizeInfo(object):

    def __init__(self):
        self._prize_id = None
        self._prize_template_id = None
        self._prize_type = None
        self._task_event_id = None
        self._task_event_type = None

    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def prize_template_id(self):
        return self._prize_template_id

    @prize_template_id.setter
    def prize_template_id(self, value):
        self._prize_template_id = value
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value
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
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.prize_template_id:
            if hasattr(self.prize_template_id, 'to_alipay_dict'):
                params['prize_template_id'] = self.prize_template_id.to_alipay_dict()
            else:
                params['prize_template_id'] = self.prize_template_id
        if self.prize_type:
            if hasattr(self.prize_type, 'to_alipay_dict'):
                params['prize_type'] = self.prize_type.to_alipay_dict()
            else:
                params['prize_type'] = self.prize_type
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
        o = TaskPrizeInfo()
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_template_id' in d:
            o.prize_template_id = d['prize_template_id']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        if 'task_event_id' in d:
            o.task_event_id = d['task_event_id']
        if 'task_event_type' in d:
            o.task_event_type = d['task_event_type']
        return o


