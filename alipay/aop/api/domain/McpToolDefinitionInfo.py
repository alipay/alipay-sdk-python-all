#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class McpToolDefinitionInfo(object):

    def __init__(self):
        self._input_schema = None
        self._output_schema = None
        self._required = None
        self._tool_desc = None
        self._tool_label = None
        self._tool_name = None

    @property
    def input_schema(self):
        return self._input_schema

    @input_schema.setter
    def input_schema(self, value):
        self._input_schema = value
    @property
    def output_schema(self):
        return self._output_schema

    @output_schema.setter
    def output_schema(self, value):
        self._output_schema = value
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value
    @property
    def tool_desc(self):
        return self._tool_desc

    @tool_desc.setter
    def tool_desc(self, value):
        self._tool_desc = value
    @property
    def tool_label(self):
        return self._tool_label

    @tool_label.setter
    def tool_label(self, value):
        self._tool_label = value
    @property
    def tool_name(self):
        return self._tool_name

    @tool_name.setter
    def tool_name(self, value):
        self._tool_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.input_schema:
            if hasattr(self.input_schema, 'to_alipay_dict'):
                params['input_schema'] = self.input_schema.to_alipay_dict()
            else:
                params['input_schema'] = self.input_schema
        if self.output_schema:
            if hasattr(self.output_schema, 'to_alipay_dict'):
                params['output_schema'] = self.output_schema.to_alipay_dict()
            else:
                params['output_schema'] = self.output_schema
        if self.required:
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
        if self.tool_desc:
            if hasattr(self.tool_desc, 'to_alipay_dict'):
                params['tool_desc'] = self.tool_desc.to_alipay_dict()
            else:
                params['tool_desc'] = self.tool_desc
        if self.tool_label:
            if hasattr(self.tool_label, 'to_alipay_dict'):
                params['tool_label'] = self.tool_label.to_alipay_dict()
            else:
                params['tool_label'] = self.tool_label
        if self.tool_name:
            if hasattr(self.tool_name, 'to_alipay_dict'):
                params['tool_name'] = self.tool_name.to_alipay_dict()
            else:
                params['tool_name'] = self.tool_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = McpToolDefinitionInfo()
        if 'input_schema' in d:
            o.input_schema = d['input_schema']
        if 'output_schema' in d:
            o.output_schema = d['output_schema']
        if 'required' in d:
            o.required = d['required']
        if 'tool_desc' in d:
            o.tool_desc = d['tool_desc']
        if 'tool_label' in d:
            o.tool_label = d['tool_label']
        if 'tool_name' in d:
            o.tool_name = d['tool_name']
        return o


