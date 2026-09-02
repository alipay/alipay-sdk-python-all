#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ToolInfo import ToolInfo


class AlipayOpenSpMcpToolAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpMcpToolAddResponse, self).__init__()
        self._tool_info_list = None

    @property
    def tool_info_list(self):
        return self._tool_info_list

    @tool_info_list.setter
    def tool_info_list(self, value):
        if isinstance(value, list):
            self._tool_info_list = list()
            for i in value:
                if isinstance(i, ToolInfo):
                    self._tool_info_list.append(i)
                else:
                    self._tool_info_list.append(ToolInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpMcpToolAddResponse, self).parse_response_content(response_content)
        if 'tool_info_list' in response:
            self.tool_info_list = response['tool_info_list']
