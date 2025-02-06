#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalPaymentCodeGetModel(object):

    def __init__(self):
        self._medical_code = None
        self._org_no = None
        self._out_request_no = None

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
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value


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
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
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
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        return o


