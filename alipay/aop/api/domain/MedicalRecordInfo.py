#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalRecordInfo(object):

    def __init__(self):
        self._allergy = None
        self._condition_desc = None
        self._disease = None
        self._gestation = None
        self._height = None
        self._hope_help = None
        self._hospital = None
        self._illness_history = None
        self._medicine_condition = None
        self._patient_course_time = None
        self._weight = None

    @property
    def allergy(self):
        return self._allergy

    @allergy.setter
    def allergy(self, value):
        self._allergy = value
    @property
    def condition_desc(self):
        return self._condition_desc

    @condition_desc.setter
    def condition_desc(self, value):
        self._condition_desc = value
    @property
    def disease(self):
        return self._disease

    @disease.setter
    def disease(self, value):
        self._disease = value
    @property
    def gestation(self):
        return self._gestation

    @gestation.setter
    def gestation(self, value):
        self._gestation = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def hope_help(self):
        return self._hope_help

    @hope_help.setter
    def hope_help(self, value):
        self._hope_help = value
    @property
    def hospital(self):
        return self._hospital

    @hospital.setter
    def hospital(self, value):
        self._hospital = value
    @property
    def illness_history(self):
        return self._illness_history

    @illness_history.setter
    def illness_history(self, value):
        self._illness_history = value
    @property
    def medicine_condition(self):
        return self._medicine_condition

    @medicine_condition.setter
    def medicine_condition(self, value):
        self._medicine_condition = value
    @property
    def patient_course_time(self):
        return self._patient_course_time

    @patient_course_time.setter
    def patient_course_time(self, value):
        self._patient_course_time = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


    def to_alipay_dict(self):
        params = dict()
        if self.allergy:
            if hasattr(self.allergy, 'to_alipay_dict'):
                params['allergy'] = self.allergy.to_alipay_dict()
            else:
                params['allergy'] = self.allergy
        if self.condition_desc:
            if hasattr(self.condition_desc, 'to_alipay_dict'):
                params['condition_desc'] = self.condition_desc.to_alipay_dict()
            else:
                params['condition_desc'] = self.condition_desc
        if self.disease:
            if hasattr(self.disease, 'to_alipay_dict'):
                params['disease'] = self.disease.to_alipay_dict()
            else:
                params['disease'] = self.disease
        if self.gestation:
            if hasattr(self.gestation, 'to_alipay_dict'):
                params['gestation'] = self.gestation.to_alipay_dict()
            else:
                params['gestation'] = self.gestation
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.hope_help:
            if hasattr(self.hope_help, 'to_alipay_dict'):
                params['hope_help'] = self.hope_help.to_alipay_dict()
            else:
                params['hope_help'] = self.hope_help
        if self.hospital:
            if hasattr(self.hospital, 'to_alipay_dict'):
                params['hospital'] = self.hospital.to_alipay_dict()
            else:
                params['hospital'] = self.hospital
        if self.illness_history:
            if hasattr(self.illness_history, 'to_alipay_dict'):
                params['illness_history'] = self.illness_history.to_alipay_dict()
            else:
                params['illness_history'] = self.illness_history
        if self.medicine_condition:
            if hasattr(self.medicine_condition, 'to_alipay_dict'):
                params['medicine_condition'] = self.medicine_condition.to_alipay_dict()
            else:
                params['medicine_condition'] = self.medicine_condition
        if self.patient_course_time:
            if hasattr(self.patient_course_time, 'to_alipay_dict'):
                params['patient_course_time'] = self.patient_course_time.to_alipay_dict()
            else:
                params['patient_course_time'] = self.patient_course_time
        if self.weight:
            if hasattr(self.weight, 'to_alipay_dict'):
                params['weight'] = self.weight.to_alipay_dict()
            else:
                params['weight'] = self.weight
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalRecordInfo()
        if 'allergy' in d:
            o.allergy = d['allergy']
        if 'condition_desc' in d:
            o.condition_desc = d['condition_desc']
        if 'disease' in d:
            o.disease = d['disease']
        if 'gestation' in d:
            o.gestation = d['gestation']
        if 'height' in d:
            o.height = d['height']
        if 'hope_help' in d:
            o.hope_help = d['hope_help']
        if 'hospital' in d:
            o.hospital = d['hospital']
        if 'illness_history' in d:
            o.illness_history = d['illness_history']
        if 'medicine_condition' in d:
            o.medicine_condition = d['medicine_condition']
        if 'patient_course_time' in d:
            o.patient_course_time = d['patient_course_time']
        if 'weight' in d:
            o.weight = d['weight']
        return o


