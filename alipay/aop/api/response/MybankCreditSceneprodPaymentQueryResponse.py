#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSceneprodPaymentQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSceneprodPaymentQueryResponse, self).__init__()
        self._content = None
        self._finish_time = None
        self._in_apply_no = None
        self._retry = None
        self._status = None
        self._trace_id = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
    @property
    def in_apply_no(self):
        return self._in_apply_no

    @in_apply_no.setter
    def in_apply_no(self, value):
        self._in_apply_no = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSceneprodPaymentQueryResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
        if 'finish_time' in response:
            self.finish_time = response['finish_time']
        if 'in_apply_no' in response:
            self.in_apply_no = response['in_apply_no']
        if 'retry' in response:
            self.retry = response['retry']
        if 'status' in response:
            self.status = response['status']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
