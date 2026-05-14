#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InpatientNursingPatientInfo(object):

    def __init__(self):
        self._age = None
        self._applicant_phone = None
        self._disease_description = None
        self._disease_photo_url_list = None
        self._gender = None
        self._id_card_no = None
        self._id_card_type = None
        self._medical_document_url_list = None
        self._patient_name = None
        self._patient_relation = None
        self._phone = None
        self._special_requirements = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def applicant_phone(self):
        return self._applicant_phone

    @applicant_phone.setter
    def applicant_phone(self, value):
        self._applicant_phone = value
    @property
    def disease_description(self):
        return self._disease_description

    @disease_description.setter
    def disease_description(self, value):
        self._disease_description = value
    @property
    def disease_photo_url_list(self):
        return self._disease_photo_url_list

    @disease_photo_url_list.setter
    def disease_photo_url_list(self, value):
        if isinstance(value, list):
            self._disease_photo_url_list = list()
            for i in value:
                self._disease_photo_url_list.append(i)
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def id_card_no(self):
        return self._id_card_no

    @id_card_no.setter
    def id_card_no(self, value):
        self._id_card_no = value
    @property
    def id_card_type(self):
        return self._id_card_type

    @id_card_type.setter
    def id_card_type(self, value):
        self._id_card_type = value
    @property
    def medical_document_url_list(self):
        return self._medical_document_url_list

    @medical_document_url_list.setter
    def medical_document_url_list(self, value):
        if isinstance(value, list):
            self._medical_document_url_list = list()
            for i in value:
                self._medical_document_url_list.append(i)
    @property
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    def patient_name(self, value):
        self._patient_name = value
    @property
    def patient_relation(self):
        return self._patient_relation

    @patient_relation.setter
    def patient_relation(self, value):
        self._patient_relation = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def special_requirements(self):
        return self._special_requirements

    @special_requirements.setter
    def special_requirements(self, value):
        self._special_requirements = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.applicant_phone:
            if hasattr(self.applicant_phone, 'to_alipay_dict'):
                params['applicant_phone'] = self.applicant_phone.to_alipay_dict()
            else:
                params['applicant_phone'] = self.applicant_phone
        if self.disease_description:
            if hasattr(self.disease_description, 'to_alipay_dict'):
                params['disease_description'] = self.disease_description.to_alipay_dict()
            else:
                params['disease_description'] = self.disease_description
        if self.disease_photo_url_list:
            if isinstance(self.disease_photo_url_list, list):
                for i in range(0, len(self.disease_photo_url_list)):
                    element = self.disease_photo_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.disease_photo_url_list[i] = element.to_alipay_dict()
            if hasattr(self.disease_photo_url_list, 'to_alipay_dict'):
                params['disease_photo_url_list'] = self.disease_photo_url_list.to_alipay_dict()
            else:
                params['disease_photo_url_list'] = self.disease_photo_url_list
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.id_card_no:
            if hasattr(self.id_card_no, 'to_alipay_dict'):
                params['id_card_no'] = self.id_card_no.to_alipay_dict()
            else:
                params['id_card_no'] = self.id_card_no
        if self.id_card_type:
            if hasattr(self.id_card_type, 'to_alipay_dict'):
                params['id_card_type'] = self.id_card_type.to_alipay_dict()
            else:
                params['id_card_type'] = self.id_card_type
        if self.medical_document_url_list:
            if isinstance(self.medical_document_url_list, list):
                for i in range(0, len(self.medical_document_url_list)):
                    element = self.medical_document_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.medical_document_url_list[i] = element.to_alipay_dict()
            if hasattr(self.medical_document_url_list, 'to_alipay_dict'):
                params['medical_document_url_list'] = self.medical_document_url_list.to_alipay_dict()
            else:
                params['medical_document_url_list'] = self.medical_document_url_list
        if self.patient_name:
            if hasattr(self.patient_name, 'to_alipay_dict'):
                params['patient_name'] = self.patient_name.to_alipay_dict()
            else:
                params['patient_name'] = self.patient_name
        if self.patient_relation:
            if hasattr(self.patient_relation, 'to_alipay_dict'):
                params['patient_relation'] = self.patient_relation.to_alipay_dict()
            else:
                params['patient_relation'] = self.patient_relation
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.special_requirements:
            if hasattr(self.special_requirements, 'to_alipay_dict'):
                params['special_requirements'] = self.special_requirements.to_alipay_dict()
            else:
                params['special_requirements'] = self.special_requirements
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InpatientNursingPatientInfo()
        if 'age' in d:
            o.age = d['age']
        if 'applicant_phone' in d:
            o.applicant_phone = d['applicant_phone']
        if 'disease_description' in d:
            o.disease_description = d['disease_description']
        if 'disease_photo_url_list' in d:
            o.disease_photo_url_list = d['disease_photo_url_list']
        if 'gender' in d:
            o.gender = d['gender']
        if 'id_card_no' in d:
            o.id_card_no = d['id_card_no']
        if 'id_card_type' in d:
            o.id_card_type = d['id_card_type']
        if 'medical_document_url_list' in d:
            o.medical_document_url_list = d['medical_document_url_list']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'patient_relation' in d:
            o.patient_relation = d['patient_relation']
        if 'phone' in d:
            o.phone = d['phone']
        if 'special_requirements' in d:
            o.special_requirements = d['special_requirements']
        return o


