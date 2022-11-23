#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MedicalPaymentQueryResponse import MedicalPaymentQueryResponse


class AlipayCommerceMedicalPaymentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalPaymentQueryResponse, self).__init__()
        self._error_message = None
        self._result_code = None
        self._result_data = None

    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_data(self):
        return self._result_data

    @result_data.setter
    def result_data(self, value):
        if isinstance(value, MedicalPaymentQueryResponse):
            self._result_data = value
        else:
            self._result_data = MedicalPaymentQueryResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalPaymentQueryResponse, self).parse_response_content(response_content)
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_data' in response:
            self.result_data = response['result_data']
