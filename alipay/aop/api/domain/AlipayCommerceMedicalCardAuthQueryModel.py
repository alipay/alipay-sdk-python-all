#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalCardAuthQueryModel(object):

    def __init__(self):
        self._ins_code = None
        self._patient_cert_no = None
        self._patient_cert_type = None
        self._relation_type = None

    @property
    def ins_code(self):
        return self._ins_code

    @ins_code.setter
    def ins_code(self, value):
        self._ins_code = value
    @property
    def patient_cert_no(self):
        return self._patient_cert_no

    @patient_cert_no.setter
    def patient_cert_no(self, value):
        self._patient_cert_no = value
    @property
    def patient_cert_type(self):
        return self._patient_cert_type

    @patient_cert_type.setter
    def patient_cert_type(self, value):
        self._patient_cert_type = value
    @property
    def relation_type(self):
        return self._relation_type

    @relation_type.setter
    def relation_type(self, value):
        self._relation_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.ins_code:
            if hasattr(self.ins_code, 'to_alipay_dict'):
                params['ins_code'] = self.ins_code.to_alipay_dict()
            else:
                params['ins_code'] = self.ins_code
        if self.patient_cert_no:
            if hasattr(self.patient_cert_no, 'to_alipay_dict'):
                params['patient_cert_no'] = self.patient_cert_no.to_alipay_dict()
            else:
                params['patient_cert_no'] = self.patient_cert_no
        if self.patient_cert_type:
            if hasattr(self.patient_cert_type, 'to_alipay_dict'):
                params['patient_cert_type'] = self.patient_cert_type.to_alipay_dict()
            else:
                params['patient_cert_type'] = self.patient_cert_type
        if self.relation_type:
            if hasattr(self.relation_type, 'to_alipay_dict'):
                params['relation_type'] = self.relation_type.to_alipay_dict()
            else:
                params['relation_type'] = self.relation_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalCardAuthQueryModel()
        if 'ins_code' in d:
            o.ins_code = d['ins_code']
        if 'patient_cert_no' in d:
            o.patient_cert_no = d['patient_cert_no']
        if 'patient_cert_type' in d:
            o.patient_cert_type = d['patient_cert_type']
        if 'relation_type' in d:
            o.relation_type = d['relation_type']
        return o


