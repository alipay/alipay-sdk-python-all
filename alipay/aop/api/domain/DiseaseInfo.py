#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DiseaseInfo(object):

    def __init__(self):
        self._disease_code_icd_10 = None
        self._disease_name = None
        self._ext_disease_code = None

    @property
    def disease_code_icd_10(self):
        return self._disease_code_icd_10

    @disease_code_icd_10.setter
    def disease_code_icd_10(self, value):
        self._disease_code_icd_10 = value
    @property
    def disease_name(self):
        return self._disease_name

    @disease_name.setter
    def disease_name(self, value):
        self._disease_name = value
    @property
    def ext_disease_code(self):
        return self._ext_disease_code

    @ext_disease_code.setter
    def ext_disease_code(self, value):
        self._ext_disease_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.disease_code_icd_10:
            if hasattr(self.disease_code_icd_10, 'to_alipay_dict'):
                params['disease_code_icd_10'] = self.disease_code_icd_10.to_alipay_dict()
            else:
                params['disease_code_icd_10'] = self.disease_code_icd_10
        if self.disease_name:
            if hasattr(self.disease_name, 'to_alipay_dict'):
                params['disease_name'] = self.disease_name.to_alipay_dict()
            else:
                params['disease_name'] = self.disease_name
        if self.ext_disease_code:
            if hasattr(self.ext_disease_code, 'to_alipay_dict'):
                params['ext_disease_code'] = self.ext_disease_code.to_alipay_dict()
            else:
                params['ext_disease_code'] = self.ext_disease_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiseaseInfo()
        if 'disease_code_icd_10' in d:
            o.disease_code_icd_10 = d['disease_code_icd_10']
        if 'disease_name' in d:
            o.disease_name = d['disease_name']
        if 'ext_disease_code' in d:
            o.ext_disease_code = d['ext_disease_code']
        return o


