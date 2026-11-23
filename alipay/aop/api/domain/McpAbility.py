#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.McpAuthorization import McpAuthorization
from alipay.aop.api.domain.McpTool import McpTool


class McpAbility(object):

    def __init__(self):
        self._authorization = None
        self._opengw_url = None
        self._server_discovery_code = None
        self._tool_list = None

    @property
    def authorization(self):
        return self._authorization

    @authorization.setter
    def authorization(self, value):
        if isinstance(value, list):
            self._authorization = list()
            for i in value:
                if isinstance(i, McpAuthorization):
                    self._authorization.append(i)
                else:
                    self._authorization.append(McpAuthorization.from_alipay_dict(i))
    @property
    def opengw_url(self):
        return self._opengw_url

    @opengw_url.setter
    def opengw_url(self, value):
        self._opengw_url = value
    @property
    def server_discovery_code(self):
        return self._server_discovery_code

    @server_discovery_code.setter
    def server_discovery_code(self, value):
        self._server_discovery_code = value
    @property
    def tool_list(self):
        return self._tool_list

    @tool_list.setter
    def tool_list(self, value):
        if isinstance(value, list):
            self._tool_list = list()
            for i in value:
                if isinstance(i, McpTool):
                    self._tool_list.append(i)
                else:
                    self._tool_list.append(McpTool.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.authorization:
            if isinstance(self.authorization, list):
                for i in range(0, len(self.authorization)):
                    element = self.authorization[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.authorization[i] = element.to_alipay_dict()
            if hasattr(self.authorization, 'to_alipay_dict'):
                params['authorization'] = self.authorization.to_alipay_dict()
            else:
                params['authorization'] = self.authorization
        if self.opengw_url:
            if hasattr(self.opengw_url, 'to_alipay_dict'):
                params['opengw_url'] = self.opengw_url.to_alipay_dict()
            else:
                params['opengw_url'] = self.opengw_url
        if self.server_discovery_code:
            if hasattr(self.server_discovery_code, 'to_alipay_dict'):
                params['server_discovery_code'] = self.server_discovery_code.to_alipay_dict()
            else:
                params['server_discovery_code'] = self.server_discovery_code
        if self.tool_list:
            if isinstance(self.tool_list, list):
                for i in range(0, len(self.tool_list)):
                    element = self.tool_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tool_list[i] = element.to_alipay_dict()
            if hasattr(self.tool_list, 'to_alipay_dict'):
                params['tool_list'] = self.tool_list.to_alipay_dict()
            else:
                params['tool_list'] = self.tool_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = McpAbility()
        if 'authorization' in d:
            o.authorization = d['authorization']
        if 'opengw_url' in d:
            o.opengw_url = d['opengw_url']
        if 'server_discovery_code' in d:
            o.server_discovery_code = d['server_discovery_code']
        if 'tool_list' in d:
            o.tool_list = d['tool_list']
        return o


