#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateVerifyConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateVerifyConsultResponse, self).__init__()
        self._normal_url = None
        self._verify_request_id = None

    @property
    def normal_url(self):
        return self._normal_url

    @normal_url.setter
    def normal_url(self, value):
        self._normal_url = value
    @property
    def verify_request_id(self):
        return self._verify_request_id

    @verify_request_id.setter
    def verify_request_id(self, value):
        self._verify_request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateVerifyConsultResponse, self).parse_response_content(response_content)
        if 'normal_url' in response:
            self.normal_url = response['normal_url']
        if 'verify_request_id' in response:
            self.verify_request_id = response['verify_request_id']
