#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplatePlaceholderDTO(object):

    def __init__(self):
        self._placeholder_key = None
        self._placeholder_value = None

    @property
    def placeholder_key(self):
        return self._placeholder_key

    @placeholder_key.setter
    def placeholder_key(self, value):
        self._placeholder_key = value
    @property
    def placeholder_value(self):
        return self._placeholder_value

    @placeholder_value.setter
    def placeholder_value(self, value):
        self._placeholder_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.placeholder_key:
            if hasattr(self.placeholder_key, 'to_alipay_dict'):
                params['placeholder_key'] = self.placeholder_key.to_alipay_dict()
            else:
                params['placeholder_key'] = self.placeholder_key
        if self.placeholder_value:
            if hasattr(self.placeholder_value, 'to_alipay_dict'):
                params['placeholder_value'] = self.placeholder_value.to_alipay_dict()
            else:
                params['placeholder_value'] = self.placeholder_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplatePlaceholderDTO()
        if 'placeholder_key' in d:
            o.placeholder_key = d['placeholder_key']
        if 'placeholder_value' in d:
            o.placeholder_value = d['placeholder_value']
        return o


