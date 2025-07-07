#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PatientVO(object):

    def __init__(self):
        self._open_id = None
        self._patient_birth = None
        self._patient_gender = None
        self._patient_id = None
        self._patient_name = None
        self._user_id = None

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
    def patient_gender(self):
        return self._patient_gender

    @patient_gender.setter
    def patient_gender(self, value):
        self._patient_gender = value
    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value
    @property
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    def patient_name(self, value):
        self._patient_name = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.patient_gender:
            if hasattr(self.patient_gender, 'to_alipay_dict'):
                params['patient_gender'] = self.patient_gender.to_alipay_dict()
            else:
                params['patient_gender'] = self.patient_gender
        if self.patient_id:
            if hasattr(self.patient_id, 'to_alipay_dict'):
                params['patient_id'] = self.patient_id.to_alipay_dict()
            else:
                params['patient_id'] = self.patient_id
        if self.patient_name:
            if hasattr(self.patient_name, 'to_alipay_dict'):
                params['patient_name'] = self.patient_name.to_alipay_dict()
            else:
                params['patient_name'] = self.patient_name
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
        o = PatientVO()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'patient_birth' in d:
            o.patient_birth = d['patient_birth']
        if 'patient_gender' in d:
            o.patient_gender = d['patient_gender']
        if 'patient_id' in d:
            o.patient_id = d['patient_id']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


