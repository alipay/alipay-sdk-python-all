#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpMcpCreateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpMcpCreateQueryResponse, self).__init__()
        self._ability_code = None
        self._mcp_chinese_name = None
        self._mcp_english_name = None
        self._status = None

    @property
    def ability_code(self):
        return self._ability_code

    @ability_code.setter
    def ability_code(self, value):
        self._ability_code = value
    @property
    def mcp_chinese_name(self):
        return self._mcp_chinese_name

    @mcp_chinese_name.setter
    def mcp_chinese_name(self, value):
        self._mcp_chinese_name = value
    @property
    def mcp_english_name(self):
        return self._mcp_english_name

    @mcp_english_name.setter
    def mcp_english_name(self, value):
        self._mcp_english_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpMcpCreateQueryResponse, self).parse_response_content(response_content)
        if 'ability_code' in response:
            self.ability_code = response['ability_code']
        if 'mcp_chinese_name' in response:
            self.mcp_chinese_name = response['mcp_chinese_name']
        if 'mcp_english_name' in response:
            self.mcp_english_name = response['mcp_english_name']
        if 'status' in response:
            self.status = response['status']
