#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class McpRel(object):

    def __init__(self):
        self._mcp_ability_code = None

    @property
    def mcp_ability_code(self):
        return self._mcp_ability_code

    @mcp_ability_code.setter
    def mcp_ability_code(self, value):
        self._mcp_ability_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.mcp_ability_code:
            if hasattr(self.mcp_ability_code, 'to_alipay_dict'):
                params['mcp_ability_code'] = self.mcp_ability_code.to_alipay_dict()
            else:
                params['mcp_ability_code'] = self.mcp_ability_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = McpRel()
        if 'mcp_ability_code' in d:
            o.mcp_ability_code = d['mcp_ability_code']
        return o


