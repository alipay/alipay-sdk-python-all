#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InputInvoiceCheckResponse import InputInvoiceCheckResponse


class AlipayBossFncInputInvoiceCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncInputInvoiceCheckResponse, self).__init__()
        self._result_set = None

    @property
    def result_set(self):
        return self._result_set

    @result_set.setter
    def result_set(self, value):
        if isinstance(value, InputInvoiceCheckResponse):
            self._result_set = value
        else:
            self._result_set = InputInvoiceCheckResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncInputInvoiceCheckResponse, self).parse_response_content(response_content)
        if 'result_set' in response:
            self.result_set = response['result_set']
