#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SolutionOpenApiVO(object):

    def __init__(self):
        self._solution_code = None
        self._solution_name = None

    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value
    @property
    def solution_name(self):
        return self._solution_name

    @solution_name.setter
    def solution_name(self, value):
        self._solution_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        if self.solution_name:
            if hasattr(self.solution_name, 'to_alipay_dict'):
                params['solution_name'] = self.solution_name.to_alipay_dict()
            else:
                params['solution_name'] = self.solution_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SolutionOpenApiVO()
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        if 'solution_name' in d:
            o.solution_name = d['solution_name']
        return o


