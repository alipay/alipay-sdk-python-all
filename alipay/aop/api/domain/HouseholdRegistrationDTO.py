#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HouseholdRegistrationDTO(object):

    def __init__(self):
        self._address = None
        self._birth_date = None
        self._birth_place = None
        self._blood_desc = None
        self._career = None
        self._city_other_addresses = None
        self._contractor = None
        self._data_issue = None
        self._degree_of_education = None
        self._former_name = None
        self._full_name = None
        self._height = None
        self._household_number = None
        self._household_type = None
        self._id_card = None
        self._marital_desc = None
        self._military_desc = None
        self._nationality = None
        self._native_place = None
        self._person_id = None
        self._print_date = None
        self._registration_date = None
        self._relationship_desc = None
        self._religion = None
        self._service_location = None
        self._sex = None
        self._when_and_from_moved_address = None
        self._when_and_from_moved_city = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value
    @property
    def birth_place(self):
        return self._birth_place

    @birth_place.setter
    def birth_place(self, value):
        self._birth_place = value
    @property
    def blood_desc(self):
        return self._blood_desc

    @blood_desc.setter
    def blood_desc(self, value):
        self._blood_desc = value
    @property
    def career(self):
        return self._career

    @career.setter
    def career(self, value):
        self._career = value
    @property
    def city_other_addresses(self):
        return self._city_other_addresses

    @city_other_addresses.setter
    def city_other_addresses(self, value):
        self._city_other_addresses = value
    @property
    def contractor(self):
        return self._contractor

    @contractor.setter
    def contractor(self, value):
        self._contractor = value
    @property
    def data_issue(self):
        return self._data_issue

    @data_issue.setter
    def data_issue(self, value):
        self._data_issue = value
    @property
    def degree_of_education(self):
        return self._degree_of_education

    @degree_of_education.setter
    def degree_of_education(self, value):
        self._degree_of_education = value
    @property
    def former_name(self):
        return self._former_name

    @former_name.setter
    def former_name(self, value):
        self._former_name = value
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def household_number(self):
        return self._household_number

    @household_number.setter
    def household_number(self, value):
        self._household_number = value
    @property
    def household_type(self):
        return self._household_type

    @household_type.setter
    def household_type(self, value):
        self._household_type = value
    @property
    def id_card(self):
        return self._id_card

    @id_card.setter
    def id_card(self, value):
        self._id_card = value
    @property
    def marital_desc(self):
        return self._marital_desc

    @marital_desc.setter
    def marital_desc(self, value):
        self._marital_desc = value
    @property
    def military_desc(self):
        return self._military_desc

    @military_desc.setter
    def military_desc(self, value):
        self._military_desc = value
    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        self._nationality = value
    @property
    def native_place(self):
        return self._native_place

    @native_place.setter
    def native_place(self, value):
        self._native_place = value
    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, value):
        self._person_id = value
    @property
    def print_date(self):
        return self._print_date

    @print_date.setter
    def print_date(self, value):
        self._print_date = value
    @property
    def registration_date(self):
        return self._registration_date

    @registration_date.setter
    def registration_date(self, value):
        self._registration_date = value
    @property
    def relationship_desc(self):
        return self._relationship_desc

    @relationship_desc.setter
    def relationship_desc(self, value):
        self._relationship_desc = value
    @property
    def religion(self):
        return self._religion

    @religion.setter
    def religion(self, value):
        self._religion = value
    @property
    def service_location(self):
        return self._service_location

    @service_location.setter
    def service_location(self, value):
        self._service_location = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value
    @property
    def when_and_from_moved_address(self):
        return self._when_and_from_moved_address

    @when_and_from_moved_address.setter
    def when_and_from_moved_address(self, value):
        self._when_and_from_moved_address = value
    @property
    def when_and_from_moved_city(self):
        return self._when_and_from_moved_city

    @when_and_from_moved_city.setter
    def when_and_from_moved_city(self, value):
        self._when_and_from_moved_city = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.birth_date:
            if hasattr(self.birth_date, 'to_alipay_dict'):
                params['birth_date'] = self.birth_date.to_alipay_dict()
            else:
                params['birth_date'] = self.birth_date
        if self.birth_place:
            if hasattr(self.birth_place, 'to_alipay_dict'):
                params['birth_place'] = self.birth_place.to_alipay_dict()
            else:
                params['birth_place'] = self.birth_place
        if self.blood_desc:
            if hasattr(self.blood_desc, 'to_alipay_dict'):
                params['blood_desc'] = self.blood_desc.to_alipay_dict()
            else:
                params['blood_desc'] = self.blood_desc
        if self.career:
            if hasattr(self.career, 'to_alipay_dict'):
                params['career'] = self.career.to_alipay_dict()
            else:
                params['career'] = self.career
        if self.city_other_addresses:
            if hasattr(self.city_other_addresses, 'to_alipay_dict'):
                params['city_other_addresses'] = self.city_other_addresses.to_alipay_dict()
            else:
                params['city_other_addresses'] = self.city_other_addresses
        if self.contractor:
            if hasattr(self.contractor, 'to_alipay_dict'):
                params['contractor'] = self.contractor.to_alipay_dict()
            else:
                params['contractor'] = self.contractor
        if self.data_issue:
            if hasattr(self.data_issue, 'to_alipay_dict'):
                params['data_issue'] = self.data_issue.to_alipay_dict()
            else:
                params['data_issue'] = self.data_issue
        if self.degree_of_education:
            if hasattr(self.degree_of_education, 'to_alipay_dict'):
                params['degree_of_education'] = self.degree_of_education.to_alipay_dict()
            else:
                params['degree_of_education'] = self.degree_of_education
        if self.former_name:
            if hasattr(self.former_name, 'to_alipay_dict'):
                params['former_name'] = self.former_name.to_alipay_dict()
            else:
                params['former_name'] = self.former_name
        if self.full_name:
            if hasattr(self.full_name, 'to_alipay_dict'):
                params['full_name'] = self.full_name.to_alipay_dict()
            else:
                params['full_name'] = self.full_name
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.household_number:
            if hasattr(self.household_number, 'to_alipay_dict'):
                params['household_number'] = self.household_number.to_alipay_dict()
            else:
                params['household_number'] = self.household_number
        if self.household_type:
            if hasattr(self.household_type, 'to_alipay_dict'):
                params['household_type'] = self.household_type.to_alipay_dict()
            else:
                params['household_type'] = self.household_type
        if self.id_card:
            if hasattr(self.id_card, 'to_alipay_dict'):
                params['id_card'] = self.id_card.to_alipay_dict()
            else:
                params['id_card'] = self.id_card
        if self.marital_desc:
            if hasattr(self.marital_desc, 'to_alipay_dict'):
                params['marital_desc'] = self.marital_desc.to_alipay_dict()
            else:
                params['marital_desc'] = self.marital_desc
        if self.military_desc:
            if hasattr(self.military_desc, 'to_alipay_dict'):
                params['military_desc'] = self.military_desc.to_alipay_dict()
            else:
                params['military_desc'] = self.military_desc
        if self.nationality:
            if hasattr(self.nationality, 'to_alipay_dict'):
                params['nationality'] = self.nationality.to_alipay_dict()
            else:
                params['nationality'] = self.nationality
        if self.native_place:
            if hasattr(self.native_place, 'to_alipay_dict'):
                params['native_place'] = self.native_place.to_alipay_dict()
            else:
                params['native_place'] = self.native_place
        if self.person_id:
            if hasattr(self.person_id, 'to_alipay_dict'):
                params['person_id'] = self.person_id.to_alipay_dict()
            else:
                params['person_id'] = self.person_id
        if self.print_date:
            if hasattr(self.print_date, 'to_alipay_dict'):
                params['print_date'] = self.print_date.to_alipay_dict()
            else:
                params['print_date'] = self.print_date
        if self.registration_date:
            if hasattr(self.registration_date, 'to_alipay_dict'):
                params['registration_date'] = self.registration_date.to_alipay_dict()
            else:
                params['registration_date'] = self.registration_date
        if self.relationship_desc:
            if hasattr(self.relationship_desc, 'to_alipay_dict'):
                params['relationship_desc'] = self.relationship_desc.to_alipay_dict()
            else:
                params['relationship_desc'] = self.relationship_desc
        if self.religion:
            if hasattr(self.religion, 'to_alipay_dict'):
                params['religion'] = self.religion.to_alipay_dict()
            else:
                params['religion'] = self.religion
        if self.service_location:
            if hasattr(self.service_location, 'to_alipay_dict'):
                params['service_location'] = self.service_location.to_alipay_dict()
            else:
                params['service_location'] = self.service_location
        if self.sex:
            if hasattr(self.sex, 'to_alipay_dict'):
                params['sex'] = self.sex.to_alipay_dict()
            else:
                params['sex'] = self.sex
        if self.when_and_from_moved_address:
            if hasattr(self.when_and_from_moved_address, 'to_alipay_dict'):
                params['when_and_from_moved_address'] = self.when_and_from_moved_address.to_alipay_dict()
            else:
                params['when_and_from_moved_address'] = self.when_and_from_moved_address
        if self.when_and_from_moved_city:
            if hasattr(self.when_and_from_moved_city, 'to_alipay_dict'):
                params['when_and_from_moved_city'] = self.when_and_from_moved_city.to_alipay_dict()
            else:
                params['when_and_from_moved_city'] = self.when_and_from_moved_city
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HouseholdRegistrationDTO()
        if 'address' in d:
            o.address = d['address']
        if 'birth_date' in d:
            o.birth_date = d['birth_date']
        if 'birth_place' in d:
            o.birth_place = d['birth_place']
        if 'blood_desc' in d:
            o.blood_desc = d['blood_desc']
        if 'career' in d:
            o.career = d['career']
        if 'city_other_addresses' in d:
            o.city_other_addresses = d['city_other_addresses']
        if 'contractor' in d:
            o.contractor = d['contractor']
        if 'data_issue' in d:
            o.data_issue = d['data_issue']
        if 'degree_of_education' in d:
            o.degree_of_education = d['degree_of_education']
        if 'former_name' in d:
            o.former_name = d['former_name']
        if 'full_name' in d:
            o.full_name = d['full_name']
        if 'height' in d:
            o.height = d['height']
        if 'household_number' in d:
            o.household_number = d['household_number']
        if 'household_type' in d:
            o.household_type = d['household_type']
        if 'id_card' in d:
            o.id_card = d['id_card']
        if 'marital_desc' in d:
            o.marital_desc = d['marital_desc']
        if 'military_desc' in d:
            o.military_desc = d['military_desc']
        if 'nationality' in d:
            o.nationality = d['nationality']
        if 'native_place' in d:
            o.native_place = d['native_place']
        if 'person_id' in d:
            o.person_id = d['person_id']
        if 'print_date' in d:
            o.print_date = d['print_date']
        if 'registration_date' in d:
            o.registration_date = d['registration_date']
        if 'relationship_desc' in d:
            o.relationship_desc = d['relationship_desc']
        if 'religion' in d:
            o.religion = d['religion']
        if 'service_location' in d:
            o.service_location = d['service_location']
        if 'sex' in d:
            o.sex = d['sex']
        if 'when_and_from_moved_address' in d:
            o.when_and_from_moved_address = d['when_and_from_moved_address']
        if 'when_and_from_moved_city' in d:
            o.when_and_from_moved_city = d['when_and_from_moved_city']
        return o


