#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenCrowdOperationOption import OpenCrowdOperationOption


class OpenCrowdOperationTag(object):

    def __init__(self):
        self._operation_option_list = None
        self._tag_code = None
        self._tag_desc = None
        self._tag_name = None

    @property
    def operation_option_list(self):
        return self._operation_option_list

    @operation_option_list.setter
    def operation_option_list(self, value):
        if isinstance(value, list):
            self._operation_option_list = list()
            for i in value:
                if isinstance(i, OpenCrowdOperationOption):
                    self._operation_option_list.append(i)
                else:
                    self._operation_option_list.append(OpenCrowdOperationOption.from_alipay_dict(i))
    @property
    def tag_code(self):
        return self._tag_code

    @tag_code.setter
    def tag_code(self, value):
        self._tag_code = value
    @property
    def tag_desc(self):
        return self._tag_desc

    @tag_desc.setter
    def tag_desc(self, value):
        self._tag_desc = value
    @property
    def tag_name(self):
        return self._tag_name

    @tag_name.setter
    def tag_name(self, value):
        self._tag_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.operation_option_list:
            if isinstance(self.operation_option_list, list):
                for i in range(0, len(self.operation_option_list)):
                    element = self.operation_option_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operation_option_list[i] = element.to_alipay_dict()
            if hasattr(self.operation_option_list, 'to_alipay_dict'):
                params['operation_option_list'] = self.operation_option_list.to_alipay_dict()
            else:
                params['operation_option_list'] = self.operation_option_list
        if self.tag_code:
            if hasattr(self.tag_code, 'to_alipay_dict'):
                params['tag_code'] = self.tag_code.to_alipay_dict()
            else:
                params['tag_code'] = self.tag_code
        if self.tag_desc:
            if hasattr(self.tag_desc, 'to_alipay_dict'):
                params['tag_desc'] = self.tag_desc.to_alipay_dict()
            else:
                params['tag_desc'] = self.tag_desc
        if self.tag_name:
            if hasattr(self.tag_name, 'to_alipay_dict'):
                params['tag_name'] = self.tag_name.to_alipay_dict()
            else:
                params['tag_name'] = self.tag_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenCrowdOperationTag()
        if 'operation_option_list' in d:
            o.operation_option_list = d['operation_option_list']
        if 'tag_code' in d:
            o.tag_code = d['tag_code']
        if 'tag_desc' in d:
            o.tag_desc = d['tag_desc']
        if 'tag_name' in d:
            o.tag_name = d['tag_name']
        return o


