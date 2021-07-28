#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceDatapropertyBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceDatapropertyBatchqueryResponse, self).__init__()
        self._process_id = None
        self._result_key = None
        self._result_response = None
        self._result_type = None
        self._result_value = None

    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value
    @property
    def result_key(self):
        return self._result_key

    @result_key.setter
    def result_key(self, value):
        self._result_key = value
    @property
    def result_response(self):
        return self._result_response

    @result_response.setter
    def result_response(self, value):
        self._result_response = value
    @property
    def result_type(self):
        return self._result_type

    @result_type.setter
    def result_type(self, value):
        self._result_type = value
    @property
    def result_value(self):
        return self._result_value

    @result_value.setter
    def result_value(self, value):
        self._result_value = value

    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceDatapropertyBatchqueryResponse, self).parse_response_content(response_content)
        if 'process_id' in response:
            self.process_id = response['process_id']
        if 'result_key' in response:
            self.result_key = response['result_key']
        if 'result_response' in response:
            self.result_response = response['result_response']
        if 'result_type' in response:
            self.result_type = response['result_type']
        if 'result_value' in response:
            self.result_value = response['result_value']
