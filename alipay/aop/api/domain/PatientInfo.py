#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PatientInfo(object):

    def __init__(self):
        self._allergy_history = None
        self._family_medical_history = None
        self._kidney_function = None
        self._lactation_status = None
        self._liver_function = None
        self._medical_history = None
        self._past_history = None
        self._patient_age = None
        self._patient_age_unit = None
        self._patient_birthday = None
        self._patient_gender = None
        self._patient_id = None
        self._patient_name = None
        self._pregnancy_status = None
        self._preparation_status = None
        self._weight = None

    @property
    def allergy_history(self):
        return self._allergy_history

    @allergy_history.setter
    def allergy_history(self, value):
        self._allergy_history = value
    @property
    def family_medical_history(self):
        return self._family_medical_history

    @family_medical_history.setter
    def family_medical_history(self, value):
        self._family_medical_history = value
    @property
    def kidney_function(self):
        return self._kidney_function

    @kidney_function.setter
    def kidney_function(self, value):
        self._kidney_function = value
    @property
    def lactation_status(self):
        return self._lactation_status

    @lactation_status.setter
    def lactation_status(self, value):
        self._lactation_status = value
    @property
    def liver_function(self):
        return self._liver_function

    @liver_function.setter
    def liver_function(self, value):
        self._liver_function = value
    @property
    def medical_history(self):
        return self._medical_history

    @medical_history.setter
    def medical_history(self, value):
        self._medical_history = value
    @property
    def past_history(self):
        return self._past_history

    @past_history.setter
    def past_history(self, value):
        self._past_history = value
    @property
    def patient_age(self):
        return self._patient_age

    @patient_age.setter
    def patient_age(self, value):
        self._patient_age = value
    @property
    def patient_age_unit(self):
        return self._patient_age_unit

    @patient_age_unit.setter
    def patient_age_unit(self, value):
        self._patient_age_unit = value
    @property
    def patient_birthday(self):
        return self._patient_birthday

    @patient_birthday.setter
    def patient_birthday(self, value):
        self._patient_birthday = value
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
    def pregnancy_status(self):
        return self._pregnancy_status

    @pregnancy_status.setter
    def pregnancy_status(self, value):
        self._pregnancy_status = value
    @property
    def preparation_status(self):
        return self._preparation_status

    @preparation_status.setter
    def preparation_status(self, value):
        self._preparation_status = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


    def to_alipay_dict(self):
        params = dict()
        if self.allergy_history:
            if hasattr(self.allergy_history, 'to_alipay_dict'):
                params['allergy_history'] = self.allergy_history.to_alipay_dict()
            else:
                params['allergy_history'] = self.allergy_history
        if self.family_medical_history:
            if hasattr(self.family_medical_history, 'to_alipay_dict'):
                params['family_medical_history'] = self.family_medical_history.to_alipay_dict()
            else:
                params['family_medical_history'] = self.family_medical_history
        if self.kidney_function:
            if hasattr(self.kidney_function, 'to_alipay_dict'):
                params['kidney_function'] = self.kidney_function.to_alipay_dict()
            else:
                params['kidney_function'] = self.kidney_function
        if self.lactation_status:
            if hasattr(self.lactation_status, 'to_alipay_dict'):
                params['lactation_status'] = self.lactation_status.to_alipay_dict()
            else:
                params['lactation_status'] = self.lactation_status
        if self.liver_function:
            if hasattr(self.liver_function, 'to_alipay_dict'):
                params['liver_function'] = self.liver_function.to_alipay_dict()
            else:
                params['liver_function'] = self.liver_function
        if self.medical_history:
            if hasattr(self.medical_history, 'to_alipay_dict'):
                params['medical_history'] = self.medical_history.to_alipay_dict()
            else:
                params['medical_history'] = self.medical_history
        if self.past_history:
            if hasattr(self.past_history, 'to_alipay_dict'):
                params['past_history'] = self.past_history.to_alipay_dict()
            else:
                params['past_history'] = self.past_history
        if self.patient_age:
            if hasattr(self.patient_age, 'to_alipay_dict'):
                params['patient_age'] = self.patient_age.to_alipay_dict()
            else:
                params['patient_age'] = self.patient_age
        if self.patient_age_unit:
            if hasattr(self.patient_age_unit, 'to_alipay_dict'):
                params['patient_age_unit'] = self.patient_age_unit.to_alipay_dict()
            else:
                params['patient_age_unit'] = self.patient_age_unit
        if self.patient_birthday:
            if hasattr(self.patient_birthday, 'to_alipay_dict'):
                params['patient_birthday'] = self.patient_birthday.to_alipay_dict()
            else:
                params['patient_birthday'] = self.patient_birthday
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
        if self.pregnancy_status:
            if hasattr(self.pregnancy_status, 'to_alipay_dict'):
                params['pregnancy_status'] = self.pregnancy_status.to_alipay_dict()
            else:
                params['pregnancy_status'] = self.pregnancy_status
        if self.preparation_status:
            if hasattr(self.preparation_status, 'to_alipay_dict'):
                params['preparation_status'] = self.preparation_status.to_alipay_dict()
            else:
                params['preparation_status'] = self.preparation_status
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
        o = PatientInfo()
        if 'allergy_history' in d:
            o.allergy_history = d['allergy_history']
        if 'family_medical_history' in d:
            o.family_medical_history = d['family_medical_history']
        if 'kidney_function' in d:
            o.kidney_function = d['kidney_function']
        if 'lactation_status' in d:
            o.lactation_status = d['lactation_status']
        if 'liver_function' in d:
            o.liver_function = d['liver_function']
        if 'medical_history' in d:
            o.medical_history = d['medical_history']
        if 'past_history' in d:
            o.past_history = d['past_history']
        if 'patient_age' in d:
            o.patient_age = d['patient_age']
        if 'patient_age_unit' in d:
            o.patient_age_unit = d['patient_age_unit']
        if 'patient_birthday' in d:
            o.patient_birthday = d['patient_birthday']
        if 'patient_gender' in d:
            o.patient_gender = d['patient_gender']
        if 'patient_id' in d:
            o.patient_id = d['patient_id']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'pregnancy_status' in d:
            o.pregnancy_status = d['pregnancy_status']
        if 'preparation_status' in d:
            o.preparation_status = d['preparation_status']
        if 'weight' in d:
            o.weight = d['weight']
        return o


