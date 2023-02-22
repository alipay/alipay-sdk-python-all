#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenOperationOpenbizmockSchemaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOperationOpenbizmockSchemaQueryResponse, self).__init__()
        self._result = None
        self._result_open_id = None
        self._result_type = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def result_open_id(self):
        return self._result_open_id

    @result_open_id.setter
    def result_open_id(self, value):
        self._result_open_id = value
    @property
    def result_type(self):
        return self._result_type

    @result_type.setter
    def result_type(self, value):
        self._result_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenOperationOpenbizmockSchemaQueryResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'result_open_id' in response:
            self.result_open_id = response['result_open_id']
        if 'result_type' in response:
            self.result_type = response['result_type']
