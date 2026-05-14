#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationServiceApplyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationServiceApplyQueryResponse, self).__init__()
        self._apply_record_id = None
        self._response_data = None

    @property
    def apply_record_id(self):
        return self._apply_record_id

    @apply_record_id.setter
    def apply_record_id(self, value):
        self._apply_record_id = value
    @property
    def response_data(self):
        return self._response_data

    @response_data.setter
    def response_data(self, value):
        self._response_data = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationServiceApplyQueryResponse, self).parse_response_content(response_content)
        if 'apply_record_id' in response:
            self.apply_record_id = response['apply_record_id']
        if 'response_data' in response:
            self.response_data = response['response_data']
