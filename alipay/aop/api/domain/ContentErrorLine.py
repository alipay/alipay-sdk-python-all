#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContentErrorLine(object):

    def __init__(self):
        self._correct_value = None
        self._error_field = None
        self._error_value = None

    @property
    def correct_value(self):
        return self._correct_value

    @correct_value.setter
    def correct_value(self, value):
        self._correct_value = value
    @property
    def error_field(self):
        return self._error_field

    @error_field.setter
    def error_field(self, value):
        self._error_field = value
    @property
    def error_value(self):
        return self._error_value

    @error_value.setter
    def error_value(self, value):
        self._error_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.correct_value:
            if hasattr(self.correct_value, 'to_alipay_dict'):
                params['correct_value'] = self.correct_value.to_alipay_dict()
            else:
                params['correct_value'] = self.correct_value
        if self.error_field:
            if hasattr(self.error_field, 'to_alipay_dict'):
                params['error_field'] = self.error_field.to_alipay_dict()
            else:
                params['error_field'] = self.error_field
        if self.error_value:
            if hasattr(self.error_value, 'to_alipay_dict'):
                params['error_value'] = self.error_value.to_alipay_dict()
            else:
                params['error_value'] = self.error_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentErrorLine()
        if 'correct_value' in d:
            o.correct_value = d['correct_value']
        if 'error_field' in d:
            o.error_field = d['error_field']
        if 'error_value' in d:
            o.error_value = d['error_value']
        return o


