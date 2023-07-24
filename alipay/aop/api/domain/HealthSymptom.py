#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HealthSymptom(object):

    def __init__(self):
        self._symptom_id = None
        self._symptom_name = None

    @property
    def symptom_id(self):
        return self._symptom_id

    @symptom_id.setter
    def symptom_id(self, value):
        self._symptom_id = value
    @property
    def symptom_name(self):
        return self._symptom_name

    @symptom_name.setter
    def symptom_name(self, value):
        self._symptom_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.symptom_id:
            if hasattr(self.symptom_id, 'to_alipay_dict'):
                params['symptom_id'] = self.symptom_id.to_alipay_dict()
            else:
                params['symptom_id'] = self.symptom_id
        if self.symptom_name:
            if hasattr(self.symptom_name, 'to_alipay_dict'):
                params['symptom_name'] = self.symptom_name.to_alipay_dict()
            else:
                params['symptom_name'] = self.symptom_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HealthSymptom()
        if 'symptom_id' in d:
            o.symptom_id = d['symptom_id']
        if 'symptom_name' in d:
            o.symptom_name = d['symptom_name']
        return o


