#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServicepackagePatientInfo(object):

    def __init__(self):
        self._patient_age = None
        self._patient_disease = None
        self._patient_gender = None
        self._patient_id = None
        self._patient_name = None
        self._patient_pic = None

    @property
    def patient_age(self):
        return self._patient_age

    @patient_age.setter
    def patient_age(self, value):
        self._patient_age = value
    @property
    def patient_disease(self):
        return self._patient_disease

    @patient_disease.setter
    def patient_disease(self, value):
        self._patient_disease = value
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
    def patient_pic(self):
        return self._patient_pic

    @patient_pic.setter
    def patient_pic(self, value):
        if isinstance(value, list):
            self._patient_pic = list()
            for i in value:
                self._patient_pic.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.patient_age:
            if hasattr(self.patient_age, 'to_alipay_dict'):
                params['patient_age'] = self.patient_age.to_alipay_dict()
            else:
                params['patient_age'] = self.patient_age
        if self.patient_disease:
            if hasattr(self.patient_disease, 'to_alipay_dict'):
                params['patient_disease'] = self.patient_disease.to_alipay_dict()
            else:
                params['patient_disease'] = self.patient_disease
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
        if self.patient_pic:
            if isinstance(self.patient_pic, list):
                for i in range(0, len(self.patient_pic)):
                    element = self.patient_pic[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.patient_pic[i] = element.to_alipay_dict()
            if hasattr(self.patient_pic, 'to_alipay_dict'):
                params['patient_pic'] = self.patient_pic.to_alipay_dict()
            else:
                params['patient_pic'] = self.patient_pic
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServicepackagePatientInfo()
        if 'patient_age' in d:
            o.patient_age = d['patient_age']
        if 'patient_disease' in d:
            o.patient_disease = d['patient_disease']
        if 'patient_gender' in d:
            o.patient_gender = d['patient_gender']
        if 'patient_id' in d:
            o.patient_id = d['patient_id']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'patient_pic' in d:
            o.patient_pic = d['patient_pic']
        return o


