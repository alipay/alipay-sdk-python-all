#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RainysComplexRefSecond(object):

    def __init__(self):
        self._schema_param_boolean = None
        self._schema_param_num = None
        self._schema_param_string = None

    @property
    def schema_param_boolean(self):
        return self._schema_param_boolean

    @schema_param_boolean.setter
    def schema_param_boolean(self, value):
        if isinstance(value, list):
            self._schema_param_boolean = list()
            for i in value:
                self._schema_param_boolean.append(i)
    @property
    def schema_param_num(self):
        return self._schema_param_num

    @schema_param_num.setter
    def schema_param_num(self, value):
        self._schema_param_num = value
    @property
    def schema_param_string(self):
        return self._schema_param_string

    @schema_param_string.setter
    def schema_param_string(self, value):
        self._schema_param_string = value


    def to_alipay_dict(self):
        params = dict()
        if self.schema_param_boolean:
            if isinstance(self.schema_param_boolean, list):
                for i in range(0, len(self.schema_param_boolean)):
                    element = self.schema_param_boolean[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.schema_param_boolean[i] = element.to_alipay_dict()
            if hasattr(self.schema_param_boolean, 'to_alipay_dict'):
                params['schema_param_boolean'] = self.schema_param_boolean.to_alipay_dict()
            else:
                params['schema_param_boolean'] = self.schema_param_boolean
        if self.schema_param_num:
            if hasattr(self.schema_param_num, 'to_alipay_dict'):
                params['schema_param_num'] = self.schema_param_num.to_alipay_dict()
            else:
                params['schema_param_num'] = self.schema_param_num
        if self.schema_param_string:
            if hasattr(self.schema_param_string, 'to_alipay_dict'):
                params['schema_param_string'] = self.schema_param_string.to_alipay_dict()
            else:
                params['schema_param_string'] = self.schema_param_string
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainysComplexRefSecond()
        if 'schema_param_boolean' in d:
            o.schema_param_boolean = d['schema_param_boolean']
        if 'schema_param_num' in d:
            o.schema_param_num = d['schema_param_num']
        if 'schema_param_string' in d:
            o.schema_param_string = d['schema_param_string']
        return o


