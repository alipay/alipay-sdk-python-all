#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HDFIllnessHistory(object):

    def __init__(self):
        self._medical_history_desc = None
        self._medical_history_type = None

    @property
    def medical_history_desc(self):
        return self._medical_history_desc

    @medical_history_desc.setter
    def medical_history_desc(self, value):
        self._medical_history_desc = value
    @property
    def medical_history_type(self):
        return self._medical_history_type

    @medical_history_type.setter
    def medical_history_type(self, value):
        self._medical_history_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.medical_history_desc:
            if hasattr(self.medical_history_desc, 'to_alipay_dict'):
                params['medical_history_desc'] = self.medical_history_desc.to_alipay_dict()
            else:
                params['medical_history_desc'] = self.medical_history_desc
        if self.medical_history_type:
            if hasattr(self.medical_history_type, 'to_alipay_dict'):
                params['medical_history_type'] = self.medical_history_type.to_alipay_dict()
            else:
                params['medical_history_type'] = self.medical_history_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HDFIllnessHistory()
        if 'medical_history_desc' in d:
            o.medical_history_desc = d['medical_history_desc']
        if 'medical_history_type' in d:
            o.medical_history_type = d['medical_history_type']
        return o


