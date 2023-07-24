#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskInstanceRewardInfoDTO(object):

    def __init__(self):
        self._current_num = None
        self._guided_finish_time = None
        self._hunter_id = None
        self._hunter_open_id = None
        self._published_amount = None
        self._receive_time = None
        self._target_num = None
        self._task_instance_id = None
        self._total_amount = None

    @property
    def current_num(self):
        return self._current_num

    @current_num.setter
    def current_num(self, value):
        self._current_num = value
    @property
    def guided_finish_time(self):
        return self._guided_finish_time

    @guided_finish_time.setter
    def guided_finish_time(self, value):
        self._guided_finish_time = value
    @property
    def hunter_id(self):
        return self._hunter_id

    @hunter_id.setter
    def hunter_id(self, value):
        self._hunter_id = value
    @property
    def hunter_open_id(self):
        return self._hunter_open_id

    @hunter_open_id.setter
    def hunter_open_id(self, value):
        self._hunter_open_id = value
    @property
    def published_amount(self):
        return self._published_amount

    @published_amount.setter
    def published_amount(self, value):
        self._published_amount = value
    @property
    def receive_time(self):
        return self._receive_time

    @receive_time.setter
    def receive_time(self, value):
        self._receive_time = value
    @property
    def target_num(self):
        return self._target_num

    @target_num.setter
    def target_num(self, value):
        self._target_num = value
    @property
    def task_instance_id(self):
        return self._task_instance_id

    @task_instance_id.setter
    def task_instance_id(self, value):
        self._task_instance_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_num:
            if hasattr(self.current_num, 'to_alipay_dict'):
                params['current_num'] = self.current_num.to_alipay_dict()
            else:
                params['current_num'] = self.current_num
        if self.guided_finish_time:
            if hasattr(self.guided_finish_time, 'to_alipay_dict'):
                params['guided_finish_time'] = self.guided_finish_time.to_alipay_dict()
            else:
                params['guided_finish_time'] = self.guided_finish_time
        if self.hunter_id:
            if hasattr(self.hunter_id, 'to_alipay_dict'):
                params['hunter_id'] = self.hunter_id.to_alipay_dict()
            else:
                params['hunter_id'] = self.hunter_id
        if self.hunter_open_id:
            if hasattr(self.hunter_open_id, 'to_alipay_dict'):
                params['hunter_open_id'] = self.hunter_open_id.to_alipay_dict()
            else:
                params['hunter_open_id'] = self.hunter_open_id
        if self.published_amount:
            if hasattr(self.published_amount, 'to_alipay_dict'):
                params['published_amount'] = self.published_amount.to_alipay_dict()
            else:
                params['published_amount'] = self.published_amount
        if self.receive_time:
            if hasattr(self.receive_time, 'to_alipay_dict'):
                params['receive_time'] = self.receive_time.to_alipay_dict()
            else:
                params['receive_time'] = self.receive_time
        if self.target_num:
            if hasattr(self.target_num, 'to_alipay_dict'):
                params['target_num'] = self.target_num.to_alipay_dict()
            else:
                params['target_num'] = self.target_num
        if self.task_instance_id:
            if hasattr(self.task_instance_id, 'to_alipay_dict'):
                params['task_instance_id'] = self.task_instance_id.to_alipay_dict()
            else:
                params['task_instance_id'] = self.task_instance_id
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskInstanceRewardInfoDTO()
        if 'current_num' in d:
            o.current_num = d['current_num']
        if 'guided_finish_time' in d:
            o.guided_finish_time = d['guided_finish_time']
        if 'hunter_id' in d:
            o.hunter_id = d['hunter_id']
        if 'hunter_open_id' in d:
            o.hunter_open_id = d['hunter_open_id']
        if 'published_amount' in d:
            o.published_amount = d['published_amount']
        if 'receive_time' in d:
            o.receive_time = d['receive_time']
        if 'target_num' in d:
            o.target_num = d['target_num']
        if 'task_instance_id' in d:
            o.task_instance_id = d['task_instance_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


