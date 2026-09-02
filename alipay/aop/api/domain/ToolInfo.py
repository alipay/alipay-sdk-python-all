#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ToolInfo(object):

    def __init__(self):
        self._tool_code = None
        self._tool_en_name = None

    @property
    def tool_code(self):
        return self._tool_code

    @tool_code.setter
    def tool_code(self, value):
        self._tool_code = value
    @property
    def tool_en_name(self):
        return self._tool_en_name

    @tool_en_name.setter
    def tool_en_name(self, value):
        self._tool_en_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.tool_code:
            if hasattr(self.tool_code, 'to_alipay_dict'):
                params['tool_code'] = self.tool_code.to_alipay_dict()
            else:
                params['tool_code'] = self.tool_code
        if self.tool_en_name:
            if hasattr(self.tool_en_name, 'to_alipay_dict'):
                params['tool_en_name'] = self.tool_en_name.to_alipay_dict()
            else:
                params['tool_en_name'] = self.tool_en_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ToolInfo()
        if 'tool_code' in d:
            o.tool_code = d['tool_code']
        if 'tool_en_name' in d:
            o.tool_en_name = d['tool_en_name']
        return o


