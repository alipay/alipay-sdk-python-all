#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceFundTransferDetectResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceFundTransferDetectResponse, self).__init__()
        self._data_code = None
        self._data_message = None
        self._data_result = None
        self._data_success = None
        self._data_timestamp = None

    @property
    def data_code(self):
        return self._data_code

    @data_code.setter
    def data_code(self, value):
        self._data_code = value
    @property
    def data_message(self):
        return self._data_message

    @data_message.setter
    def data_message(self, value):
        self._data_message = value
    @property
    def data_result(self):
        return self._data_result

    @data_result.setter
    def data_result(self, value):
        self._data_result = value
    @property
    def data_success(self):
        return self._data_success

    @data_success.setter
    def data_success(self, value):
        self._data_success = value
    @property
    def data_timestamp(self):
        return self._data_timestamp

    @data_timestamp.setter
    def data_timestamp(self, value):
        self._data_timestamp = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceFundTransferDetectResponse, self).parse_response_content(response_content)
        if 'data_code' in response:
            self.data_code = response['data_code']
        if 'data_message' in response:
            self.data_message = response['data_message']
        if 'data_result' in response:
            self.data_result = response['data_result']
        if 'data_success' in response:
            self.data_success = response['data_success']
        if 'data_timestamp' in response:
            self.data_timestamp = response['data_timestamp']
