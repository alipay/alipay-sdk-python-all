#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MemberArchiveOpenApiInfoDTO(object):

    def __init__(self):
        self._age = None
        self._archive_no = None
        self._avatar = None
        self._birthday = None
        self._desensitization_id_number = None
        self._desensitization_phone = None
        self._desensitization_username = None
        self._gender = None
        self._id_number = None
        self._id_type = None
        self._phone = None
        self._role_type = None
        self._user_name = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def archive_no(self):
        return self._archive_no

    @archive_no.setter
    def archive_no(self, value):
        self._archive_no = value
    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
    @property
    def desensitization_id_number(self):
        return self._desensitization_id_number

    @desensitization_id_number.setter
    def desensitization_id_number(self, value):
        self._desensitization_id_number = value
    @property
    def desensitization_phone(self):
        return self._desensitization_phone

    @desensitization_phone.setter
    def desensitization_phone(self, value):
        self._desensitization_phone = value
    @property
    def desensitization_username(self):
        return self._desensitization_username

    @desensitization_username.setter
    def desensitization_username(self, value):
        self._desensitization_username = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
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
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.archive_no:
            if hasattr(self.archive_no, 'to_alipay_dict'):
                params['archive_no'] = self.archive_no.to_alipay_dict()
            else:
                params['archive_no'] = self.archive_no
        if self.avatar:
            if hasattr(self.avatar, 'to_alipay_dict'):
                params['avatar'] = self.avatar.to_alipay_dict()
            else:
                params['avatar'] = self.avatar
        if self.birthday:
            if hasattr(self.birthday, 'to_alipay_dict'):
                params['birthday'] = self.birthday.to_alipay_dict()
            else:
                params['birthday'] = self.birthday
        if self.desensitization_id_number:
            if hasattr(self.desensitization_id_number, 'to_alipay_dict'):
                params['desensitization_id_number'] = self.desensitization_id_number.to_alipay_dict()
            else:
                params['desensitization_id_number'] = self.desensitization_id_number
        if self.desensitization_phone:
            if hasattr(self.desensitization_phone, 'to_alipay_dict'):
                params['desensitization_phone'] = self.desensitization_phone.to_alipay_dict()
            else:
                params['desensitization_phone'] = self.desensitization_phone
        if self.desensitization_username:
            if hasattr(self.desensitization_username, 'to_alipay_dict'):
                params['desensitization_username'] = self.desensitization_username.to_alipay_dict()
            else:
                params['desensitization_username'] = self.desensitization_username
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
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
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.role_type:
            if hasattr(self.role_type, 'to_alipay_dict'):
                params['role_type'] = self.role_type.to_alipay_dict()
            else:
                params['role_type'] = self.role_type
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberArchiveOpenApiInfoDTO()
        if 'age' in d:
            o.age = d['age']
        if 'archive_no' in d:
            o.archive_no = d['archive_no']
        if 'avatar' in d:
            o.avatar = d['avatar']
        if 'birthday' in d:
            o.birthday = d['birthday']
        if 'desensitization_id_number' in d:
            o.desensitization_id_number = d['desensitization_id_number']
        if 'desensitization_phone' in d:
            o.desensitization_phone = d['desensitization_phone']
        if 'desensitization_username' in d:
            o.desensitization_username = d['desensitization_username']
        if 'gender' in d:
            o.gender = d['gender']
        if 'id_number' in d:
            o.id_number = d['id_number']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'phone' in d:
            o.phone = d['phone']
        if 'role_type' in d:
            o.role_type = d['role_type']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


