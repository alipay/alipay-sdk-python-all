#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNcoilopenReferenceCreateModel(object):

    def __init__(self):
        self._solution_id = None
        self._sub_solution_id = None
        self._template_code = None

    @property
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value
    @property
    def sub_solution_id(self):
        return self._sub_solution_id

    @sub_solution_id.setter
    def sub_solution_id(self, value):
        self._sub_solution_id = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.solution_id:
            if hasattr(self.solution_id, 'to_alipay_dict'):
                params['solution_id'] = self.solution_id.to_alipay_dict()
            else:
                params['solution_id'] = self.solution_id
        if self.sub_solution_id:
            if hasattr(self.sub_solution_id, 'to_alipay_dict'):
                params['sub_solution_id'] = self.sub_solution_id.to_alipay_dict()
            else:
                params['sub_solution_id'] = self.sub_solution_id
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNcoilopenReferenceCreateModel()
        if 'solution_id' in d:
            o.solution_id = d['solution_id']
        if 'sub_solution_id' in d:
            o.sub_solution_id = d['sub_solution_id']
        if 'template_code' in d:
            o.template_code = d['template_code']
        return o


