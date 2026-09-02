#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HeaderParam import HeaderParam
from alipay.aop.api.domain.McpToolList import McpToolList


class AlipayOpenSpMcpDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpMcpDetailQueryResponse, self).__init__()
        self._ability_status = None
        self._ability_version = None
        self._encrypt_app_id = None
        self._header_list = None
        self._icon_url = None
        self._mcp_chinese_name = None
        self._mcp_desc = None
        self._mcp_english_name = None
        self._mcp_server_url = None
        self._mcp_tool_list = None
        self._request_timeout = None
        self._response_timeout = None
        self._support_account_type_list = None
        self._support_protocols = None

    @property
    def ability_status(self):
        return self._ability_status

    @ability_status.setter
    def ability_status(self, value):
        self._ability_status = value
    @property
    def ability_version(self):
        return self._ability_version

    @ability_version.setter
    def ability_version(self, value):
        self._ability_version = value
    @property
    def encrypt_app_id(self):
        return self._encrypt_app_id

    @encrypt_app_id.setter
    def encrypt_app_id(self, value):
        self._encrypt_app_id = value
    @property
    def header_list(self):
        return self._header_list

    @header_list.setter
    def header_list(self, value):
        if isinstance(value, HeaderParam):
            self._header_list = value
        else:
            self._header_list = HeaderParam.from_alipay_dict(value)
    @property
    def icon_url(self):
        return self._icon_url

    @icon_url.setter
    def icon_url(self, value):
        self._icon_url = value
    @property
    def mcp_chinese_name(self):
        return self._mcp_chinese_name

    @mcp_chinese_name.setter
    def mcp_chinese_name(self, value):
        self._mcp_chinese_name = value
    @property
    def mcp_desc(self):
        return self._mcp_desc

    @mcp_desc.setter
    def mcp_desc(self, value):
        self._mcp_desc = value
    @property
    def mcp_english_name(self):
        return self._mcp_english_name

    @mcp_english_name.setter
    def mcp_english_name(self, value):
        self._mcp_english_name = value
    @property
    def mcp_server_url(self):
        return self._mcp_server_url

    @mcp_server_url.setter
    def mcp_server_url(self, value):
        self._mcp_server_url = value
    @property
    def mcp_tool_list(self):
        return self._mcp_tool_list

    @mcp_tool_list.setter
    def mcp_tool_list(self, value):
        if isinstance(value, list):
            self._mcp_tool_list = list()
            for i in value:
                if isinstance(i, McpToolList):
                    self._mcp_tool_list.append(i)
                else:
                    self._mcp_tool_list.append(McpToolList.from_alipay_dict(i))
    @property
    def request_timeout(self):
        return self._request_timeout

    @request_timeout.setter
    def request_timeout(self, value):
        self._request_timeout = value
    @property
    def response_timeout(self):
        return self._response_timeout

    @response_timeout.setter
    def response_timeout(self, value):
        self._response_timeout = value
    @property
    def support_account_type_list(self):
        return self._support_account_type_list

    @support_account_type_list.setter
    def support_account_type_list(self, value):
        if isinstance(value, list):
            self._support_account_type_list = list()
            for i in value:
                self._support_account_type_list.append(i)
    @property
    def support_protocols(self):
        return self._support_protocols

    @support_protocols.setter
    def support_protocols(self, value):
        if isinstance(value, list):
            self._support_protocols = list()
            for i in value:
                self._support_protocols.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpMcpDetailQueryResponse, self).parse_response_content(response_content)
        if 'ability_status' in response:
            self.ability_status = response['ability_status']
        if 'ability_version' in response:
            self.ability_version = response['ability_version']
        if 'encrypt_app_id' in response:
            self.encrypt_app_id = response['encrypt_app_id']
        if 'header_list' in response:
            self.header_list = response['header_list']
        if 'icon_url' in response:
            self.icon_url = response['icon_url']
        if 'mcp_chinese_name' in response:
            self.mcp_chinese_name = response['mcp_chinese_name']
        if 'mcp_desc' in response:
            self.mcp_desc = response['mcp_desc']
        if 'mcp_english_name' in response:
            self.mcp_english_name = response['mcp_english_name']
        if 'mcp_server_url' in response:
            self.mcp_server_url = response['mcp_server_url']
        if 'mcp_tool_list' in response:
            self.mcp_tool_list = response['mcp_tool_list']
        if 'request_timeout' in response:
            self.request_timeout = response['request_timeout']
        if 'response_timeout' in response:
            self.response_timeout = response['response_timeout']
        if 'support_account_type_list' in response:
            self.support_account_type_list = response['support_account_type_list']
        if 'support_protocols' in response:
            self.support_protocols = response['support_protocols']
