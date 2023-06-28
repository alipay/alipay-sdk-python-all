#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskInstanceBasicInfoDTO(object):

    def __init__(self):
        self._complete_time = None
        self._published_amount = None
        self._receive_time = None
        self._status = None
        self._task_instance_id = None
        self._task_name = None
        self._task_template_id = None
        self._task_type = None
        self._total_amount = None

    @property
    def complete_time(self):
        return self._complete_time

    @complete_time.setter
    def complete_time(self, value):
        self._complete_time = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_instance_id(self):
        return self._task_instance_id

    @task_instance_id.setter
    def task_instance_id(self, value):
        self._task_instance_id = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_template_id(self):
        return self._task_template_id

    @task_template_id.setter
    def task_template_id(self, value):
        self._task_template_id = value
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.task_instance_id:
            if hasattr(self.task_instance_id, 'to_alipay_dict'):
                params['task_instance_id'] = self.task_instance_id.to_alipay_dict()
            else:
                params['task_instance_id'] = self.task_instance_id
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.task_template_id:
            if hasattr(self.task_template_id, 'to_alipay_dict'):
                params['task_template_id'] = self.task_template_id.to_alipay_dict()
            else:
                params['task_template_id'] = self.task_template_id
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
        o = TaskInstanceBasicInfoDTO()
        if 'complete_time' in d:
            o.complete_time = d['complete_time']
        if 'published_amount' in d:
            o.published_amount = d['published_amount']
        if 'receive_time' in d:
            o.receive_time = d['receive_time']
        if 'status' in d:
            o.status = d['status']
        if 'task_instance_id' in d:
            o.task_instance_id = d['task_instance_id']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_template_id' in d:
            o.task_template_id = d['task_template_id']
        if 'task_type' in d:
            o.task_type = d['task_type']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


