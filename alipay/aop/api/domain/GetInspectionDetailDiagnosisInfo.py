#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GetInspectionDetailDiagnosisInfo(object):

    def __init__(self):
        self._diacrisis_icd_code = None
        self._diagnosis = None

    @property
    def diacrisis_icd_code(self):
        return self._diacrisis_icd_code

    @diacrisis_icd_code.setter
    def diacrisis_icd_code(self, value):
        self._diacrisis_icd_code = value
    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        self._diagnosis = value


    def to_alipay_dict(self):
        params = dict()
        if self.diacrisis_icd_code:
            if hasattr(self.diacrisis_icd_code, 'to_alipay_dict'):
                params['diacrisis_icd_code'] = self.diacrisis_icd_code.to_alipay_dict()
            else:
                params['diacrisis_icd_code'] = self.diacrisis_icd_code
        if self.diagnosis:
            if hasattr(self.diagnosis, 'to_alipay_dict'):
                params['diagnosis'] = self.diagnosis.to_alipay_dict()
            else:
                params['diagnosis'] = self.diagnosis
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GetInspectionDetailDiagnosisInfo()
        if 'diacrisis_icd_code' in d:
            o.diacrisis_icd_code = d['diacrisis_icd_code']
        if 'diagnosis' in d:
            o.diagnosis = d['diagnosis']
        return o


