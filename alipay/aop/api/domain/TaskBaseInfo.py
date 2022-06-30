#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskBaseInfo(object):

    def __init__(self):
        self._gmt_begin = None
        self._gmt_end = None
        self._sign_up_begin_time = None
        self._sign_up_end_time = None
        self._task_name = None
        self._task_type = None

    @property
    def gmt_begin(self):
        return self._gmt_begin

    @gmt_begin.setter
    def gmt_begin(self, value):
        self._gmt_begin = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def sign_up_begin_time(self):
        return self._sign_up_begin_time

    @sign_up_begin_time.setter
    def sign_up_begin_time(self, value):
        self._sign_up_begin_time = value
    @property
    def sign_up_end_time(self):
        return self._sign_up_end_time

    @sign_up_end_time.setter
    def sign_up_end_time(self, value):
        self._sign_up_end_time = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_begin:
            if hasattr(self.gmt_begin, 'to_alipay_dict'):
                params['gmt_begin'] = self.gmt_begin.to_alipay_dict()
            else:
                params['gmt_begin'] = self.gmt_begin
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.sign_up_begin_time:
            if hasattr(self.sign_up_begin_time, 'to_alipay_dict'):
                params['sign_up_begin_time'] = self.sign_up_begin_time.to_alipay_dict()
            else:
                params['sign_up_begin_time'] = self.sign_up_begin_time
        if self.sign_up_end_time:
            if hasattr(self.sign_up_end_time, 'to_alipay_dict'):
                params['sign_up_end_time'] = self.sign_up_end_time.to_alipay_dict()
            else:
                params['sign_up_end_time'] = self.sign_up_end_time
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskBaseInfo()
        if 'gmt_begin' in d:
            o.gmt_begin = d['gmt_begin']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'sign_up_begin_time' in d:
            o.sign_up_begin_time = d['sign_up_begin_time']
        if 'sign_up_end_time' in d:
            o.sign_up_end_time = d['sign_up_end_time']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_type' in d:
            o.task_type = d['task_type']
        return o


