#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalPaymentCodeGetModel(object):

    def __init__(self):
        self._medical_code = None
        self._org_no = None

    @property
    def medical_code(self):
        return self._medical_code

    @medical_code.setter
    def medical_code(self, value):
        self._medical_code = value
    @property
    def org_no(self):
        return self._org_no

    @org_no.setter
    def org_no(self, value):
        self._org_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.medical_code:
            if hasattr(self.medical_code, 'to_alipay_dict'):
                params['medical_code'] = self.medical_code.to_alipay_dict()
            else:
                params['medical_code'] = self.medical_code
        if self.org_no:
            if hasattr(self.org_no, 'to_alipay_dict'):
                params['org_no'] = self.org_no.to_alipay_dict()
            else:
                params['org_no'] = self.org_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalPaymentCodeGetModel()
        if 'medical_code' in d:
            o.medical_code = d['medical_code']
        if 'org_no' in d:
            o.org_no = d['org_no']
        return o


