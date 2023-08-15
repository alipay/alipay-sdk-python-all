#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Execution(object):

    def __init__(self):
        self._cost = None
        self._env_id = None
        self._function_name = None
        self._status = None
        self._time = None
        self._trace_id = None

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value
    @property
    def env_id(self):
        return self._env_id

    @env_id.setter
    def env_id(self, value):
        self._env_id = value
    @property
    def function_name(self):
        return self._function_name

    @function_name.setter
    def function_name(self, value):
        self._function_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cost:
            if hasattr(self.cost, 'to_alipay_dict'):
                params['cost'] = self.cost.to_alipay_dict()
            else:
                params['cost'] = self.cost
        if self.env_id:
            if hasattr(self.env_id, 'to_alipay_dict'):
                params['env_id'] = self.env_id.to_alipay_dict()
            else:
                params['env_id'] = self.env_id
        if self.function_name:
            if hasattr(self.function_name, 'to_alipay_dict'):
                params['function_name'] = self.function_name.to_alipay_dict()
            else:
                params['function_name'] = self.function_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Execution()
        if 'cost' in d:
            o.cost = d['cost']
        if 'env_id' in d:
            o.env_id = d['env_id']
        if 'function_name' in d:
            o.function_name = d['function_name']
        if 'status' in d:
            o.status = d['status']
        if 'time' in d:
            o.time = d['time']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        return o


