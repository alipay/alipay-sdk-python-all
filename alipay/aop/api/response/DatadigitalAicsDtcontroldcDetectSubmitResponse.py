#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalAicsDtcontroldcDetectSubmitResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAicsDtcontroldcDetectSubmitResponse, self).__init__()
        self._data = None
        self._message = None
        self._qc_detect_result_id = None
        self._result_code = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def qc_detect_result_id(self):
        return self._qc_detect_result_id

    @qc_detect_result_id.setter
    def qc_detect_result_id(self, value):
        self._qc_detect_result_id = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalAicsDtcontroldcDetectSubmitResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'message' in response:
            self.message = response['message']
        if 'qc_detect_result_id' in response:
            self.qc_detect_result_id = response['qc_detect_result_id']
        if 'result_code' in response:
            self.result_code = response['result_code']
