#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalIndustrydataDoctorcontentdetailQueryModel(object):

    def __init__(self):
        self._merchant_doctor_id = None
        self._platform_code = None

    @property
    def merchant_doctor_id(self):
        return self._merchant_doctor_id

    @merchant_doctor_id.setter
    def merchant_doctor_id(self, value):
        self._merchant_doctor_id = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_doctor_id:
            if hasattr(self.merchant_doctor_id, 'to_alipay_dict'):
                params['merchant_doctor_id'] = self.merchant_doctor_id.to_alipay_dict()
            else:
                params['merchant_doctor_id'] = self.merchant_doctor_id
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataDoctorcontentdetailQueryModel()
        if 'merchant_doctor_id' in d:
            o.merchant_doctor_id = d['merchant_doctor_id']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        return o


