#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInspectNotifyModel(object):

    def __init__(self):
        self._function_name = None
        self._job_id = None
        self._log_url = None
        self._result = None
        self._status = None
        self._timing = None

    @property
    def function_name(self):
        return self._function_name

    @function_name.setter
    def function_name(self, value):
        self._function_name = value
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value
    @property
    def log_url(self):
        return self._log_url

    @log_url.setter
    def log_url(self, value):
        self._log_url = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def timing(self):
        return self._timing

    @timing.setter
    def timing(self, value):
        self._timing = value


    def to_alipay_dict(self):
        params = dict()
        if self.function_name:
            if hasattr(self.function_name, 'to_alipay_dict'):
                params['function_name'] = self.function_name.to_alipay_dict()
            else:
                params['function_name'] = self.function_name
        if self.job_id:
            if hasattr(self.job_id, 'to_alipay_dict'):
                params['job_id'] = self.job_id.to_alipay_dict()
            else:
                params['job_id'] = self.job_id
        if self.log_url:
            if hasattr(self.log_url, 'to_alipay_dict'):
                params['log_url'] = self.log_url.to_alipay_dict()
            else:
                params['log_url'] = self.log_url
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.timing:
            if hasattr(self.timing, 'to_alipay_dict'):
                params['timing'] = self.timing.to_alipay_dict()
            else:
                params['timing'] = self.timing
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInspectNotifyModel()
        if 'function_name' in d:
            o.function_name = d['function_name']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'log_url' in d:
            o.log_url = d['log_url']
        if 'result' in d:
            o.result = d['result']
        if 'status' in d:
            o.status = d['status']
        if 'timing' in d:
            o.timing = d['timing']
        return o


