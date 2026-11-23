#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalDeviceSosSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalDeviceSosSendResponse, self).__init__()
        self._assistance_id = None
        self._operation_result = None
        self._rescue_status = None

    @property
    def assistance_id(self):
        return self._assistance_id

    @assistance_id.setter
    def assistance_id(self, value):
        self._assistance_id = value
    @property
    def operation_result(self):
        return self._operation_result

    @operation_result.setter
    def operation_result(self, value):
        self._operation_result = value
    @property
    def rescue_status(self):
        return self._rescue_status

    @rescue_status.setter
    def rescue_status(self, value):
        self._rescue_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalDeviceSosSendResponse, self).parse_response_content(response_content)
        if 'assistance_id' in response:
            self.assistance_id = response['assistance_id']
        if 'operation_result' in response:
            self.operation_result = response['operation_result']
        if 'rescue_status' in response:
            self.rescue_status = response['rescue_status']
