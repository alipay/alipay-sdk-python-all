#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskDetailInfo(object):

    def __init__(self):
        self._applied_point = None
        self._indicator_point_map = None
        self._point_status = None
        self._task_code = None
        self._task_current_indicator = None
        self._task_desc = None
        self._task_end_time = None
        self._task_icon_url = None
        self._task_introduction_url = None
        self._task_name = None
        self._task_start_time = None
        self._task_status = None
        self._task_target_indicator = None

    @property
    def applied_point(self):
        return self._applied_point

    @applied_point.setter
    def applied_point(self, value):
        self._applied_point = value
    @property
    def indicator_point_map(self):
        return self._indicator_point_map

    @indicator_point_map.setter
    def indicator_point_map(self, value):
        self._indicator_point_map = value
    @property
    def point_status(self):
        return self._point_status

    @point_status.setter
    def point_status(self, value):
        self._point_status = value
    @property
    def task_code(self):
        return self._task_code

    @task_code.setter
    def task_code(self, value):
        self._task_code = value
    @property
    def task_current_indicator(self):
        return self._task_current_indicator

    @task_current_indicator.setter
    def task_current_indicator(self, value):
        self._task_current_indicator = value
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
    def task_introduction_url(self):
        return self._task_introduction_url

    @task_introduction_url.setter
    def task_introduction_url(self, value):
        self._task_introduction_url = value
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
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value
    @property
    def task_target_indicator(self):
        return self._task_target_indicator

    @task_target_indicator.setter
    def task_target_indicator(self, value):
        self._task_target_indicator = value


    def to_alipay_dict(self):
        params = dict()
        if self.applied_point:
            if hasattr(self.applied_point, 'to_alipay_dict'):
                params['applied_point'] = self.applied_point.to_alipay_dict()
            else:
                params['applied_point'] = self.applied_point
        if self.indicator_point_map:
            if hasattr(self.indicator_point_map, 'to_alipay_dict'):
                params['indicator_point_map'] = self.indicator_point_map.to_alipay_dict()
            else:
                params['indicator_point_map'] = self.indicator_point_map
        if self.point_status:
            if hasattr(self.point_status, 'to_alipay_dict'):
                params['point_status'] = self.point_status.to_alipay_dict()
            else:
                params['point_status'] = self.point_status
        if self.task_code:
            if hasattr(self.task_code, 'to_alipay_dict'):
                params['task_code'] = self.task_code.to_alipay_dict()
            else:
                params['task_code'] = self.task_code
        if self.task_current_indicator:
            if hasattr(self.task_current_indicator, 'to_alipay_dict'):
                params['task_current_indicator'] = self.task_current_indicator.to_alipay_dict()
            else:
                params['task_current_indicator'] = self.task_current_indicator
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
        if self.task_introduction_url:
            if hasattr(self.task_introduction_url, 'to_alipay_dict'):
                params['task_introduction_url'] = self.task_introduction_url.to_alipay_dict()
            else:
                params['task_introduction_url'] = self.task_introduction_url
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
        if self.task_status:
            if hasattr(self.task_status, 'to_alipay_dict'):
                params['task_status'] = self.task_status.to_alipay_dict()
            else:
                params['task_status'] = self.task_status
        if self.task_target_indicator:
            if hasattr(self.task_target_indicator, 'to_alipay_dict'):
                params['task_target_indicator'] = self.task_target_indicator.to_alipay_dict()
            else:
                params['task_target_indicator'] = self.task_target_indicator
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskDetailInfo()
        if 'applied_point' in d:
            o.applied_point = d['applied_point']
        if 'indicator_point_map' in d:
            o.indicator_point_map = d['indicator_point_map']
        if 'point_status' in d:
            o.point_status = d['point_status']
        if 'task_code' in d:
            o.task_code = d['task_code']
        if 'task_current_indicator' in d:
            o.task_current_indicator = d['task_current_indicator']
        if 'task_desc' in d:
            o.task_desc = d['task_desc']
        if 'task_end_time' in d:
            o.task_end_time = d['task_end_time']
        if 'task_icon_url' in d:
            o.task_icon_url = d['task_icon_url']
        if 'task_introduction_url' in d:
            o.task_introduction_url = d['task_introduction_url']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_start_time' in d:
            o.task_start_time = d['task_start_time']
        if 'task_status' in d:
            o.task_status = d['task_status']
        if 'task_target_indicator' in d:
            o.task_target_indicator = d['task_target_indicator']
        return o


