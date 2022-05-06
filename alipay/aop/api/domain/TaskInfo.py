#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskInfo(object):

    def __init__(self):
        self._earned_point = None
        self._owner_type = None
        self._task_code = None
        self._task_desc = None
        self._task_end_time = None
        self._task_icon_url = None
        self._task_name = None
        self._task_remain_point = None
        self._task_start_time = None
        self._task_status = None
        self._total_point = None

    @property
    def earned_point(self):
        return self._earned_point

    @earned_point.setter
    def earned_point(self, value):
        self._earned_point = value
    @property
    def owner_type(self):
        return self._owner_type

    @owner_type.setter
    def owner_type(self, value):
        self._owner_type = value
    @property
    def task_code(self):
        return self._task_code

    @task_code.setter
    def task_code(self, value):
        self._task_code = value
    @property
    def task_desc(self):
        return self._task_desc

    @task_desc.setter
    def task_desc(self, value):
        self._task_desc = value
    @property
    def task_end_time(self):
        return self._task_end_time

    @task_end_time.setter
    def task_end_time(self, value):
        self._task_end_time = value
    @property
    def task_icon_url(self):
        return self._task_icon_url

    @task_icon_url.setter
    def task_icon_url(self, value):
        self._task_icon_url = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_remain_point(self):
        return self._task_remain_point

    @task_remain_point.setter
    def task_remain_point(self, value):
        self._task_remain_point = value
    @property
    def task_start_time(self):
        return self._task_start_time

    @task_start_time.setter
    def task_start_time(self, value):
        self._task_start_time = value
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value
    @property
    def total_point(self):
        return self._total_point

    @total_point.setter
    def total_point(self, value):
        self._total_point = value


    def to_alipay_dict(self):
        params = dict()
        if self.earned_point:
            if hasattr(self.earned_point, 'to_alipay_dict'):
                params['earned_point'] = self.earned_point.to_alipay_dict()
            else:
                params['earned_point'] = self.earned_point
        if self.owner_type:
            if hasattr(self.owner_type, 'to_alipay_dict'):
                params['owner_type'] = self.owner_type.to_alipay_dict()
            else:
                params['owner_type'] = self.owner_type
        if self.task_code:
            if hasattr(self.task_code, 'to_alipay_dict'):
                params['task_code'] = self.task_code.to_alipay_dict()
            else:
                params['task_code'] = self.task_code
        if self.task_desc:
            if hasattr(self.task_desc, 'to_alipay_dict'):
                params['task_desc'] = self.task_desc.to_alipay_dict()
            else:
                params['task_desc'] = self.task_desc
        if self.task_end_time:
            if hasattr(self.task_end_time, 'to_alipay_dict'):
                params['task_end_time'] = self.task_end_time.to_alipay_dict()
            else:
                params['task_end_time'] = self.task_end_time
        if self.task_icon_url:
            if hasattr(self.task_icon_url, 'to_alipay_dict'):
                params['task_icon_url'] = self.task_icon_url.to_alipay_dict()
            else:
                params['task_icon_url'] = self.task_icon_url
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.task_remain_point:
            if hasattr(self.task_remain_point, 'to_alipay_dict'):
                params['task_remain_point'] = self.task_remain_point.to_alipay_dict()
            else:
                params['task_remain_point'] = self.task_remain_point
        if self.task_start_time:
            if hasattr(self.task_start_time, 'to_alipay_dict'):
                params['task_start_time'] = self.task_start_time.to_alipay_dict()
            else:
                params['task_start_time'] = self.task_start_time
        if self.task_status:
            if hasattr(self.task_status, 'to_alipay_dict'):
                params['task_status'] = self.task_status.to_alipay_dict()
            else:
                params['task_status'] = self.task_status
        if self.total_point:
            if hasattr(self.total_point, 'to_alipay_dict'):
                params['total_point'] = self.total_point.to_alipay_dict()
            else:
                params['total_point'] = self.total_point
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskInfo()
        if 'earned_point' in d:
            o.earned_point = d['earned_point']
        if 'owner_type' in d:
            o.owner_type = d['owner_type']
        if 'task_code' in d:
            o.task_code = d['task_code']
        if 'task_desc' in d:
            o.task_desc = d['task_desc']
        if 'task_end_time' in d:
            o.task_end_time = d['task_end_time']
        if 'task_icon_url' in d:
            o.task_icon_url = d['task_icon_url']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_remain_point' in d:
            o.task_remain_point = d['task_remain_point']
        if 'task_start_time' in d:
            o.task_start_time = d['task_start_time']
        if 'task_status' in d:
            o.task_status = d['task_status']
        if 'total_point' in d:
            o.total_point = d['total_point']
        return o


