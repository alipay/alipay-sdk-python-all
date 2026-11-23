#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RegisterPatientDetailInfo(object):

    def __init__(self):
        self._age_unit = None
        self._birth_date = None
        self._card_no = None
        self._card_type = None
        self._city = None
        self._detail_address = None
        self._has_complete = None
        self._patient_age = None
        self._patient_cert_status = None
        self._patient_gender = None
        self._patient_gender_desc = None
        self._patient_id = None
        self._patient_name = None
        self._patient_relation = None
        self._phone = None
        self._province = None
        self._region = None

    @property
    def age_unit(self):
        return self._age_unit

    @age_unit.setter
    def age_unit(self, value):
        self._age_unit = value
    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def detail_address(self):
        return self._detail_address

    @detail_address.setter
    def detail_address(self, value):
        self._detail_address = value
    @property
    def has_complete(self):
        return self._has_complete

    @has_complete.setter
    def has_complete(self, value):
        self._has_complete = value
    @property
    def patient_age(self):
        return self._patient_age

    @patient_age.setter
    def patient_age(self, value):
        self._patient_age = value
    @property
    def patient_cert_status(self):
        return self._patient_cert_status

    @patient_cert_status.setter
    def patient_cert_status(self, value):
        self._patient_cert_status = value
    @property
    def patient_gender(self):
        return self._patient_gender

    @patient_gender.setter
    def patient_gender(self, value):
        self._patient_gender = value
    @property
    def patient_gender_desc(self):
        return self._patient_gender_desc

    @patient_gender_desc.setter
    def patient_gender_desc(self, value):
        self._patient_gender_desc = value
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
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value


    def to_alipay_dict(self):
        params = dict()
        if self.age_unit:
            if hasattr(self.age_unit, 'to_alipay_dict'):
                params['age_unit'] = self.age_unit.to_alipay_dict()
            else:
                params['age_unit'] = self.age_unit
        if self.birth_date:
            if hasattr(self.birth_date, 'to_alipay_dict'):
                params['birth_date'] = self.birth_date.to_alipay_dict()
            else:
                params['birth_date'] = self.birth_date
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.detail_address:
            if hasattr(self.detail_address, 'to_alipay_dict'):
                params['detail_address'] = self.detail_address.to_alipay_dict()
            else:
                params['detail_address'] = self.detail_address
        if self.has_complete:
            if hasattr(self.has_complete, 'to_alipay_dict'):
                params['has_complete'] = self.has_complete.to_alipay_dict()
            else:
                params['has_complete'] = self.has_complete
        if self.patient_age:
            if hasattr(self.patient_age, 'to_alipay_dict'):
                params['patient_age'] = self.patient_age.to_alipay_dict()
            else:
                params['patient_age'] = self.patient_age
        if self.patient_cert_status:
            if hasattr(self.patient_cert_status, 'to_alipay_dict'):
                params['patient_cert_status'] = self.patient_cert_status.to_alipay_dict()
            else:
                params['patient_cert_status'] = self.patient_cert_status
        if self.patient_gender:
            if hasattr(self.patient_gender, 'to_alipay_dict'):
                params['patient_gender'] = self.patient_gender.to_alipay_dict()
            else:
                params['patient_gender'] = self.patient_gender
        if self.patient_gender_desc:
            if hasattr(self.patient_gender_desc, 'to_alipay_dict'):
                params['patient_gender_desc'] = self.patient_gender_desc.to_alipay_dict()
            else:
                params['patient_gender_desc'] = self.patient_gender_desc
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
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RegisterPatientDetailInfo()
        if 'age_unit' in d:
            o.age_unit = d['age_unit']
        if 'birth_date' in d:
            o.birth_date = d['birth_date']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'city' in d:
            o.city = d['city']
        if 'detail_address' in d:
            o.detail_address = d['detail_address']
        if 'has_complete' in d:
            o.has_complete = d['has_complete']
        if 'patient_age' in d:
            o.patient_age = d['patient_age']
        if 'patient_cert_status' in d:
            o.patient_cert_status = d['patient_cert_status']
        if 'patient_gender' in d:
            o.patient_gender = d['patient_gender']
        if 'patient_gender_desc' in d:
            o.patient_gender_desc = d['patient_gender_desc']
        if 'patient_id' in d:
            o.patient_id = d['patient_id']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'patient_relation' in d:
            o.patient_relation = d['patient_relation']
        if 'phone' in d:
            o.phone = d['phone']
        if 'province' in d:
            o.province = d['province']
        if 'region' in d:
            o.region = d['region']
        return o


