#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskOperateResult(object):

    def __init__(self):
        self._error_message = None
        self._need_warning = None
        self._task_operate_result = None

    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def need_warning(self):
        return self._need_warning

    @need_warning.setter
    def need_warning(self, value):
        self._need_warning = value
    @property
    def task_operate_result(self):
        return self._task_operate_result

    @task_operate_result.setter
    def task_operate_result(self, value):
        self._task_operate_result = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_message:
            if hasattr(self.error_message, 'to_alipay_dict'):
                params['error_message'] = self.error_message.to_alipay_dict()
            else:
                params['error_message'] = self.error_message
        if self.need_warning:
            if hasattr(self.need_warning, 'to_alipay_dict'):
                params['need_warning'] = self.need_warning.to_alipay_dict()
            else:
                params['need_warning'] = self.need_warning
        if self.task_operate_result:
            if hasattr(self.task_operate_result, 'to_alipay_dict'):
                params['task_operate_result'] = self.task_operate_result.to_alipay_dict()
            else:
                params['task_operate_result'] = self.task_operate_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskOperateResult()
        if 'error_message' in d:
            o.error_message = d['error_message']
        if 'need_warning' in d:
            o.need_warning = d['need_warning']
        if 'task_operate_result' in d:
            o.task_operate_result = d['task_operate_result']
        return o


