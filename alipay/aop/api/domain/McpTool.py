#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class McpTool(object):

    def __init__(self):
        self._input_schema_examples = None
        self._output_schema_examples = None
        self._tool_code = None
        self._tool_name = None
        self._tool_schema = None
        self._tool_version = None

    @property
    def input_schema_examples(self):
        return self._input_schema_examples

    @input_schema_examples.setter
    def input_schema_examples(self, value):
        if isinstance(value, list):
            self._input_schema_examples = list()
            for i in value:
                self._input_schema_examples.append(i)
    @property
    def output_schema_examples(self):
        return self._output_schema_examples

    @output_schema_examples.setter
    def output_schema_examples(self, value):
        if isinstance(value, list):
            self._output_schema_examples = list()
            for i in value:
                self._output_schema_examples.append(i)
    @property
    def tool_code(self):
        return self._tool_code

    @tool_code.setter
    def tool_code(self, value):
        self._tool_code = value
    @property
    def tool_name(self):
        return self._tool_name

    @tool_name.setter
    def tool_name(self, value):
        self._tool_name = value
    @property
    def tool_schema(self):
        return self._tool_schema

    @tool_schema.setter
    def tool_schema(self, value):
        self._tool_schema = value
    @property
    def tool_version(self):
        return self._tool_version

    @tool_version.setter
    def tool_version(self, value):
        self._tool_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.input_schema_examples:
            if isinstance(self.input_schema_examples, list):
                for i in range(0, len(self.input_schema_examples)):
                    element = self.input_schema_examples[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.input_schema_examples[i] = element.to_alipay_dict()
            if hasattr(self.input_schema_examples, 'to_alipay_dict'):
                params['input_schema_examples'] = self.input_schema_examples.to_alipay_dict()
            else:
                params['input_schema_examples'] = self.input_schema_examples
        if self.output_schema_examples:
            if isinstance(self.output_schema_examples, list):
                for i in range(0, len(self.output_schema_examples)):
                    element = self.output_schema_examples[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.output_schema_examples[i] = element.to_alipay_dict()
            if hasattr(self.output_schema_examples, 'to_alipay_dict'):
                params['output_schema_examples'] = self.output_schema_examples.to_alipay_dict()
            else:
                params['output_schema_examples'] = self.output_schema_examples
        if self.tool_code:
            if hasattr(self.tool_code, 'to_alipay_dict'):
                params['tool_code'] = self.tool_code.to_alipay_dict()
            else:
                params['tool_code'] = self.tool_code
        if self.tool_name:
            if hasattr(self.tool_name, 'to_alipay_dict'):
                params['tool_name'] = self.tool_name.to_alipay_dict()
            else:
                params['tool_name'] = self.tool_name
        if self.tool_schema:
            if hasattr(self.tool_schema, 'to_alipay_dict'):
                params['tool_schema'] = self.tool_schema.to_alipay_dict()
            else:
                params['tool_schema'] = self.tool_schema
        if self.tool_version:
            if hasattr(self.tool_version, 'to_alipay_dict'):
                params['tool_version'] = self.tool_version.to_alipay_dict()
            else:
                params['tool_version'] = self.tool_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = McpTool()
        if 'input_schema_examples' in d:
            o.input_schema_examples = d['input_schema_examples']
        if 'output_schema_examples' in d:
            o.output_schema_examples = d['output_schema_examples']
        if 'tool_code' in d:
            o.tool_code = d['tool_code']
        if 'tool_name' in d:
            o.tool_name = d['tool_name']
        if 'tool_schema' in d:
            o.tool_schema = d['tool_schema']
        if 'tool_version' in d:
            o.tool_version = d['tool_version']
        return o


