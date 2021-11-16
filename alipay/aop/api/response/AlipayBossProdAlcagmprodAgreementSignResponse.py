#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdAlcagmprodAgreementSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAlcagmprodAgreementSignResponse, self).__init__()
        self._result_success = None
        self._result_trace_id = None

    @property
    def result_success(self):
        return self._result_success

    @result_success.setter
    def result_success(self, value):
        self._result_success = value
    @property
    def result_trace_id(self):
        return self._result_trace_id

    @result_trace_id.setter
    def result_trace_id(self, value):
        self._result_trace_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAlcagmprodAgreementSignResponse, self).parse_response_content(response_content)
        if 'result_success' in response:
            self.result_success = response['result_success']
        if 'result_trace_id' in response:
            self.result_trace_id = response['result_trace_id']
