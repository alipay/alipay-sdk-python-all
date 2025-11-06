#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicationInformation(object):

    def __init__(self):
        self._dosage = None
        self._medical_name = None

    @property
    def dosage(self):
        return self._dosage

    @dosage.setter
    def dosage(self, value):
        self._dosage = value
    @property
    def medical_name(self):
        return self._medical_name

    @medical_name.setter
    def medical_name(self, value):
        self._medical_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.dosage:
            if hasattr(self.dosage, 'to_alipay_dict'):
                params['dosage'] = self.dosage.to_alipay_dict()
            else:
                params['dosage'] = self.dosage
        if self.medical_name:
            if hasattr(self.medical_name, 'to_alipay_dict'):
                params['medical_name'] = self.medical_name.to_alipay_dict()
            else:
                params['medical_name'] = self.medical_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicationInformation()
        if 'dosage' in d:
            o.dosage = d['dosage']
        if 'medical_name' in d:
            o.medical_name = d['medical_name']
        return o


