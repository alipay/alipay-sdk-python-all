#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LiveSubTaskList(object):

    def __init__(self):
        self._sub_task_status = None
        self._sub_task_type = None

    @property
    def sub_task_status(self):
        return self._sub_task_status

    @sub_task_status.setter
    def sub_task_status(self, value):
        self._sub_task_status = value
    @property
    def sub_task_type(self):
        return self._sub_task_type

    @sub_task_type.setter
    def sub_task_type(self, value):
        self._sub_task_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.sub_task_status:
            if hasattr(self.sub_task_status, 'to_alipay_dict'):
                params['sub_task_status'] = self.sub_task_status.to_alipay_dict()
            else:
                params['sub_task_status'] = self.sub_task_status
        if self.sub_task_type:
            if hasattr(self.sub_task_type, 'to_alipay_dict'):
                params['sub_task_type'] = self.sub_task_type.to_alipay_dict()
            else:
                params['sub_task_type'] = self.sub_task_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LiveSubTaskList()
        if 'sub_task_status' in d:
            o.sub_task_status = d['sub_task_status']
        if 'sub_task_type' in d:
            o.sub_task_type = d['sub_task_type']
        return o


