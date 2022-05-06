#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MedicalHospitalOrderUploadResult import MedicalHospitalOrderUploadResult


class AlipayCommerceMedicalHospitalorderUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHospitalorderUploadResponse, self).__init__()
        self._data = None
        self._error_message = None
        self._result_code = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, MedicalHospitalOrderUploadResult):
            self._data = value
        else:
            self._data = MedicalHospitalOrderUploadResult.from_alipay_dict(value)
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
        response = super(AlipayCommerceMedicalHospitalorderUploadResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'result_code' in response:
            self.result_code = response['result_code']
