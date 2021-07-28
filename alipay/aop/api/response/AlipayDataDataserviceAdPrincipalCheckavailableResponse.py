#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAdPrincipalCheckavailableResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdPrincipalCheckavailableResponse, self).__init__()
        self._principal_id = None
        self._sign_status = None

    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdPrincipalCheckavailableResponse, self).parse_response_content(response_content)
        if 'principal_id' in response:
            self.principal_id = response['principal_id']
        if 'sign_status' in response:
            self.sign_status = response['sign_status']
