#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ErrorCodeDTO(object):

    def __init__(self):
        self._description = None
        self._error_code = None
        self._solution = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def solution(self):
        return self._solution

    @solution.setter
    def solution(self, value):
        self._solution = value


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.solution:
            if hasattr(self.solution, 'to_alipay_dict'):
                params['solution'] = self.solution.to_alipay_dict()
            else:
                params['solution'] = self.solution
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ErrorCodeDTO()
        if 'description' in d:
            o.description = d['description']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'solution' in d:
            o.solution = d['solution']
        return o


