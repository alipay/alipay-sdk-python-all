#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AttrPathItemDTO(object):

    def __init__(self):
        self._code = None
        self._real_name = None
        self._type = None
        self._view_name = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def view_name(self):
        return self._view_name

    @view_name.setter
    def view_name(self, value):
        self._view_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.view_name:
            if hasattr(self.view_name, 'to_alipay_dict'):
                params['view_name'] = self.view_name.to_alipay_dict()
            else:
                params['view_name'] = self.view_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AttrPathItemDTO()
        if 'code' in d:
            o.code = d['code']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'type' in d:
            o.type = d['type']
        if 'view_name' in d:
            o.view_name = d['view_name']
        return o


