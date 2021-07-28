#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ParticipantInfo(object):

    def __init__(self):
        self._contact_address = None
        self._current_school = None
        self._e_mail = None
        self._id_number = None
        self._id_type = None
        self._name = None
        self._photo = None
        self._sex = None
        self._tel_number = None

    @property
    def contact_address(self):
        return self._contact_address

    @contact_address.setter
    def contact_address(self, value):
        self._contact_address = value
    @property
    def current_school(self):
        return self._current_school

    @current_school.setter
    def current_school(self, value):
        self._current_school = value
    @property
    def e_mail(self):
        return self._e_mail

    @e_mail.setter
    def e_mail(self, value):
        self._e_mail = value
    @property
    def id_number(self):
        return self._id_number

    @id_number.setter
    def id_number(self, value):
        self._id_number = value
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def photo(self):
        return self._photo

    @photo.setter
    def photo(self, value):
        self._photo = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value
    @property
    def tel_number(self):
        return self._tel_number

    @tel_number.setter
    def tel_number(self, value):
        self._tel_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_address:
            if hasattr(self.contact_address, 'to_alipay_dict'):
                params['contact_address'] = self.contact_address.to_alipay_dict()
            else:
                params['contact_address'] = self.contact_address
        if self.current_school:
            if hasattr(self.current_school, 'to_alipay_dict'):
                params['current_school'] = self.current_school.to_alipay_dict()
            else:
                params['current_school'] = self.current_school
        if self.e_mail:
            if hasattr(self.e_mail, 'to_alipay_dict'):
                params['e_mail'] = self.e_mail.to_alipay_dict()
            else:
                params['e_mail'] = self.e_mail
        if self.id_number:
            if hasattr(self.id_number, 'to_alipay_dict'):
                params['id_number'] = self.id_number.to_alipay_dict()
            else:
                params['id_number'] = self.id_number
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.photo:
            if hasattr(self.photo, 'to_alipay_dict'):
                params['photo'] = self.photo.to_alipay_dict()
            else:
                params['photo'] = self.photo
        if self.sex:
            if hasattr(self.sex, 'to_alipay_dict'):
                params['sex'] = self.sex.to_alipay_dict()
            else:
                params['sex'] = self.sex
        if self.tel_number:
            if hasattr(self.tel_number, 'to_alipay_dict'):
                params['tel_number'] = self.tel_number.to_alipay_dict()
            else:
                params['tel_number'] = self.tel_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ParticipantInfo()
        if 'contact_address' in d:
            o.contact_address = d['contact_address']
        if 'current_school' in d:
            o.current_school = d['current_school']
        if 'e_mail' in d:
            o.e_mail = d['e_mail']
        if 'id_number' in d:
            o.id_number = d['id_number']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'name' in d:
            o.name = d['name']
        if 'photo' in d:
            o.photo = d['photo']
        if 'sex' in d:
            o.sex = d['sex']
        if 'tel_number' in d:
            o.tel_number = d['tel_number']
        return o


