#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HDFDrugInfo import HDFDrugInfo


class HDFPrescription(object):

    def __init__(self):
        self._check_time = None
        self._create_doctor_id = None
        self._create_doctor_name = None
        self._create_time = None
        self._diagnosis = None
        self._drug_info = None
        self._expire_time = None
        self._faculty_name = None
        self._partner_prescription_id = None
        self._patient_age = None
        self._patient_name = None
        self._patient_sex = None
        self._pharmacist_id = None
        self._pharmacist_name = None
        self._prescription_id = None
        self._prescription_note = None
        self._weight = None

    @property
    def check_time(self):
        return self._check_time

    @check_time.setter
    def check_time(self, value):
        self._check_time = value
    @property
    def create_doctor_id(self):
        return self._create_doctor_id

    @create_doctor_id.setter
    def create_doctor_id(self, value):
        self._create_doctor_id = value
    @property
    def create_doctor_name(self):
        return self._create_doctor_name

    @create_doctor_name.setter
    def create_doctor_name(self, value):
        self._create_doctor_name = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        self._diagnosis = value
    @property
    def drug_info(self):
        return self._drug_info

    @drug_info.setter
    def drug_info(self, value):
        if isinstance(value, list):
            self._drug_info = list()
            for i in value:
                if isinstance(i, HDFDrugInfo):
                    self._drug_info.append(i)
                else:
                    self._drug_info.append(HDFDrugInfo.from_alipay_dict(i))
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def faculty_name(self):
        return self._faculty_name

    @faculty_name.setter
    def faculty_name(self, value):
        self._faculty_name = value
    @property
    def partner_prescription_id(self):
        return self._partner_prescription_id

    @partner_prescription_id.setter
    def partner_prescription_id(self, value):
        self._partner_prescription_id = value
    @property
    def patient_age(self):
        return self._patient_age

    @patient_age.setter
    def patient_age(self, value):
        self._patient_age = value
    @property
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    def patient_name(self, value):
        self._patient_name = value
    @property
    def patient_sex(self):
        return self._patient_sex

    @patient_sex.setter
    def patient_sex(self, value):
        self._patient_sex = value
    @property
    def pharmacist_id(self):
        return self._pharmacist_id

    @pharmacist_id.setter
    def pharmacist_id(self, value):
        self._pharmacist_id = value
    @property
    def pharmacist_name(self):
        return self._pharmacist_name

    @pharmacist_name.setter
    def pharmacist_name(self, value):
        self._pharmacist_name = value
    @property
    def prescription_id(self):
        return self._prescription_id

    @prescription_id.setter
    def prescription_id(self, value):
        self._prescription_id = value
    @property
    def prescription_note(self):
        return self._prescription_note

    @prescription_note.setter
    def prescription_note(self, value):
        self._prescription_note = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_time:
            if hasattr(self.check_time, 'to_alipay_dict'):
                params['check_time'] = self.check_time.to_alipay_dict()
            else:
                params['check_time'] = self.check_time
        if self.create_doctor_id:
            if hasattr(self.create_doctor_id, 'to_alipay_dict'):
                params['create_doctor_id'] = self.create_doctor_id.to_alipay_dict()
            else:
                params['create_doctor_id'] = self.create_doctor_id
        if self.create_doctor_name:
            if hasattr(self.create_doctor_name, 'to_alipay_dict'):
                params['create_doctor_name'] = self.create_doctor_name.to_alipay_dict()
            else:
                params['create_doctor_name'] = self.create_doctor_name
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.diagnosis:
            if hasattr(self.diagnosis, 'to_alipay_dict'):
                params['diagnosis'] = self.diagnosis.to_alipay_dict()
            else:
                params['diagnosis'] = self.diagnosis
        if self.drug_info:
            if isinstance(self.drug_info, list):
                for i in range(0, len(self.drug_info)):
                    element = self.drug_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.drug_info[i] = element.to_alipay_dict()
            if hasattr(self.drug_info, 'to_alipay_dict'):
                params['drug_info'] = self.drug_info.to_alipay_dict()
            else:
                params['drug_info'] = self.drug_info
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.faculty_name:
            if hasattr(self.faculty_name, 'to_alipay_dict'):
                params['faculty_name'] = self.faculty_name.to_alipay_dict()
            else:
                params['faculty_name'] = self.faculty_name
        if self.partner_prescription_id:
            if hasattr(self.partner_prescription_id, 'to_alipay_dict'):
                params['partner_prescription_id'] = self.partner_prescription_id.to_alipay_dict()
            else:
                params['partner_prescription_id'] = self.partner_prescription_id
        if self.patient_age:
            if hasattr(self.patient_age, 'to_alipay_dict'):
                params['patient_age'] = self.patient_age.to_alipay_dict()
            else:
                params['patient_age'] = self.patient_age
        if self.patient_name:
            if hasattr(self.patient_name, 'to_alipay_dict'):
                params['patient_name'] = self.patient_name.to_alipay_dict()
            else:
                params['patient_name'] = self.patient_name
        if self.patient_sex:
            if hasattr(self.patient_sex, 'to_alipay_dict'):
                params['patient_sex'] = self.patient_sex.to_alipay_dict()
            else:
                params['patient_sex'] = self.patient_sex
        if self.pharmacist_id:
            if hasattr(self.pharmacist_id, 'to_alipay_dict'):
                params['pharmacist_id'] = self.pharmacist_id.to_alipay_dict()
            else:
                params['pharmacist_id'] = self.pharmacist_id
        if self.pharmacist_name:
            if hasattr(self.pharmacist_name, 'to_alipay_dict'):
                params['pharmacist_name'] = self.pharmacist_name.to_alipay_dict()
            else:
                params['pharmacist_name'] = self.pharmacist_name
        if self.prescription_id:
            if hasattr(self.prescription_id, 'to_alipay_dict'):
                params['prescription_id'] = self.prescription_id.to_alipay_dict()
            else:
                params['prescription_id'] = self.prescription_id
        if self.prescription_note:
            if hasattr(self.prescription_note, 'to_alipay_dict'):
                params['prescription_note'] = self.prescription_note.to_alipay_dict()
            else:
                params['prescription_note'] = self.prescription_note
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
        o = HDFPrescription()
        if 'check_time' in d:
            o.check_time = d['check_time']
        if 'create_doctor_id' in d:
            o.create_doctor_id = d['create_doctor_id']
        if 'create_doctor_name' in d:
            o.create_doctor_name = d['create_doctor_name']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'diagnosis' in d:
            o.diagnosis = d['diagnosis']
        if 'drug_info' in d:
            o.drug_info = d['drug_info']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'faculty_name' in d:
            o.faculty_name = d['faculty_name']
        if 'partner_prescription_id' in d:
            o.partner_prescription_id = d['partner_prescription_id']
        if 'patient_age' in d:
            o.patient_age = d['patient_age']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'patient_sex' in d:
            o.patient_sex = d['patient_sex']
        if 'pharmacist_id' in d:
            o.pharmacist_id = d['pharmacist_id']
        if 'pharmacist_name' in d:
            o.pharmacist_name = d['pharmacist_name']
        if 'prescription_id' in d:
            o.prescription_id = d['prescription_id']
        if 'prescription_note' in d:
            o.prescription_note = d['prescription_note']
        if 'weight' in d:
            o.weight = d['weight']
        return o


