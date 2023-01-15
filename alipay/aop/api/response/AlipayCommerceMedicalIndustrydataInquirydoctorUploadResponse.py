#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalIndustrydataInquirydoctorUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalIndustrydataInquirydoctorUploadResponse, self).__init__()
        self._error_message = None
        self._result_code = None
        self._time = None

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
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalIndustrydataInquirydoctorUploadResponse, self).parse_response_content(response_content)
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'time' in response:
            self.time = response['time']
