#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSceneprodPreadmitQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSceneprodPreadmitQueryResponse, self).__init__()
        self._pre_admit_result = None
        self._reject_code = None
        self._reject_reason = None
        self._trace_id = None

    @property
    def pre_admit_result(self):
        return self._pre_admit_result

    @pre_admit_result.setter
    def pre_admit_result(self, value):
        self._pre_admit_result = value
    @property
    def reject_code(self):
        return self._reject_code

    @reject_code.setter
    def reject_code(self, value):
        self._reject_code = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSceneprodPreadmitQueryResponse, self).parse_response_content(response_content)
        if 'pre_admit_result' in response:
            self.pre_admit_result = response['pre_admit_result']
        if 'reject_code' in response:
            self.reject_code = response['reject_code']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
