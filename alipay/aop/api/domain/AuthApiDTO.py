#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AuthApiDTO(object):

    def __init__(self):
        self._api_name = None
        self._field_name = None
        self._package_code = None

    @property
    def api_name(self):
        return self._api_name

    @api_name.setter
    def api_name(self, value):
        self._api_name = value
    @property
    def field_name(self):
        return self._field_name

    @field_name.setter
    def field_name(self, value):
        self._field_name = value
    @property
    def package_code(self):
        return self._package_code

    @package_code.setter
    def package_code(self, value):
        self._package_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_name:
            if hasattr(self.api_name, 'to_alipay_dict'):
                params['api_name'] = self.api_name.to_alipay_dict()
            else:
                params['api_name'] = self.api_name
        if self.field_name:
            if hasattr(self.field_name, 'to_alipay_dict'):
                params['field_name'] = self.field_name.to_alipay_dict()
            else:
                params['field_name'] = self.field_name
        if self.package_code:
            if hasattr(self.package_code, 'to_alipay_dict'):
                params['package_code'] = self.package_code.to_alipay_dict()
            else:
                params['package_code'] = self.package_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthApiDTO()
        if 'api_name' in d:
            o.api_name = d['api_name']
        if 'field_name' in d:
            o.field_name = d['field_name']
        if 'package_code' in d:
            o.package_code = d['package_code']
        return o


