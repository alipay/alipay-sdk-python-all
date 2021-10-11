#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportCarrentalServiceSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportCarrentalServiceSubmitResponse, self).__init__()
        self._request_id = None
        self._service_code = None

    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportCarrentalServiceSubmitResponse, self).parse_response_content(response_content)
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'service_code' in response:
            self.service_code = response['service_code']
