#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BillInferenceResult import BillInferenceResult


class AlipayIserviceCognitiveBillInferenceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCognitiveBillInferenceQueryResponse, self).__init__()
        self._result = None
        self._ret = None
        self._trace_id = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, BillInferenceResult):
            self._result = value
        else:
            self._result = BillInferenceResult.from_alipay_dict(value)
    @property
    def ret(self):
        return self._ret

    @ret.setter
    def ret(self, value):
        self._ret = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCognitiveBillInferenceQueryResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'ret' in response:
            self.ret = response['ret']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
