#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationPlanetsolutioncenterIsvBindModel(object):

    def __init__(self):
        self._solution_code = None

    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationPlanetsolutioncenterIsvBindModel()
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        return o


