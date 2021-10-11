#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFincoreComplianceCrossborderMerchantBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceCrossborderMerchantBatchqueryResponse, self).__init__()
        self._memo = None
        self._result = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceCrossborderMerchantBatchqueryResponse, self).parse_response_content(response_content)
        if 'memo' in response:
            self.memo = response['memo']
        if 'result' in response:
            self.result = response['result']
