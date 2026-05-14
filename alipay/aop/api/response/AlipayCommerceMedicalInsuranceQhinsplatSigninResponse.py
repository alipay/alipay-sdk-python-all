#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalInsuranceQhinsplatSigninResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsuranceQhinsplatSigninResponse, self).__init__()
        self._response_str = None

    @property
    def response_str(self):
        return self._response_str

    @response_str.setter
    def response_str(self, value):
        self._response_str = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsuranceQhinsplatSigninResponse, self).parse_response_content(response_content)
        if 'response_str' in response:
            self.response_str = response['response_str']
