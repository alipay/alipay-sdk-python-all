#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsPerson(object):

    def __init__(self):
        self._address = None
        self._area_code = None
        self._birthday = None
        self._biz_data = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._channel_user_id = None
        self._channel_user_source = None
        self._email = None
        self._gender = None
        self._identity_type = None
        self._nationality = None
        self._phone = None
        self._pronounce_name = None
        self._user_id = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
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
    def channel_user_id(self):
        return self._channel_user_id

    @channel_user_id.setter
    def channel_user_id(self, value):
        self._channel_user_id = value
    @property
    def channel_user_source(self):
        return self._channel_user_source

    @channel_user_source.setter
    def channel_user_source(self, value):
        self._channel_user_source = value
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
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        self._nationality = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def pronounce_name(self):
        return self._pronounce_name

    @pronounce_name.setter
    def pronounce_name(self, value):
        self._pronounce_name = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.birthday:
            if hasattr(self.birthday, 'to_alipay_dict'):
                params['birthday'] = self.birthday.to_alipay_dict()
            else:
                params['birthday'] = self.birthday
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
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
        if self.channel_user_id:
            if hasattr(self.channel_user_id, 'to_alipay_dict'):
                params['channel_user_id'] = self.channel_user_id.to_alipay_dict()
            else:
                params['channel_user_id'] = self.channel_user_id
        if self.channel_user_source:
            if hasattr(self.channel_user_source, 'to_alipay_dict'):
                params['channel_user_source'] = self.channel_user_source.to_alipay_dict()
            else:
                params['channel_user_source'] = self.channel_user_source
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
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.nationality:
            if hasattr(self.nationality, 'to_alipay_dict'):
                params['nationality'] = self.nationality.to_alipay_dict()
            else:
                params['nationality'] = self.nationality
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.pronounce_name:
            if hasattr(self.pronounce_name, 'to_alipay_dict'):
                params['pronounce_name'] = self.pronounce_name.to_alipay_dict()
            else:
                params['pronounce_name'] = self.pronounce_name
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsPerson()
        if 'address' in d:
            o.address = d['address']
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'birthday' in d:
            o.birthday = d['birthday']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'channel_user_id' in d:
            o.channel_user_id = d['channel_user_id']
        if 'channel_user_source' in d:
            o.channel_user_source = d['channel_user_source']
        if 'email' in d:
            o.email = d['email']
        if 'gender' in d:
            o.gender = d['gender']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'nationality' in d:
            o.nationality = d['nationality']
        if 'phone' in d:
            o.phone = d['phone']
        if 'pronounce_name' in d:
            o.pronounce_name = d['pronounce_name']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


