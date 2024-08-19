#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FunctionInfo(object):

    def __init__(self):
        self._function_description = None
        self._function_name = None
        self._version_description = None
        self._version_name = None

    @property
    def function_description(self):
        return self._function_description

    @function_description.setter
    def function_description(self, value):
        self._function_description = value
    @property
    def function_name(self):
        return self._function_name

    @function_name.setter
    def function_name(self, value):
        self._function_name = value
    @property
    def version_description(self):
        return self._version_description

    @version_description.setter
    def version_description(self, value):
        self._version_description = value
    @property
    def version_name(self):
        return self._version_name

    @version_name.setter
    def version_name(self, value):
        self._version_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.function_description:
            if hasattr(self.function_description, 'to_alipay_dict'):
                params['function_description'] = self.function_description.to_alipay_dict()
            else:
                params['function_description'] = self.function_description
        if self.function_name:
            if hasattr(self.function_name, 'to_alipay_dict'):
                params['function_name'] = self.function_name.to_alipay_dict()
            else:
                params['function_name'] = self.function_name
        if self.version_description:
            if hasattr(self.version_description, 'to_alipay_dict'):
                params['version_description'] = self.version_description.to_alipay_dict()
            else:
                params['version_description'] = self.version_description
        if self.version_name:
            if hasattr(self.version_name, 'to_alipay_dict'):
                params['version_name'] = self.version_name.to_alipay_dict()
            else:
                params['version_name'] = self.version_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FunctionInfo()
        if 'function_description' in d:
            o.function_description = d['function_description']
        if 'function_name' in d:
            o.function_name = d['function_name']
        if 'version_description' in d:
            o.version_description = d['version_description']
        if 'version_name' in d:
            o.version_name = d['version_name']
        return o


