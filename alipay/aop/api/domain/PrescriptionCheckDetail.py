#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Diagnosis import Diagnosis


class PrescriptionCheckDetail(object):

    def __init__(self):
        self._check_code = None
        self._check_content = None
        self._check_title = None
        self._recommended_diagnosis_list = None
        self._solve_level = None

    @property
    def check_code(self):
        return self._check_code

    @check_code.setter
    def check_code(self, value):
        self._check_code = value
    @property
    def check_content(self):
        return self._check_content

    @check_content.setter
    def check_content(self, value):
        self._check_content = value
    @property
    def check_title(self):
        return self._check_title

    @check_title.setter
    def check_title(self, value):
        self._check_title = value
    @property
    def recommended_diagnosis_list(self):
        return self._recommended_diagnosis_list

    @recommended_diagnosis_list.setter
    def recommended_diagnosis_list(self, value):
        if isinstance(value, list):
            self._recommended_diagnosis_list = list()
            for i in value:
                if isinstance(i, Diagnosis):
                    self._recommended_diagnosis_list.append(i)
                else:
                    self._recommended_diagnosis_list.append(Diagnosis.from_alipay_dict(i))
    @property
    def solve_level(self):
        return self._solve_level

    @solve_level.setter
    def solve_level(self, value):
        self._solve_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_code:
            if hasattr(self.check_code, 'to_alipay_dict'):
                params['check_code'] = self.check_code.to_alipay_dict()
            else:
                params['check_code'] = self.check_code
        if self.check_content:
            if hasattr(self.check_content, 'to_alipay_dict'):
                params['check_content'] = self.check_content.to_alipay_dict()
            else:
                params['check_content'] = self.check_content
        if self.check_title:
            if hasattr(self.check_title, 'to_alipay_dict'):
                params['check_title'] = self.check_title.to_alipay_dict()
            else:
                params['check_title'] = self.check_title
        if self.recommended_diagnosis_list:
            if isinstance(self.recommended_diagnosis_list, list):
                for i in range(0, len(self.recommended_diagnosis_list)):
                    element = self.recommended_diagnosis_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.recommended_diagnosis_list[i] = element.to_alipay_dict()
            if hasattr(self.recommended_diagnosis_list, 'to_alipay_dict'):
                params['recommended_diagnosis_list'] = self.recommended_diagnosis_list.to_alipay_dict()
            else:
                params['recommended_diagnosis_list'] = self.recommended_diagnosis_list
        if self.solve_level:
            if hasattr(self.solve_level, 'to_alipay_dict'):
                params['solve_level'] = self.solve_level.to_alipay_dict()
            else:
                params['solve_level'] = self.solve_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrescriptionCheckDetail()
        if 'check_code' in d:
            o.check_code = d['check_code']
        if 'check_content' in d:
            o.check_content = d['check_content']
        if 'check_title' in d:
            o.check_title = d['check_title']
        if 'recommended_diagnosis_list' in d:
            o.recommended_diagnosis_list = d['recommended_diagnosis_list']
        if 'solve_level' in d:
            o.solve_level = d['solve_level']
        return o


