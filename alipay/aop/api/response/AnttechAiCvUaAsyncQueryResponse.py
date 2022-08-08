#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechAiCvUaAsyncQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechAiCvUaAsyncQueryResponse, self).__init__()
        self._host = None
        self._result_code = None
        self._result_detail = None
        self._result_msg = None
        self._result_success = None
        self._result_url = None
        self._status = None

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
    def result_detail(self):
        return self._result_detail

    @result_detail.setter
    def result_detail(self, value):
        self._result_detail = value
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
    def result_url(self):
        return self._result_url

    @result_url.setter
    def result_url(self, value):
        self._result_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AnttechAiCvUaAsyncQueryResponse, self).parse_response_content(response_content)
        if 'host' in response:
            self.host = response['host']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_detail' in response:
            self.result_detail = response['result_detail']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
        if 'result_success' in response:
            self.result_success = response['result_success']
        if 'result_url' in response:
            self.result_url = response['result_url']
        if 'status' in response:
            self.status = response['status']
