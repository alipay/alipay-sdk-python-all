#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GlobalParam import GlobalParam
from alipay.aop.api.domain.McpToolDefinitionInfo import McpToolDefinitionInfo
from alipay.aop.api.domain.TemplateInfoVO import TemplateInfoVO


class AlipayOpenSpSkillTemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpSkillTemplateQueryResponse, self).__init__()
        self._global_param_list = None
        self._mcp_tool_list = None
        self._preset_query_list = None
        self._template_info = None

    @property
    def global_param_list(self):
        return self._global_param_list

    @global_param_list.setter
    def global_param_list(self, value):
        if isinstance(value, list):
            self._global_param_list = list()
            for i in value:
                if isinstance(i, GlobalParam):
                    self._global_param_list.append(i)
                else:
                    self._global_param_list.append(GlobalParam.from_alipay_dict(i))
    @property
    def mcp_tool_list(self):
        return self._mcp_tool_list

    @mcp_tool_list.setter
    def mcp_tool_list(self, value):
        if isinstance(value, list):
            self._mcp_tool_list = list()
            for i in value:
                if isinstance(i, McpToolDefinitionInfo):
                    self._mcp_tool_list.append(i)
                else:
                    self._mcp_tool_list.append(McpToolDefinitionInfo.from_alipay_dict(i))
    @property
    def preset_query_list(self):
        return self._preset_query_list

    @preset_query_list.setter
    def preset_query_list(self, value):
        if isinstance(value, list):
            self._preset_query_list = list()
            for i in value:
                self._preset_query_list.append(i)
    @property
    def template_info(self):
        return self._template_info

    @template_info.setter
    def template_info(self, value):
        if isinstance(value, TemplateInfoVO):
            self._template_info = value
        else:
            self._template_info = TemplateInfoVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpSkillTemplateQueryResponse, self).parse_response_content(response_content)
        if 'global_param_list' in response:
            self.global_param_list = response['global_param_list']
        if 'mcp_tool_list' in response:
            self.mcp_tool_list = response['mcp_tool_list']
        if 'preset_query_list' in response:
            self.preset_query_list = response['preset_query_list']
        if 'template_info' in response:
            self.template_info = response['template_info']
