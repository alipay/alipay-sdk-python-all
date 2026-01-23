#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsuranceHkmedicalSigninModel(object):

    def __init__(self):
        self._hosp_id = None
        self._qr_code = None

    @property
    def hosp_id(self):
        return self._hosp_id

    @hosp_id.setter
    def hosp_id(self, value):
        self._hosp_id = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.hosp_id:
            if hasattr(self.hosp_id, 'to_alipay_dict'):
                params['hosp_id'] = self.hosp_id.to_alipay_dict()
            else:
                params['hosp_id'] = self.hosp_id
        if self.qr_code:
            if hasattr(self.qr_code, 'to_alipay_dict'):
                params['qr_code'] = self.qr_code.to_alipay_dict()
            else:
                params['qr_code'] = self.qr_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceHkmedicalSigninModel()
        if 'hosp_id' in d:
            o.hosp_id = d['hosp_id']
        if 'qr_code' in d:
            o.qr_code = d['qr_code']
        return o


