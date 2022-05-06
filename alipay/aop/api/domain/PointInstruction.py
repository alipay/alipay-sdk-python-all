#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PointInstruction(object):

    def __init__(self):
        self._action_type = None
        self._point_amount = None
        self._reason = None
        self._status = None
        self._task_name = None
        self._time = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def point_amount(self):
        return self._point_amount

    @point_amount.setter
    def point_amount(self, value):
        self._point_amount = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.point_amount:
            if hasattr(self.point_amount, 'to_alipay_dict'):
                params['point_amount'] = self.point_amount.to_alipay_dict()
            else:
                params['point_amount'] = self.point_amount
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PointInstruction()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'point_amount' in d:
            o.point_amount = d['point_amount']
        if 'reason' in d:
            o.reason = d['reason']
        if 'status' in d:
            o.status = d['status']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'time' in d:
            o.time = d['time']
        return o


