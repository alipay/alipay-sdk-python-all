#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ToolParameterInfos import ToolParameterInfos
from alipay.aop.api.domain.ToolParameterInfos import ToolParameterInfos


class McpToolList(object):

    def __init__(self):
        self._biz_status = None
        self._input_parameter_list = None
        self._output_parameter_list = None
        self._tool_cn_name = None
        self._tool_code = None
        self._tool_description = None
        self._tool_en_name = None
        self._tool_version = None

    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def input_parameter_list(self):
        return self._input_parameter_list

    @input_parameter_list.setter
    def input_parameter_list(self, value):
        if isinstance(value, list):
            self._input_parameter_list = list()
            for i in value:
                if isinstance(i, ToolParameterInfos):
                    self._input_parameter_list.append(i)
                else:
                    self._input_parameter_list.append(ToolParameterInfos.from_alipay_dict(i))
    @property
    def output_parameter_list(self):
        return self._output_parameter_list

    @output_parameter_list.setter
    def output_parameter_list(self, value):
        if isinstance(value, list):
            self._output_parameter_list = list()
            for i in value:
                if isinstance(i, ToolParameterInfos):
                    self._output_parameter_list.append(i)
                else:
                    self._output_parameter_list.append(ToolParameterInfos.from_alipay_dict(i))
    @property
    def tool_cn_name(self):
        return self._tool_cn_name

    @tool_cn_name.setter
    def tool_cn_name(self, value):
        self._tool_cn_name = value
    @property
    def tool_code(self):
        return self._tool_code

    @tool_code.setter
    def tool_code(self, value):
        self._tool_code = value
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
    @property
    def tool_version(self):
        return self._tool_version

    @tool_version.setter
    def tool_version(self, value):
        self._tool_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_status:
            if hasattr(self.biz_status, 'to_alipay_dict'):
                params['biz_status'] = self.biz_status.to_alipay_dict()
            else:
                params['biz_status'] = self.biz_status
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
        if self.tool_cn_name:
            if hasattr(self.tool_cn_name, 'to_alipay_dict'):
                params['tool_cn_name'] = self.tool_cn_name.to_alipay_dict()
            else:
                params['tool_cn_name'] = self.tool_cn_name
        if self.tool_code:
            if hasattr(self.tool_code, 'to_alipay_dict'):
                params['tool_code'] = self.tool_code.to_alipay_dict()
            else:
                params['tool_code'] = self.tool_code
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
        o = McpToolList()
        if 'biz_status' in d:
            o.biz_status = d['biz_status']
        if 'input_parameter_list' in d:
            o.input_parameter_list = d['input_parameter_list']
        if 'output_parameter_list' in d:
            o.output_parameter_list = d['output_parameter_list']
        if 'tool_cn_name' in d:
            o.tool_cn_name = d['tool_cn_name']
        if 'tool_code' in d:
            o.tool_code = d['tool_code']
        if 'tool_description' in d:
            o.tool_description = d['tool_description']
        if 'tool_en_name' in d:
            o.tool_en_name = d['tool_en_name']
        if 'tool_version' in d:
            o.tool_version = d['tool_version']
        return o


