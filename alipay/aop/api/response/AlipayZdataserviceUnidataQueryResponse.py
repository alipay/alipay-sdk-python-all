#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayZdataserviceUnidataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayZdataserviceUnidataQueryResponse, self).__init__()
        self._query_result = None
        self._result_code = None
        self._success = None

    @property
    def query_result(self):
        return self._query_result

    @query_result.setter
    def query_result(self, value):
        self._query_result = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayZdataserviceUnidataQueryResponse, self).parse_response_content(response_content)
        if 'query_result' in response:
            self.query_result = response['query_result']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'success' in response:
            self.success = response['success']
