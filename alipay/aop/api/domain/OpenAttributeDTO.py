#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenAttributeDTO(object):

    def __init__(self):
        self._filed_name = None
        self._filed_value = None

    @property
    def filed_name(self):
        return self._filed_name

    @filed_name.setter
    def filed_name(self, value):
        self._filed_name = value
    @property
    def filed_value(self):
        return self._filed_value

    @filed_value.setter
    def filed_value(self, value):
        self._filed_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.filed_name:
            if hasattr(self.filed_name, 'to_alipay_dict'):
                params['filed_name'] = self.filed_name.to_alipay_dict()
            else:
                params['filed_name'] = self.filed_name
        if self.filed_value:
            if hasattr(self.filed_value, 'to_alipay_dict'):
                params['filed_value'] = self.filed_value.to_alipay_dict()
            else:
                params['filed_value'] = self.filed_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenAttributeDTO()
        if 'filed_name' in d:
            o.filed_name = d['filed_name']
        if 'filed_value' in d:
            o.filed_value = d['filed_value']
        return o


