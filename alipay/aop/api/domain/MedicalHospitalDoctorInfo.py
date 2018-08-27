#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalHospitalDoctorInfo(object):

    def __init__(self):
        self._code = None
        self._name = None
        self._sex = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.sex:
            if hasattr(self.sex, 'to_alipay_dict'):
                params['sex'] = self.sex.to_alipay_dict()
            else:
                params['sex'] = self.sex
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalHospitalDoctorInfo()
        if 'code' in d:
            o.code = d['code']
        if 'name' in d:
            o.name = d['name']
        if 'sex' in d:
            o.sex = d['sex']
        return o


