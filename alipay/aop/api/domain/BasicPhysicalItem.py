#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BasicPhysicalItem(object):

    def __init__(self):
        self._abnormal_type = None
        self._project_code = None
        self._project_name = None
        self._range = None
        self._result = None
        self._unit = None

    @property
    def abnormal_type(self):
        return self._abnormal_type

    @abnormal_type.setter
    def abnormal_type(self, value):
        self._abnormal_type = value
    @property
    def project_code(self):
        return self._project_code

    @project_code.setter
    def project_code(self, value):
        self._project_code = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value
    @property
    def range(self):
        return self._range

    @range.setter
    def range(self, value):
        self._range = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.abnormal_type:
            if hasattr(self.abnormal_type, 'to_alipay_dict'):
                params['abnormal_type'] = self.abnormal_type.to_alipay_dict()
            else:
                params['abnormal_type'] = self.abnormal_type
        if self.project_code:
            if hasattr(self.project_code, 'to_alipay_dict'):
                params['project_code'] = self.project_code.to_alipay_dict()
            else:
                params['project_code'] = self.project_code
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        if self.range:
            if hasattr(self.range, 'to_alipay_dict'):
                params['range'] = self.range.to_alipay_dict()
            else:
                params['range'] = self.range
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BasicPhysicalItem()
        if 'abnormal_type' in d:
            o.abnormal_type = d['abnormal_type']
        if 'project_code' in d:
            o.project_code = d['project_code']
        if 'project_name' in d:
            o.project_name = d['project_name']
        if 'range' in d:
            o.range = d['range']
        if 'result' in d:
            o.result = d['result']
        if 'unit' in d:
            o.unit = d['unit']
        return o


