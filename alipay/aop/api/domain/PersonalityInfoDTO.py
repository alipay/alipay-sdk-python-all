#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PersonalityInfoDTO(object):

    def __init__(self):
        self._enum_code = None
        self._enum_id = None
        self._enum_name = None
        self._enum_value_code = None
        self._enum_value_name = None

    @property
    def enum_code(self):
        return self._enum_code

    @enum_code.setter
    def enum_code(self, value):
        self._enum_code = value
    @property
    def enum_id(self):
        return self._enum_id

    @enum_id.setter
    def enum_id(self, value):
        self._enum_id = value
    @property
    def enum_name(self):
        return self._enum_name

    @enum_name.setter
    def enum_name(self, value):
        self._enum_name = value
    @property
    def enum_value_code(self):
        return self._enum_value_code

    @enum_value_code.setter
    def enum_value_code(self, value):
        self._enum_value_code = value
    @property
    def enum_value_name(self):
        return self._enum_value_name

    @enum_value_name.setter
    def enum_value_name(self, value):
        self._enum_value_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.enum_code:
            if hasattr(self.enum_code, 'to_alipay_dict'):
                params['enum_code'] = self.enum_code.to_alipay_dict()
            else:
                params['enum_code'] = self.enum_code
        if self.enum_id:
            if hasattr(self.enum_id, 'to_alipay_dict'):
                params['enum_id'] = self.enum_id.to_alipay_dict()
            else:
                params['enum_id'] = self.enum_id
        if self.enum_name:
            if hasattr(self.enum_name, 'to_alipay_dict'):
                params['enum_name'] = self.enum_name.to_alipay_dict()
            else:
                params['enum_name'] = self.enum_name
        if self.enum_value_code:
            if hasattr(self.enum_value_code, 'to_alipay_dict'):
                params['enum_value_code'] = self.enum_value_code.to_alipay_dict()
            else:
                params['enum_value_code'] = self.enum_value_code
        if self.enum_value_name:
            if hasattr(self.enum_value_name, 'to_alipay_dict'):
                params['enum_value_name'] = self.enum_value_name.to_alipay_dict()
            else:
                params['enum_value_name'] = self.enum_value_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PersonalityInfoDTO()
        if 'enum_code' in d:
            o.enum_code = d['enum_code']
        if 'enum_id' in d:
            o.enum_id = d['enum_id']
        if 'enum_name' in d:
            o.enum_name = d['enum_name']
        if 'enum_value_code' in d:
            o.enum_value_code = d['enum_value_code']
        if 'enum_value_name' in d:
            o.enum_value_name = d['enum_value_name']
        return o


