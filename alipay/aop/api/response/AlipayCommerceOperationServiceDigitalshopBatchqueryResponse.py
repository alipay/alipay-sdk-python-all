#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationServiceDigitalshopBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationServiceDigitalshopBatchqueryResponse, self).__init__()
        self._response_data = None
        self._service_code = None

    @property
    def response_data(self):
        return self._response_data

    @response_data.setter
    def response_data(self, value):
        self._response_data = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationServiceDigitalshopBatchqueryResponse, self).parse_response_content(response_content)
        if 'response_data' in response:
            self.response_data = response['response_data']
        if 'service_code' in response:
            self.service_code = response['service_code']
