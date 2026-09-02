#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationServiceShopBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationServiceShopBindResponse, self).__init__()
        self._response_data = None
        self._submit_record_id = None

    @property
    def response_data(self):
        return self._response_data

    @response_data.setter
    def response_data(self, value):
        self._response_data = value
    @property
    def submit_record_id(self):
        return self._submit_record_id

    @submit_record_id.setter
    def submit_record_id(self, value):
        self._submit_record_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationServiceShopBindResponse, self).parse_response_content(response_content)
        if 'response_data' in response:
            self.response_data = response['response_data']
        if 'submit_record_id' in response:
            self.submit_record_id = response['submit_record_id']
