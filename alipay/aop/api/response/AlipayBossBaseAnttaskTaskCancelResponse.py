#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossBaseAnttaskTaskCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossBaseAnttaskTaskCancelResponse, self).__init__()
        self._error_message = None
        self._need_warning = None
        self._task_error_code = None
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
    def task_error_code(self):
        return self._task_error_code

    @task_error_code.setter
    def task_error_code(self, value):
        self._task_error_code = value
    @property
    def task_operate_result(self):
        return self._task_operate_result

    @task_operate_result.setter
    def task_operate_result(self, value):
        self._task_operate_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossBaseAnttaskTaskCancelResponse, self).parse_response_content(response_content)
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'need_warning' in response:
            self.need_warning = response['need_warning']
        if 'task_error_code' in response:
            self.task_error_code = response['task_error_code']
        if 'task_operate_result' in response:
            self.task_operate_result = response['task_operate_result']
