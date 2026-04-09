#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemProjectList(object):

    def __init__(self):
        self._check_result = None
        self._indicators_range = None
        self._indicators_unit = None
        self._project_code = None
        self._project_name = None

    @property
    def check_result(self):
        return self._check_result

    @check_result.setter
    def check_result(self, value):
        self._check_result = value
    @property
    def indicators_range(self):
        return self._indicators_range

    @indicators_range.setter
    def indicators_range(self, value):
        self._indicators_range = value
    @property
    def indicators_unit(self):
        return self._indicators_unit

    @indicators_unit.setter
    def indicators_unit(self, value):
        self._indicators_unit = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.check_result:
            if hasattr(self.check_result, 'to_alipay_dict'):
                params['check_result'] = self.check_result.to_alipay_dict()
            else:
                params['check_result'] = self.check_result
        if self.indicators_range:
            if hasattr(self.indicators_range, 'to_alipay_dict'):
                params['indicators_range'] = self.indicators_range.to_alipay_dict()
            else:
                params['indicators_range'] = self.indicators_range
        if self.indicators_unit:
            if hasattr(self.indicators_unit, 'to_alipay_dict'):
                params['indicators_unit'] = self.indicators_unit.to_alipay_dict()
            else:
                params['indicators_unit'] = self.indicators_unit
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemProjectList()
        if 'check_result' in d:
            o.check_result = d['check_result']
        if 'indicators_range' in d:
            o.indicators_range = d['indicators_range']
        if 'indicators_unit' in d:
            o.indicators_unit = d['indicators_unit']
        if 'project_code' in d:
            o.project_code = d['project_code']
        if 'project_name' in d:
            o.project_name = d['project_name']
        return o


