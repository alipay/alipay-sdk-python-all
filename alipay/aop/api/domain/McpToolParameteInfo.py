#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ToolParameterInfo import ToolParameterInfo
from alipay.aop.api.domain.ToolParameterInfo import ToolParameterInfo


class McpToolParameteInfo(object):

    def __init__(self):
        self._input_parameter_list = None
        self._output_parameter_list = None
        self._tool_description = None
        self._tool_en_name = None

    @property
    def input_parameter_list(self):
        return self._input_parameter_list

    @input_parameter_list.setter
    def input_parameter_list(self, value):
        if isinstance(value, list):
            self._input_parameter_list = list()
            for i in value:
                if isinstance(i, ToolParameterInfo):
                    self._input_parameter_list.append(i)
                else:
                    self._input_parameter_list.append(ToolParameterInfo.from_alipay_dict(i))
    @property
    def output_parameter_list(self):
        return self._output_parameter_list

    @output_parameter_list.setter
    def output_parameter_list(self, value):
        if isinstance(value, list):
            self._output_parameter_list = list()
            for i in value:
                if isinstance(i, ToolParameterInfo):
                    self._output_parameter_list.append(i)
                else:
                    self._output_parameter_list.append(ToolParameterInfo.from_alipay_dict(i))
    @property
    def tool_description(self):
        return self._tool_description

    @tool_description.setter
    def tool_description(self, value):
        self._tool_description = value
    @property
    def tool_en_name(self):
        return self._tool_en_name

    @tool_en_name.setter
    def tool_en_name(self, value):
        self._tool_en_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.input_parameter_list:
            if isinstance(self.input_parameter_list, list):
                for i in range(0, len(self.input_parameter_list)):
                    element = self.input_parameter_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.input_parameter_list[i] = element.to_alipay_dict()
            if hasattr(self.input_parameter_list, 'to_alipay_dict'):
                params['input_parameter_list'] = self.input_parameter_list.to_alipay_dict()
            else:
                params['input_parameter_list'] = self.input_parameter_list
        if self.output_parameter_list:
            if isinstance(self.output_parameter_list, list):
                for i in range(0, len(self.output_parameter_list)):
                    element = self.output_parameter_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.output_parameter_list[i] = element.to_alipay_dict()
            if hasattr(self.output_parameter_list, 'to_alipay_dict'):
                params['output_parameter_list'] = self.output_parameter_list.to_alipay_dict()
            else:
                params['output_parameter_list'] = self.output_parameter_list
        if self.tool_description:
            if hasattr(self.tool_description, 'to_alipay_dict'):
                params['tool_description'] = self.tool_description.to_alipay_dict()
            else:
                params['tool_description'] = self.tool_description
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
        o = McpToolParameteInfo()
        if 'input_parameter_list' in d:
            o.input_parameter_list = d['input_parameter_list']
        if 'output_parameter_list' in d:
            o.output_parameter_list = d['output_parameter_list']
        if 'tool_description' in d:
            o.tool_description = d['tool_description']
        if 'tool_en_name' in d:
            o.tool_en_name = d['tool_en_name']
        return o


