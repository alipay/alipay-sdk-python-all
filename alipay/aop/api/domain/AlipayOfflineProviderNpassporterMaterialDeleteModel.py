#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderNpassporterMaterialDeleteModel(object):

    def __init__(self):
        self._activity_code = None
        self._coil_no_list = None
        self._solution_code = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def coil_no_list(self):
        return self._coil_no_list

    @coil_no_list.setter
    def coil_no_list(self, value):
        if isinstance(value, list):
            self._coil_no_list = list()
            for i in value:
                self._coil_no_list.append(i)
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.coil_no_list:
            if isinstance(self.coil_no_list, list):
                for i in range(0, len(self.coil_no_list)):
                    element = self.coil_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.coil_no_list[i] = element.to_alipay_dict()
            if hasattr(self.coil_no_list, 'to_alipay_dict'):
                params['coil_no_list'] = self.coil_no_list.to_alipay_dict()
            else:
                params['coil_no_list'] = self.coil_no_list
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
        o = AlipayOfflineProviderNpassporterMaterialDeleteModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'coil_no_list' in d:
            o.coil_no_list = d['coil_no_list']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        return o


