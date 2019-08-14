#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSceneprodDrawdownConfirmResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSceneprodDrawdownConfirmResponse, self).__init__()
        self._apply_no = None
        self._error_msg = None
        self._fin_order_no = None
        self._process_result = None
        self._request_id = None
        self._retry = None
        self._trace_id = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def fin_order_no(self):
        return self._fin_order_no

    @fin_order_no.setter
    def fin_order_no(self, value):
        self._fin_order_no = value
    @property
    def process_result(self):
        return self._process_result

    @process_result.setter
    def process_result(self, value):
        self._process_result = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSceneprodDrawdownConfirmResponse, self).parse_response_content(response_content)
        if 'apply_no' in response:
            self.apply_no = response['apply_no']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'fin_order_no' in response:
            self.fin_order_no = response['fin_order_no']
        if 'process_result' in response:
            self.process_result = response['process_result']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'retry' in response:
            self.retry = response['retry']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
