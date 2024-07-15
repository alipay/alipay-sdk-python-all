#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenOperationOption import OpenOperationOption


class OpenCrowdOperationOption(object):

    def __init__(self):
        self._option_code = None
        self._option_data_type = None
        self._option_list = None
        self._option_name = None

    @property
    def option_code(self):
        return self._option_code

    @option_code.setter
    def option_code(self, value):
        self._option_code = value
    @property
    def option_data_type(self):
        return self._option_data_type

    @option_data_type.setter
    def option_data_type(self, value):
        self._option_data_type = value
    @property
    def option_list(self):
        return self._option_list

    @option_list.setter
    def option_list(self, value):
        if isinstance(value, list):
            self._option_list = list()
            for i in value:
                if isinstance(i, OpenOperationOption):
                    self._option_list.append(i)
                else:
                    self._option_list.append(OpenOperationOption.from_alipay_dict(i))
    @property
    def option_name(self):
        return self._option_name

    @option_name.setter
    def option_name(self, value):
        self._option_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.option_code:
            if hasattr(self.option_code, 'to_alipay_dict'):
                params['option_code'] = self.option_code.to_alipay_dict()
            else:
                params['option_code'] = self.option_code
        if self.option_data_type:
            if hasattr(self.option_data_type, 'to_alipay_dict'):
                params['option_data_type'] = self.option_data_type.to_alipay_dict()
            else:
                params['option_data_type'] = self.option_data_type
        if self.option_list:
            if isinstance(self.option_list, list):
                for i in range(0, len(self.option_list)):
                    element = self.option_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.option_list[i] = element.to_alipay_dict()
            if hasattr(self.option_list, 'to_alipay_dict'):
                params['option_list'] = self.option_list.to_alipay_dict()
            else:
                params['option_list'] = self.option_list
        if self.option_name:
            if hasattr(self.option_name, 'to_alipay_dict'):
                params['option_name'] = self.option_name.to_alipay_dict()
            else:
                params['option_name'] = self.option_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenCrowdOperationOption()
        if 'option_code' in d:
            o.option_code = d['option_code']
        if 'option_data_type' in d:
            o.option_data_type = d['option_data_type']
        if 'option_list' in d:
            o.option_list = d['option_list']
        if 'option_name' in d:
            o.option_name = d['option_name']
        return o


