#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MedicalUserMessageSubcriptionInfo import MedicalUserMessageSubcriptionInfo


class AlipayCommerceMedicalUsermessageSubscriptionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalUsermessageSubscriptionQueryResponse, self).__init__()
        self._data = None
        self._error_message = None
        self._result_code = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, MedicalUserMessageSubcriptionInfo):
                    self._data.append(i)
                else:
                    self._data.append(MedicalUserMessageSubcriptionInfo.from_alipay_dict(i))
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

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalUsermessageSubscriptionQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'result_code' in response:
            self.result_code = response['result_code']
