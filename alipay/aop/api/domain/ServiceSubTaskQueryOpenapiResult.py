#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceSubTaskQueryOpenapiResult(object):

    def __init__(self):
        self._end_time = None
        self._ext_info = None
        self._result_code = None
        self._result_msg = None
        self._start_time = None
        self._sub_task_id = None
        self._sub_task_status = None
        self._sub_task_type = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def sub_task_id(self):
        return self._sub_task_id

    @sub_task_id.setter
    def sub_task_id(self, value):
        self._sub_task_id = value
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
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
        if self.result_msg:
            if hasattr(self.result_msg, 'to_alipay_dict'):
                params['result_msg'] = self.result_msg.to_alipay_dict()
            else:
                params['result_msg'] = self.result_msg
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.sub_task_id:
            if hasattr(self.sub_task_id, 'to_alipay_dict'):
                params['sub_task_id'] = self.sub_task_id.to_alipay_dict()
            else:
                params['sub_task_id'] = self.sub_task_id
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
        o = ServiceSubTaskQueryOpenapiResult()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'result_msg' in d:
            o.result_msg = d['result_msg']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'sub_task_id' in d:
            o.sub_task_id = d['sub_task_id']
        if 'sub_task_status' in d:
            o.sub_task_status = d['sub_task_status']
        if 'sub_task_type' in d:
            o.sub_task_type = d['sub_task_type']
        return o


