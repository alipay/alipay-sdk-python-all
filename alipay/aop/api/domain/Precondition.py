#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Precondition(object):

    def __init__(self):
        self._equivalent_relation = None
        self._input_param = None
        self._output_param = None

    @property
    def equivalent_relation(self):
        return self._equivalent_relation

    @equivalent_relation.setter
    def equivalent_relation(self, value):
        self._equivalent_relation = value
    @property
    def input_param(self):
        return self._input_param

    @input_param.setter
    def input_param(self, value):
        self._input_param = value
    @property
    def output_param(self):
        return self._output_param

    @output_param.setter
    def output_param(self, value):
        self._output_param = value


    def to_alipay_dict(self):
        params = dict()
        if self.equivalent_relation:
            if hasattr(self.equivalent_relation, 'to_alipay_dict'):
                params['equivalent_relation'] = self.equivalent_relation.to_alipay_dict()
            else:
                params['equivalent_relation'] = self.equivalent_relation
        if self.input_param:
            if hasattr(self.input_param, 'to_alipay_dict'):
                params['input_param'] = self.input_param.to_alipay_dict()
            else:
                params['input_param'] = self.input_param
        if self.output_param:
            if hasattr(self.output_param, 'to_alipay_dict'):
                params['output_param'] = self.output_param.to_alipay_dict()
            else:
                params['output_param'] = self.output_param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Precondition()
        if 'equivalent_relation' in d:
            o.equivalent_relation = d['equivalent_relation']
        if 'input_param' in d:
            o.input_param = d['input_param']
        if 'output_param' in d:
            o.output_param = d['output_param']
        return o


