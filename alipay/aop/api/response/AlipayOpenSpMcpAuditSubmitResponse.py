#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpMcpAuditSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpMcpAuditSubmitResponse, self).__init__()
        self._submit_result = None
        self._tool_list = None

    @property
    def submit_result(self):
        return self._submit_result

    @submit_result.setter
    def submit_result(self, value):
        self._submit_result = value
    @property
    def tool_list(self):
        return self._tool_list

    @tool_list.setter
    def tool_list(self, value):
        if isinstance(value, list):
            self._tool_list = list()
            for i in value:
                self._tool_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpMcpAuditSubmitResponse, self).parse_response_content(response_content)
        if 'submit_result' in response:
            self.submit_result = response['submit_result']
        if 'tool_list' in response:
            self.tool_list = response['tool_list']
