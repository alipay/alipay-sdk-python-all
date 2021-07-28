#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FixProblemDTO(object):

    def __init__(self):
        self._id = None
        self._problem_level_1 = None
        self._problem_level_2 = None
        self._problem_level_3 = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def problem_level_1(self):
        return self._problem_level_1

    @problem_level_1.setter
    def problem_level_1(self, value):
        self._problem_level_1 = value
    @property
    def problem_level_2(self):
        return self._problem_level_2

    @problem_level_2.setter
    def problem_level_2(self, value):
        self._problem_level_2 = value
    @property
    def problem_level_3(self):
        return self._problem_level_3

    @problem_level_3.setter
    def problem_level_3(self, value):
        self._problem_level_3 = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.problem_level_1:
            if hasattr(self.problem_level_1, 'to_alipay_dict'):
                params['problem_level_1'] = self.problem_level_1.to_alipay_dict()
            else:
                params['problem_level_1'] = self.problem_level_1
        if self.problem_level_2:
            if hasattr(self.problem_level_2, 'to_alipay_dict'):
                params['problem_level_2'] = self.problem_level_2.to_alipay_dict()
            else:
                params['problem_level_2'] = self.problem_level_2
        if self.problem_level_3:
            if hasattr(self.problem_level_3, 'to_alipay_dict'):
                params['problem_level_3'] = self.problem_level_3.to_alipay_dict()
            else:
                params['problem_level_3'] = self.problem_level_3
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FixProblemDTO()
        if 'id' in d:
            o.id = d['id']
        if 'problem_level_1' in d:
            o.problem_level_1 = d['problem_level_1']
        if 'problem_level_2' in d:
            o.problem_level_2 = d['problem_level_2']
        if 'problem_level_3' in d:
            o.problem_level_3 = d['problem_level_3']
        return o


