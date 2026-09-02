#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationServiceDigitalpoiCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationServiceDigitalpoiCreateResponse, self).__init__()
        self._submit_record_id = None

    @property
    def submit_record_id(self):
        return self._submit_record_id

    @submit_record_id.setter
    def submit_record_id(self, value):
        self._submit_record_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationServiceDigitalpoiCreateResponse, self).parse_response_content(response_content)
        if 'submit_record_id' in response:
            self.submit_record_id = response['submit_record_id']
