#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneQuotationResearchdataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneQuotationResearchdataQueryResponse, self).__init__()
        self._result_code = None
        self._result_content = None
        self._result_desc = None
        self._result_success = None

    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_content(self):
        return self._result_content

    @result_content.setter
    def result_content(self, value):
        self._result_content = value
    @property
    def result_desc(self):
        return self._result_desc

    @result_desc.setter
    def result_desc(self, value):
        self._result_desc = value
    @property
    def result_success(self):
        return self._result_success

    @result_success.setter
    def result_success(self, value):
        self._result_success = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneQuotationResearchdataQueryResponse, self).parse_response_content(response_content)
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_content' in response:
            self.result_content = response['result_content']
        if 'result_desc' in response:
            self.result_desc = response['result_desc']
        if 'result_success' in response:
            self.result_success = response['result_success']
