#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHealthcaSignqrurlCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHealthcaSignqrurlCreateResponse, self).__init__()
        self._sign_flow_id = None
        self._sign_url = None

    @property
    def sign_flow_id(self):
        return self._sign_flow_id

    @sign_flow_id.setter
    def sign_flow_id(self, value):
        self._sign_flow_id = value
    @property
    def sign_url(self):
        return self._sign_url

    @sign_url.setter
    def sign_url(self, value):
        self._sign_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHealthcaSignqrurlCreateResponse, self).parse_response_content(response_content)
        if 'sign_flow_id' in response:
            self.sign_flow_id = response['sign_flow_id']
        if 'sign_url' in response:
            self.sign_url = response['sign_url']
