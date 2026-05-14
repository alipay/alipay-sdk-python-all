#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FulfillmentPatientInfo(object):

    def __init__(self):
        self._age = None
        self._disease_desc = None
        self._gender = None
        self._id_card_no = None
        self._id_card_type = None
        self._mindful_male_flag = None
        self._patient_name = None
        self._patient_relation = None
        self._phone = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def disease_desc(self):
        return self._disease_desc

    @disease_desc.setter
    def disease_desc(self, value):
        self._disease_desc = value
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
    def mindful_male_flag(self):
        return self._mindful_male_flag

    @mindful_male_flag.setter
    def mindful_male_flag(self, value):
        self._mindful_male_flag = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.disease_desc:
            if hasattr(self.disease_desc, 'to_alipay_dict'):
                params['disease_desc'] = self.disease_desc.to_alipay_dict()
            else:
                params['disease_desc'] = self.disease_desc
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
        if self.mindful_male_flag:
            if hasattr(self.mindful_male_flag, 'to_alipay_dict'):
                params['mindful_male_flag'] = self.mindful_male_flag.to_alipay_dict()
            else:
                params['mindful_male_flag'] = self.mindful_male_flag
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FulfillmentPatientInfo()
        if 'age' in d:
            o.age = d['age']
        if 'disease_desc' in d:
            o.disease_desc = d['disease_desc']
        if 'gender' in d:
            o.gender = d['gender']
        if 'id_card_no' in d:
            o.id_card_no = d['id_card_no']
        if 'id_card_type' in d:
            o.id_card_type = d['id_card_type']
        if 'mindful_male_flag' in d:
            o.mindful_male_flag = d['mindful_male_flag']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'patient_relation' in d:
            o.patient_relation = d['patient_relation']
        if 'phone' in d:
            o.phone = d['phone']
        return o


