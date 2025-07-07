#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalMedagentPatientQueryModel(object):

    def __init__(self):
        self._channel_id = None
        self._doctor_id = None
        self._open_id = None
        self._patient_birth = None
        self._patient_cert_no = None
        self._patient_cert_type = None
        self._patient_gender = None
        self._patient_name = None
        self._patient_role = None
        self._user_id = None

    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def patient_birth(self):
        return self._patient_birth

    @patient_birth.setter
    def patient_birth(self, value):
        self._patient_birth = value
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
    def patient_gender(self):
        return self._patient_gender

    @patient_gender.setter
    def patient_gender(self, value):
        self._patient_gender = value
    @property
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    def patient_name(self, value):
        self._patient_name = value
    @property
    def patient_role(self):
        return self._patient_role

    @patient_role.setter
    def patient_role(self, value):
        self._patient_role = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.patient_birth:
            if hasattr(self.patient_birth, 'to_alipay_dict'):
                params['patient_birth'] = self.patient_birth.to_alipay_dict()
            else:
                params['patient_birth'] = self.patient_birth
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
        if self.patient_gender:
            if hasattr(self.patient_gender, 'to_alipay_dict'):
                params['patient_gender'] = self.patient_gender.to_alipay_dict()
            else:
                params['patient_gender'] = self.patient_gender
        if self.patient_name:
            if hasattr(self.patient_name, 'to_alipay_dict'):
                params['patient_name'] = self.patient_name.to_alipay_dict()
            else:
                params['patient_name'] = self.patient_name
        if self.patient_role:
            if hasattr(self.patient_role, 'to_alipay_dict'):
                params['patient_role'] = self.patient_role.to_alipay_dict()
            else:
                params['patient_role'] = self.patient_role
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMedagentPatientQueryModel()
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'patient_birth' in d:
            o.patient_birth = d['patient_birth']
        if 'patient_cert_no' in d:
            o.patient_cert_no = d['patient_cert_no']
        if 'patient_cert_type' in d:
            o.patient_cert_type = d['patient_cert_type']
        if 'patient_gender' in d:
            o.patient_gender = d['patient_gender']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'patient_role' in d:
            o.patient_role = d['patient_role']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


