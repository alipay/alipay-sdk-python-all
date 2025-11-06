#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHomedoctorAgenturlQueryModel(object):

    def __init__(self):
        self._doctor_cert_no = None

    @property
    def doctor_cert_no(self):
        return self._doctor_cert_no

    @doctor_cert_no.setter
    def doctor_cert_no(self, value):
        self._doctor_cert_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_cert_no:
            if hasattr(self.doctor_cert_no, 'to_alipay_dict'):
                params['doctor_cert_no'] = self.doctor_cert_no.to_alipay_dict()
            else:
                params['doctor_cert_no'] = self.doctor_cert_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHomedoctorAgenturlQueryModel()
        if 'doctor_cert_no' in d:
            o.doctor_cert_no = d['doctor_cert_no']
        return o


