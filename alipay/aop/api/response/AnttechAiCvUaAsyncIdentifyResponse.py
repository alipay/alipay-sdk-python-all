#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechAiCvUaAsyncIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechAiCvUaAsyncIdentifyResponse, self).__init__()
        self._host = None
        self._result_code = None
        self._result_msg = None
        self._result_success = None
        self._service_code = None
        self._task_id = None

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value
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
    def result_success(self):
        return self._result_success

    @result_success.setter
    def result_success(self, value):
        self._result_success = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechAiCvUaAsyncIdentifyResponse, self).parse_response_content(response_content)
        if 'host' in response:
            self.host = response['host']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
        if 'result_success' in response:
            self.result_success = response['result_success']
        if 'service_code' in response:
            self.service_code = response['service_code']
        if 'task_id' in response:
            self.task_id = response['task_id']
