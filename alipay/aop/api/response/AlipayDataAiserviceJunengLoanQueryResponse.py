#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataAiserviceJunengLoanQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataAiserviceJunengLoanQueryResponse, self).__init__()
        self._biz_error_code = None
        self._hashed_cert_no = None
        self._request_uuid = None
        self._result = None

    @property
    def biz_error_code(self):
        return self._biz_error_code

    @biz_error_code.setter
    def biz_error_code(self, value):
        self._biz_error_code = value
    @property
    def hashed_cert_no(self):
        return self._hashed_cert_no

    @hashed_cert_no.setter
    def hashed_cert_no(self, value):
        self._hashed_cert_no = value
    @property
    def request_uuid(self):
        return self._request_uuid

    @request_uuid.setter
    def request_uuid(self, value):
        self._request_uuid = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataAiserviceJunengLoanQueryResponse, self).parse_response_content(response_content)
        if 'biz_error_code' in response:
            self.biz_error_code = response['biz_error_code']
        if 'hashed_cert_no' in response:
            self.hashed_cert_no = response['hashed_cert_no']
        if 'request_uuid' in response:
            self.request_uuid = response['request_uuid']
        if 'result' in response:
            self.result = response['result']
