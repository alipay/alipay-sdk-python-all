#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PatientInfoForFulfillmentList(object):

    def __init__(self):
        self._age = None
        self._birth_day = None
        self._cert_type = None
        self._gender = None
        self._id_card = None
        self._name = None
        self._patient_id = None
        self._phone = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def birth_day(self):
        return self._birth_day

    @birth_day.setter
    def birth_day(self, value):
        self._birth_day = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def id_card(self):
        return self._id_card

    @id_card.setter
    def id_card(self, value):
        self._id_card = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value
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
        if self.birth_day:
            if hasattr(self.birth_day, 'to_alipay_dict'):
                params['birth_day'] = self.birth_day.to_alipay_dict()
            else:
                params['birth_day'] = self.birth_day
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.id_card:
            if hasattr(self.id_card, 'to_alipay_dict'):
                params['id_card'] = self.id_card.to_alipay_dict()
            else:
                params['id_card'] = self.id_card
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.patient_id:
            if hasattr(self.patient_id, 'to_alipay_dict'):
                params['patient_id'] = self.patient_id.to_alipay_dict()
            else:
                params['patient_id'] = self.patient_id
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
        o = PatientInfoForFulfillmentList()
        if 'age' in d:
            o.age = d['age']
        if 'birth_day' in d:
            o.birth_day = d['birth_day']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'gender' in d:
            o.gender = d['gender']
        if 'id_card' in d:
            o.id_card = d['id_card']
        if 'name' in d:
            o.name = d['name']
        if 'patient_id' in d:
            o.patient_id = d['patient_id']
        if 'phone' in d:
            o.phone = d['phone']
        return o


