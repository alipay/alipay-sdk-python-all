#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AuthExtendParams(object):

    def __init__(self):
        self._patient_cert_no = None
        self._patient_cert_type = None
        self._patient_name = None
        self._sys_service_provider_id = None

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
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    def patient_name(self, value):
        self._patient_name = value
    @property
    def sys_service_provider_id(self):
        return self._sys_service_provider_id

    @sys_service_provider_id.setter
    def sys_service_provider_id(self, value):
        self._sys_service_provider_id = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.patient_name:
            if hasattr(self.patient_name, 'to_alipay_dict'):
                params['patient_name'] = self.patient_name.to_alipay_dict()
            else:
                params['patient_name'] = self.patient_name
        if self.sys_service_provider_id:
            if hasattr(self.sys_service_provider_id, 'to_alipay_dict'):
                params['sys_service_provider_id'] = self.sys_service_provider_id.to_alipay_dict()
            else:
                params['sys_service_provider_id'] = self.sys_service_provider_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthExtendParams()
        if 'patient_cert_no' in d:
            o.patient_cert_no = d['patient_cert_no']
        if 'patient_cert_type' in d:
            o.patient_cert_type = d['patient_cert_type']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'sys_service_provider_id' in d:
            o.sys_service_provider_id = d['sys_service_provider_id']
        return o


