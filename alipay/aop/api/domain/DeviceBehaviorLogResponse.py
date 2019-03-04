#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceBehaviorLogResponse(object):

    def __init__(self):
        self._behavior_type = None
        self._log_content = None
        self._log_time = None

    @property
    def behavior_type(self):
        return self._behavior_type

    @behavior_type.setter
    def behavior_type(self, value):
        self._behavior_type = value
    @property
    def log_content(self):
        return self._log_content

    @log_content.setter
    def log_content(self, value):
        self._log_content = value
    @property
    def log_time(self):
        return self._log_time

    @log_time.setter
    def log_time(self, value):
        self._log_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.behavior_type:
            if hasattr(self.behavior_type, 'to_alipay_dict'):
                params['behavior_type'] = self.behavior_type.to_alipay_dict()
            else:
                params['behavior_type'] = self.behavior_type
        if self.log_content:
            if hasattr(self.log_content, 'to_alipay_dict'):
                params['log_content'] = self.log_content.to_alipay_dict()
            else:
                params['log_content'] = self.log_content
        if self.log_time:
            if hasattr(self.log_time, 'to_alipay_dict'):
                params['log_time'] = self.log_time.to_alipay_dict()
            else:
                params['log_time'] = self.log_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceBehaviorLogResponse()
        if 'behavior_type' in d:
            o.behavior_type = d['behavior_type']
        if 'log_content' in d:
            o.log_content = d['log_content']
        if 'log_time' in d:
            o.log_time = d['log_time']
        return o


