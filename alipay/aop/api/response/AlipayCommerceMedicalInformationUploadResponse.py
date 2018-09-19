#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalInformationUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInformationUploadResponse, self).__init__()
        self._gmt_payment = None
        self._response_content = None

    @property
    def gmt_payment(self):
        return self._gmt_payment

    @gmt_payment.setter
    def gmt_payment(self, value):
        self._gmt_payment = value
    @property
    def response_content(self):
        return self._response_content

    @response_content.setter
    def response_content(self, value):
        self._response_content = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInformationUploadResponse, self).parse_response_content(response_content)
        if 'gmt_payment' in response:
            self.gmt_payment = response['gmt_payment']
        if 'response_content' in response:
            self.response_content = response['response_content']
