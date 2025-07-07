#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BirthCertificateDTO(object):

    def __init__(self):
        self._birth_gestational_weeks = None
        self._birth_length = None
        self._birth_medical_institution = None
        self._birth_time = None
        self._birth_weight = None
        self._date_issue = None
        self._father_address = None
        self._father_age = None
        self._father_country = None
        self._father_id_card = None
        self._father_name = None
        self._father_nationality = None
        self._full_name = None
        self._mother_address = None
        self._mother_age = None
        self._mother_country = None
        self._mother_id_card = None
        self._mother_name = None
        self._mother_nationality = None
        self._number = None
        self._place_birth = None
        self._sex = None

    @property
    def birth_gestational_weeks(self):
        return self._birth_gestational_weeks

    @birth_gestational_weeks.setter
    def birth_gestational_weeks(self, value):
        self._birth_gestational_weeks = value
    @property
    def birth_length(self):
        return self._birth_length

    @birth_length.setter
    def birth_length(self, value):
        self._birth_length = value
    @property
    def birth_medical_institution(self):
        return self._birth_medical_institution

    @birth_medical_institution.setter
    def birth_medical_institution(self, value):
        self._birth_medical_institution = value
    @property
    def birth_time(self):
        return self._birth_time

    @birth_time.setter
    def birth_time(self, value):
        self._birth_time = value
    @property
    def birth_weight(self):
        return self._birth_weight

    @birth_weight.setter
    def birth_weight(self, value):
        self._birth_weight = value
    @property
    def date_issue(self):
        return self._date_issue

    @date_issue.setter
    def date_issue(self, value):
        self._date_issue = value
    @property
    def father_address(self):
        return self._father_address

    @father_address.setter
    def father_address(self, value):
        self._father_address = value
    @property
    def father_age(self):
        return self._father_age

    @father_age.setter
    def father_age(self, value):
        self._father_age = value
    @property
    def father_country(self):
        return self._father_country

    @father_country.setter
    def father_country(self, value):
        self._father_country = value
    @property
    def father_id_card(self):
        return self._father_id_card

    @father_id_card.setter
    def father_id_card(self, value):
        self._father_id_card = value
    @property
    def father_name(self):
        return self._father_name

    @father_name.setter
    def father_name(self, value):
        self._father_name = value
    @property
    def father_nationality(self):
        return self._father_nationality

    @father_nationality.setter
    def father_nationality(self, value):
        self._father_nationality = value
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value
    @property
    def mother_address(self):
        return self._mother_address

    @mother_address.setter
    def mother_address(self, value):
        self._mother_address = value
    @property
    def mother_age(self):
        return self._mother_age

    @mother_age.setter
    def mother_age(self, value):
        self._mother_age = value
    @property
    def mother_country(self):
        return self._mother_country

    @mother_country.setter
    def mother_country(self, value):
        self._mother_country = value
    @property
    def mother_id_card(self):
        return self._mother_id_card

    @mother_id_card.setter
    def mother_id_card(self, value):
        self._mother_id_card = value
    @property
    def mother_name(self):
        return self._mother_name

    @mother_name.setter
    def mother_name(self, value):
        self._mother_name = value
    @property
    def mother_nationality(self):
        return self._mother_nationality

    @mother_nationality.setter
    def mother_nationality(self, value):
        self._mother_nationality = value
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value
    @property
    def place_birth(self):
        return self._place_birth

    @place_birth.setter
    def place_birth(self, value):
        self._place_birth = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value


    def to_alipay_dict(self):
        params = dict()
        if self.birth_gestational_weeks:
            if hasattr(self.birth_gestational_weeks, 'to_alipay_dict'):
                params['birth_gestational_weeks'] = self.birth_gestational_weeks.to_alipay_dict()
            else:
                params['birth_gestational_weeks'] = self.birth_gestational_weeks
        if self.birth_length:
            if hasattr(self.birth_length, 'to_alipay_dict'):
                params['birth_length'] = self.birth_length.to_alipay_dict()
            else:
                params['birth_length'] = self.birth_length
        if self.birth_medical_institution:
            if hasattr(self.birth_medical_institution, 'to_alipay_dict'):
                params['birth_medical_institution'] = self.birth_medical_institution.to_alipay_dict()
            else:
                params['birth_medical_institution'] = self.birth_medical_institution
        if self.birth_time:
            if hasattr(self.birth_time, 'to_alipay_dict'):
                params['birth_time'] = self.birth_time.to_alipay_dict()
            else:
                params['birth_time'] = self.birth_time
        if self.birth_weight:
            if hasattr(self.birth_weight, 'to_alipay_dict'):
                params['birth_weight'] = self.birth_weight.to_alipay_dict()
            else:
                params['birth_weight'] = self.birth_weight
        if self.date_issue:
            if hasattr(self.date_issue, 'to_alipay_dict'):
                params['date_issue'] = self.date_issue.to_alipay_dict()
            else:
                params['date_issue'] = self.date_issue
        if self.father_address:
            if hasattr(self.father_address, 'to_alipay_dict'):
                params['father_address'] = self.father_address.to_alipay_dict()
            else:
                params['father_address'] = self.father_address
        if self.father_age:
            if hasattr(self.father_age, 'to_alipay_dict'):
                params['father_age'] = self.father_age.to_alipay_dict()
            else:
                params['father_age'] = self.father_age
        if self.father_country:
            if hasattr(self.father_country, 'to_alipay_dict'):
                params['father_country'] = self.father_country.to_alipay_dict()
            else:
                params['father_country'] = self.father_country
        if self.father_id_card:
            if hasattr(self.father_id_card, 'to_alipay_dict'):
                params['father_id_card'] = self.father_id_card.to_alipay_dict()
            else:
                params['father_id_card'] = self.father_id_card
        if self.father_name:
            if hasattr(self.father_name, 'to_alipay_dict'):
                params['father_name'] = self.father_name.to_alipay_dict()
            else:
                params['father_name'] = self.father_name
        if self.father_nationality:
            if hasattr(self.father_nationality, 'to_alipay_dict'):
                params['father_nationality'] = self.father_nationality.to_alipay_dict()
            else:
                params['father_nationality'] = self.father_nationality
        if self.full_name:
            if hasattr(self.full_name, 'to_alipay_dict'):
                params['full_name'] = self.full_name.to_alipay_dict()
            else:
                params['full_name'] = self.full_name
        if self.mother_address:
            if hasattr(self.mother_address, 'to_alipay_dict'):
                params['mother_address'] = self.mother_address.to_alipay_dict()
            else:
                params['mother_address'] = self.mother_address
        if self.mother_age:
            if hasattr(self.mother_age, 'to_alipay_dict'):
                params['mother_age'] = self.mother_age.to_alipay_dict()
            else:
                params['mother_age'] = self.mother_age
        if self.mother_country:
            if hasattr(self.mother_country, 'to_alipay_dict'):
                params['mother_country'] = self.mother_country.to_alipay_dict()
            else:
                params['mother_country'] = self.mother_country
        if self.mother_id_card:
            if hasattr(self.mother_id_card, 'to_alipay_dict'):
                params['mother_id_card'] = self.mother_id_card.to_alipay_dict()
            else:
                params['mother_id_card'] = self.mother_id_card
        if self.mother_name:
            if hasattr(self.mother_name, 'to_alipay_dict'):
                params['mother_name'] = self.mother_name.to_alipay_dict()
            else:
                params['mother_name'] = self.mother_name
        if self.mother_nationality:
            if hasattr(self.mother_nationality, 'to_alipay_dict'):
                params['mother_nationality'] = self.mother_nationality.to_alipay_dict()
            else:
                params['mother_nationality'] = self.mother_nationality
        if self.number:
            if hasattr(self.number, 'to_alipay_dict'):
                params['number'] = self.number.to_alipay_dict()
            else:
                params['number'] = self.number
        if self.place_birth:
            if hasattr(self.place_birth, 'to_alipay_dict'):
                params['place_birth'] = self.place_birth.to_alipay_dict()
            else:
                params['place_birth'] = self.place_birth
        if self.sex:
            if hasattr(self.sex, 'to_alipay_dict'):
                params['sex'] = self.sex.to_alipay_dict()
            else:
                params['sex'] = self.sex
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BirthCertificateDTO()
        if 'birth_gestational_weeks' in d:
            o.birth_gestational_weeks = d['birth_gestational_weeks']
        if 'birth_length' in d:
            o.birth_length = d['birth_length']
        if 'birth_medical_institution' in d:
            o.birth_medical_institution = d['birth_medical_institution']
        if 'birth_time' in d:
            o.birth_time = d['birth_time']
        if 'birth_weight' in d:
            o.birth_weight = d['birth_weight']
        if 'date_issue' in d:
            o.date_issue = d['date_issue']
        if 'father_address' in d:
            o.father_address = d['father_address']
        if 'father_age' in d:
            o.father_age = d['father_age']
        if 'father_country' in d:
            o.father_country = d['father_country']
        if 'father_id_card' in d:
            o.father_id_card = d['father_id_card']
        if 'father_name' in d:
            o.father_name = d['father_name']
        if 'father_nationality' in d:
            o.father_nationality = d['father_nationality']
        if 'full_name' in d:
            o.full_name = d['full_name']
        if 'mother_address' in d:
            o.mother_address = d['mother_address']
        if 'mother_age' in d:
            o.mother_age = d['mother_age']
        if 'mother_country' in d:
            o.mother_country = d['mother_country']
        if 'mother_id_card' in d:
            o.mother_id_card = d['mother_id_card']
        if 'mother_name' in d:
            o.mother_name = d['mother_name']
        if 'mother_nationality' in d:
            o.mother_nationality = d['mother_nationality']
        if 'number' in d:
            o.number = d['number']
        if 'place_birth' in d:
            o.place_birth = d['place_birth']
        if 'sex' in d:
            o.sex = d['sex']
        return o


