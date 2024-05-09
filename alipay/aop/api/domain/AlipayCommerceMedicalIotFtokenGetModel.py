#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalIotFtokenGetModel(object):

    def __init__(self):
        self._medical_code = None

    @property
    def medical_code(self):
        return self._medical_code

    @medical_code.setter
    def medical_code(self, value):
        self._medical_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.medical_code:
            if hasattr(self.medical_code, 'to_alipay_dict'):
                params['medical_code'] = self.medical_code.to_alipay_dict()
            else:
                params['medical_code'] = self.medical_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIotFtokenGetModel()
        if 'medical_code' in d:
            o.medical_code = d['medical_code']
        return o


