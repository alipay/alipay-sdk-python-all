#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFincoreComplianceApccenterAlgorithmarchiveDetectModel(object):

    def __init__(self):
        self._platform_algorithm_code = None
        self._platform_algorithm_last_iteration_code = None
        self._platform_algorithm_source = None

    @property
    def platform_algorithm_code(self):
        return self._platform_algorithm_code

    @platform_algorithm_code.setter
    def platform_algorithm_code(self, value):
        self._platform_algorithm_code = value
    @property
    def platform_algorithm_last_iteration_code(self):
        return self._platform_algorithm_last_iteration_code

    @platform_algorithm_last_iteration_code.setter
    def platform_algorithm_last_iteration_code(self, value):
        self._platform_algorithm_last_iteration_code = value
    @property
    def platform_algorithm_source(self):
        return self._platform_algorithm_source

    @platform_algorithm_source.setter
    def platform_algorithm_source(self, value):
        self._platform_algorithm_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.platform_algorithm_code:
            if hasattr(self.platform_algorithm_code, 'to_alipay_dict'):
                params['platform_algorithm_code'] = self.platform_algorithm_code.to_alipay_dict()
            else:
                params['platform_algorithm_code'] = self.platform_algorithm_code
        if self.platform_algorithm_last_iteration_code:
            if hasattr(self.platform_algorithm_last_iteration_code, 'to_alipay_dict'):
                params['platform_algorithm_last_iteration_code'] = self.platform_algorithm_last_iteration_code.to_alipay_dict()
            else:
                params['platform_algorithm_last_iteration_code'] = self.platform_algorithm_last_iteration_code
        if self.platform_algorithm_source:
            if hasattr(self.platform_algorithm_source, 'to_alipay_dict'):
                params['platform_algorithm_source'] = self.platform_algorithm_source.to_alipay_dict()
            else:
                params['platform_algorithm_source'] = self.platform_algorithm_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceApccenterAlgorithmarchiveDetectModel()
        if 'platform_algorithm_code' in d:
            o.platform_algorithm_code = d['platform_algorithm_code']
        if 'platform_algorithm_last_iteration_code' in d:
            o.platform_algorithm_last_iteration_code = d['platform_algorithm_last_iteration_code']
        if 'platform_algorithm_source' in d:
            o.platform_algorithm_source = d['platform_algorithm_source']
        return o


