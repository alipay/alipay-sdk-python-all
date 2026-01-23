#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderNpassporterVerifyconfigQueryModel(object):

    def __init__(self):
        self._activity_code = None
        self._solution_code = None
        self._verify_config_id = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value
    @property
    def verify_config_id(self):
        return self._verify_config_id

    @verify_config_id.setter
    def verify_config_id(self, value):
        self._verify_config_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        if self.verify_config_id:
            if hasattr(self.verify_config_id, 'to_alipay_dict'):
                params['verify_config_id'] = self.verify_config_id.to_alipay_dict()
            else:
                params['verify_config_id'] = self.verify_config_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderNpassporterVerifyconfigQueryModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        if 'verify_config_id' in d:
            o.verify_config_id = d['verify_config_id']
        return o


