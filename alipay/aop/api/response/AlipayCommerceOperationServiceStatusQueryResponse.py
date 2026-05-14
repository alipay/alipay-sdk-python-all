#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationServiceStatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationServiceStatusQueryResponse, self).__init__()
        self._response_data = None
        self._service_code = None
        self._subject_id = None
        self._subject_type = None

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
    @property
    def subject_id(self):
        return self._subject_id

    @subject_id.setter
    def subject_id(self, value):
        self._subject_id = value
    @property
    def subject_type(self):
        return self._subject_type

    @subject_type.setter
    def subject_type(self, value):
        self._subject_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationServiceStatusQueryResponse, self).parse_response_content(response_content)
        if 'response_data' in response:
            self.response_data = response['response_data']
        if 'service_code' in response:
            self.service_code = response['service_code']
        if 'subject_id' in response:
            self.subject_id = response['subject_id']
        if 'subject_type' in response:
            self.subject_type = response['subject_type']
