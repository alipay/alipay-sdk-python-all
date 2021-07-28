#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FamilyArchiveDetail(object):

    def __init__(self):
        self._address = None
        self._archive_id = None
        self._area = None
        self._birthday = None
        self._cert_no = None
        self._cert_type = None
        self._city = None
        self._desensitized_logon_id = None
        self._desensitized_real_name = None
        self._email = None
        self._gender = None
        self._mobile = None
        self._profession = None
        self._province = None
        self._real_name = None
        self._role = None
        self._zip = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def archive_id(self):
        return self._archive_id

    @archive_id.setter
    def archive_id(self, value):
        self._archive_id = value
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def desensitized_logon_id(self):
        return self._desensitized_logon_id

    @desensitized_logon_id.setter
    def desensitized_logon_id(self, value):
        self._desensitized_logon_id = value
    @property
    def desensitized_real_name(self):
        return self._desensitized_real_name

    @desensitized_real_name.setter
    def desensitized_real_name(self, value):
        self._desensitized_real_name = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, value):
        self._profession = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def zip(self):
        return self._zip

    @zip.setter
    def zip(self, value):
        self._zip = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.archive_id:
            if hasattr(self.archive_id, 'to_alipay_dict'):
                params['archive_id'] = self.archive_id.to_alipay_dict()
            else:
                params['archive_id'] = self.archive_id
        if self.area:
            if hasattr(self.area, 'to_alipay_dict'):
                params['area'] = self.area.to_alipay_dict()
            else:
                params['area'] = self.area
        if self.birthday:
            if hasattr(self.birthday, 'to_alipay_dict'):
                params['birthday'] = self.birthday.to_alipay_dict()
            else:
                params['birthday'] = self.birthday
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.desensitized_logon_id:
            if hasattr(self.desensitized_logon_id, 'to_alipay_dict'):
                params['desensitized_logon_id'] = self.desensitized_logon_id.to_alipay_dict()
            else:
                params['desensitized_logon_id'] = self.desensitized_logon_id
        if self.desensitized_real_name:
            if hasattr(self.desensitized_real_name, 'to_alipay_dict'):
                params['desensitized_real_name'] = self.desensitized_real_name.to_alipay_dict()
            else:
                params['desensitized_real_name'] = self.desensitized_real_name
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.profession:
            if hasattr(self.profession, 'to_alipay_dict'):
                params['profession'] = self.profession.to_alipay_dict()
            else:
                params['profession'] = self.profession
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.zip:
            if hasattr(self.zip, 'to_alipay_dict'):
                params['zip'] = self.zip.to_alipay_dict()
            else:
                params['zip'] = self.zip
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FamilyArchiveDetail()
        if 'address' in d:
            o.address = d['address']
        if 'archive_id' in d:
            o.archive_id = d['archive_id']
        if 'area' in d:
            o.area = d['area']
        if 'birthday' in d:
            o.birthday = d['birthday']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'city' in d:
            o.city = d['city']
        if 'desensitized_logon_id' in d:
            o.desensitized_logon_id = d['desensitized_logon_id']
        if 'desensitized_real_name' in d:
            o.desensitized_real_name = d['desensitized_real_name']
        if 'email' in d:
            o.email = d['email']
        if 'gender' in d:
            o.gender = d['gender']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'profession' in d:
            o.profession = d['profession']
        if 'province' in d:
            o.province = d['province']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'role' in d:
            o.role = d['role']
        if 'zip' in d:
            o.zip = d['zip']
        return o


