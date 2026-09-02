#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpMcpDebugSubmitModel(object):

    def __init__(self):
        self._ability_code = None
        self._tool_code = None
        self._tool_schema = None

    @property
    def ability_code(self):
        return self._ability_code

    @ability_code.setter
    def ability_code(self, value):
        self._ability_code = value
    @property
    def tool_code(self):
        return self._tool_code

    @tool_code.setter
    def tool_code(self, value):
        self._tool_code = value
    @property
    def tool_schema(self):
        return self._tool_schema

    @tool_schema.setter
    def tool_schema(self, value):
        self._tool_schema = value


    def to_alipay_dict(self):
        params = dict()
        if self.ability_code:
            if hasattr(self.ability_code, 'to_alipay_dict'):
                params['ability_code'] = self.ability_code.to_alipay_dict()
            else:
                params['ability_code'] = self.ability_code
        if self.tool_code:
            if hasattr(self.tool_code, 'to_alipay_dict'):
                params['tool_code'] = self.tool_code.to_alipay_dict()
            else:
                params['tool_code'] = self.tool_code
        if self.tool_schema:
            if hasattr(self.tool_schema, 'to_alipay_dict'):
                params['tool_schema'] = self.tool_schema.to_alipay_dict()
            else:
                params['tool_schema'] = self.tool_schema
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpMcpDebugSubmitModel()
        if 'ability_code' in d:
            o.ability_code = d['ability_code']
        if 'tool_code' in d:
            o.tool_code = d['tool_code']
        if 'tool_schema' in d:
            o.tool_schema = d['tool_schema']
        return o


