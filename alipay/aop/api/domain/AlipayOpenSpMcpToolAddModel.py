#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.McpToolParameteInfo import McpToolParameteInfo


class AlipayOpenSpMcpToolAddModel(object):

    def __init__(self):
        self._ability_code = None
        self._add_type = None
        self._mcp_tool_info_list = None

    @property
    def ability_code(self):
        return self._ability_code

    @ability_code.setter
    def ability_code(self, value):
        self._ability_code = value
    @property
    def add_type(self):
        return self._add_type

    @add_type.setter
    def add_type(self, value):
        self._add_type = value
    @property
    def mcp_tool_info_list(self):
        return self._mcp_tool_info_list

    @mcp_tool_info_list.setter
    def mcp_tool_info_list(self, value):
        if isinstance(value, list):
            self._mcp_tool_info_list = list()
            for i in value:
                if isinstance(i, McpToolParameteInfo):
                    self._mcp_tool_info_list.append(i)
                else:
                    self._mcp_tool_info_list.append(McpToolParameteInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.ability_code:
            if hasattr(self.ability_code, 'to_alipay_dict'):
                params['ability_code'] = self.ability_code.to_alipay_dict()
            else:
                params['ability_code'] = self.ability_code
        if self.add_type:
            if hasattr(self.add_type, 'to_alipay_dict'):
                params['add_type'] = self.add_type.to_alipay_dict()
            else:
                params['add_type'] = self.add_type
        if self.mcp_tool_info_list:
            if isinstance(self.mcp_tool_info_list, list):
                for i in range(0, len(self.mcp_tool_info_list)):
                    element = self.mcp_tool_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mcp_tool_info_list[i] = element.to_alipay_dict()
            if hasattr(self.mcp_tool_info_list, 'to_alipay_dict'):
                params['mcp_tool_info_list'] = self.mcp_tool_info_list.to_alipay_dict()
            else:
                params['mcp_tool_info_list'] = self.mcp_tool_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpMcpToolAddModel()
        if 'ability_code' in d:
            o.ability_code = d['ability_code']
        if 'add_type' in d:
            o.add_type = d['add_type']
        if 'mcp_tool_info_list' in d:
            o.mcp_tool_info_list = d['mcp_tool_info_list']
        return o


