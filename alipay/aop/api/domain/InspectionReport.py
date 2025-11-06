#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InspectionReport(object):

    def __init__(self):
        self._age = None
        self._dino = None
        self._gender = None
        self._inspect_project = None
        self._inspect_url = None
        self._report_sub_sub_type = None
        self._report_sub_type = None
        self._result = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def dino(self):
        return self._dino

    @dino.setter
    def dino(self, value):
        self._dino = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def inspect_project(self):
        return self._inspect_project

    @inspect_project.setter
    def inspect_project(self, value):
        self._inspect_project = value
    @property
    def inspect_url(self):
        return self._inspect_url

    @inspect_url.setter
    def inspect_url(self, value):
        self._inspect_url = value
    @property
    def report_sub_sub_type(self):
        return self._report_sub_sub_type

    @report_sub_sub_type.setter
    def report_sub_sub_type(self, value):
        self._report_sub_sub_type = value
    @property
    def report_sub_type(self):
        return self._report_sub_type

    @report_sub_type.setter
    def report_sub_type(self, value):
        self._report_sub_type = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.dino:
            if hasattr(self.dino, 'to_alipay_dict'):
                params['dino'] = self.dino.to_alipay_dict()
            else:
                params['dino'] = self.dino
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.inspect_project:
            if hasattr(self.inspect_project, 'to_alipay_dict'):
                params['inspect_project'] = self.inspect_project.to_alipay_dict()
            else:
                params['inspect_project'] = self.inspect_project
        if self.inspect_url:
            if hasattr(self.inspect_url, 'to_alipay_dict'):
                params['inspect_url'] = self.inspect_url.to_alipay_dict()
            else:
                params['inspect_url'] = self.inspect_url
        if self.report_sub_sub_type:
            if hasattr(self.report_sub_sub_type, 'to_alipay_dict'):
                params['report_sub_sub_type'] = self.report_sub_sub_type.to_alipay_dict()
            else:
                params['report_sub_sub_type'] = self.report_sub_sub_type
        if self.report_sub_type:
            if hasattr(self.report_sub_type, 'to_alipay_dict'):
                params['report_sub_type'] = self.report_sub_type.to_alipay_dict()
            else:
                params['report_sub_type'] = self.report_sub_type
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InspectionReport()
        if 'age' in d:
            o.age = d['age']
        if 'dino' in d:
            o.dino = d['dino']
        if 'gender' in d:
            o.gender = d['gender']
        if 'inspect_project' in d:
            o.inspect_project = d['inspect_project']
        if 'inspect_url' in d:
            o.inspect_url = d['inspect_url']
        if 'report_sub_sub_type' in d:
            o.report_sub_sub_type = d['report_sub_sub_type']
        if 'report_sub_type' in d:
            o.report_sub_type = d['report_sub_type']
        if 'result' in d:
            o.result = d['result']
        return o


