#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsultActivityResultInfo(object):

    def __init__(self):
        self._activity_id = None
        self._consult_result_code = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def consult_result_code(self):
        return self._consult_result_code

    @consult_result_code.setter
    def consult_result_code(self, value):
        self._consult_result_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.consult_result_code:
            if hasattr(self.consult_result_code, 'to_alipay_dict'):
                params['consult_result_code'] = self.consult_result_code.to_alipay_dict()
            else:
                params['consult_result_code'] = self.consult_result_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsultActivityResultInfo()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'consult_result_code' in d:
            o.consult_result_code = d['consult_result_code']
        return o


