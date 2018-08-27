#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSceneprodPaymentApplyResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSceneprodPaymentApplyResponse, self).__init__()
        self._in_apply_no = None
        self._retry = None
        self._trace_id = None

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
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSceneprodPaymentApplyResponse, self).parse_response_content(response_content)
        if 'in_apply_no' in response:
            self.in_apply_no = response['in_apply_no']
        if 'retry' in response:
            self.retry = response['retry']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
