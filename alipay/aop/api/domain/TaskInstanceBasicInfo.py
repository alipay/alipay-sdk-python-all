#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskInstanceBasicInfo(object):

    def __init__(self):
        self._logo = None
        self._published_point_amount = None
        self._status = None
        self._task_end_time = None
        self._task_instance_id = None
        self._task_name = None
        self._task_start_time = None
        self._task_template_id = None
        self._task_type = None
        self._total_point_amount = None

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def published_point_amount(self):
        return self._published_point_amount

    @published_point_amount.setter
    def published_point_amount(self, value):
        self._published_point_amount = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_end_time(self):
        return self._task_end_time

    @task_end_time.setter
    def task_end_time(self, value):
        self._task_end_time = value
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
    def task_start_time(self):
        return self._task_start_time

    @task_start_time.setter
    def task_start_time(self, value):
        self._task_start_time = value
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
    def total_point_amount(self):
        return self._total_point_amount

    @total_point_amount.setter
    def total_point_amount(self, value):
        self._total_point_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.published_point_amount:
            if hasattr(self.published_point_amount, 'to_alipay_dict'):
                params['published_point_amount'] = self.published_point_amount.to_alipay_dict()
            else:
                params['published_point_amount'] = self.published_point_amount
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.task_end_time:
            if hasattr(self.task_end_time, 'to_alipay_dict'):
                params['task_end_time'] = self.task_end_time.to_alipay_dict()
            else:
                params['task_end_time'] = self.task_end_time
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
        if self.task_start_time:
            if hasattr(self.task_start_time, 'to_alipay_dict'):
                params['task_start_time'] = self.task_start_time.to_alipay_dict()
            else:
                params['task_start_time'] = self.task_start_time
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
        if self.total_point_amount:
            if hasattr(self.total_point_amount, 'to_alipay_dict'):
                params['total_point_amount'] = self.total_point_amount.to_alipay_dict()
            else:
                params['total_point_amount'] = self.total_point_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskInstanceBasicInfo()
        if 'logo' in d:
            o.logo = d['logo']
        if 'published_point_amount' in d:
            o.published_point_amount = d['published_point_amount']
        if 'status' in d:
            o.status = d['status']
        if 'task_end_time' in d:
            o.task_end_time = d['task_end_time']
        if 'task_instance_id' in d:
            o.task_instance_id = d['task_instance_id']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_start_time' in d:
            o.task_start_time = d['task_start_time']
        if 'task_template_id' in d:
            o.task_template_id = d['task_template_id']
        if 'task_type' in d:
            o.task_type = d['task_type']
        if 'total_point_amount' in d:
            o.total_point_amount = d['total_point_amount']
        return o


