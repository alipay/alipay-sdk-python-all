#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskInstanceInfoDTO(object):

    def __init__(self):
        self._complete_time = None
        self._current_num = None
        self._max_incentive_count = None
        self._published_amount = None
        self._receive_time = None
        self._reward_type = None
        self._status = None
        self._target_num = None
        self._task_name = None
        self._task_type = None
        self._total_amount = None

    @property
    def complete_time(self):
        return self._complete_time

    @complete_time.setter
    def complete_time(self, value):
        self._complete_time = value
    @property
    def current_num(self):
        return self._current_num

    @current_num.setter
    def current_num(self, value):
        self._current_num = value
    @property
    def max_incentive_count(self):
        return self._max_incentive_count

    @max_incentive_count.setter
    def max_incentive_count(self, value):
        self._max_incentive_count = value
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
    def reward_type(self):
        return self._reward_type

    @reward_type.setter
    def reward_type(self, value):
        self._reward_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def target_num(self):
        return self._target_num

    @target_num.setter
    def target_num(self, value):
        self._target_num = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.complete_time:
            if hasattr(self.complete_time, 'to_alipay_dict'):
                params['complete_time'] = self.complete_time.to_alipay_dict()
            else:
                params['complete_time'] = self.complete_time
        if self.current_num:
            if hasattr(self.current_num, 'to_alipay_dict'):
                params['current_num'] = self.current_num.to_alipay_dict()
            else:
                params['current_num'] = self.current_num
        if self.max_incentive_count:
            if hasattr(self.max_incentive_count, 'to_alipay_dict'):
                params['max_incentive_count'] = self.max_incentive_count.to_alipay_dict()
            else:
                params['max_incentive_count'] = self.max_incentive_count
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
        if self.reward_type:
            if hasattr(self.reward_type, 'to_alipay_dict'):
                params['reward_type'] = self.reward_type.to_alipay_dict()
            else:
                params['reward_type'] = self.reward_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.target_num:
            if hasattr(self.target_num, 'to_alipay_dict'):
                params['target_num'] = self.target_num.to_alipay_dict()
            else:
                params['target_num'] = self.target_num
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = self.task_type.to_alipay_dict()
            else:
                params['task_type'] = self.task_type
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
        o = TaskInstanceInfoDTO()
        if 'complete_time' in d:
            o.complete_time = d['complete_time']
        if 'current_num' in d:
            o.current_num = d['current_num']
        if 'max_incentive_count' in d:
            o.max_incentive_count = d['max_incentive_count']
        if 'published_amount' in d:
            o.published_amount = d['published_amount']
        if 'receive_time' in d:
            o.receive_time = d['receive_time']
        if 'reward_type' in d:
            o.reward_type = d['reward_type']
        if 'status' in d:
            o.status = d['status']
        if 'target_num' in d:
            o.target_num = d['target_num']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_type' in d:
            o.task_type = d['task_type']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


