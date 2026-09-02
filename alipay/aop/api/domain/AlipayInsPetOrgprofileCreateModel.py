#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsPetOrgprofileCreateModel(object):

    def __init__(self):
        self._org_code = None
        self._out_biz_no = None
        self._pet_birthday = None
        self._pet_breed_code = None
        self._pet_breed_name = None
        self._pet_face_url = None
        self._pet_gender = None
        self._pet_nick = None
        self._pet_no_baby = None
        self._pet_type = None

    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pet_birthday(self):
        return self._pet_birthday

    @pet_birthday.setter
    def pet_birthday(self, value):
        self._pet_birthday = value
    @property
    def pet_breed_code(self):
        return self._pet_breed_code

    @pet_breed_code.setter
    def pet_breed_code(self, value):
        self._pet_breed_code = value
    @property
    def pet_breed_name(self):
        return self._pet_breed_name

    @pet_breed_name.setter
    def pet_breed_name(self, value):
        self._pet_breed_name = value
    @property
    def pet_face_url(self):
        return self._pet_face_url

    @pet_face_url.setter
    def pet_face_url(self, value):
        self._pet_face_url = value
    @property
    def pet_gender(self):
        return self._pet_gender

    @pet_gender.setter
    def pet_gender(self, value):
        self._pet_gender = value
    @property
    def pet_nick(self):
        return self._pet_nick

    @pet_nick.setter
    def pet_nick(self, value):
        self._pet_nick = value
    @property
    def pet_no_baby(self):
        return self._pet_no_baby

    @pet_no_baby.setter
    def pet_no_baby(self, value):
        self._pet_no_baby = value
    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, value):
        self._pet_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pet_birthday:
            if hasattr(self.pet_birthday, 'to_alipay_dict'):
                params['pet_birthday'] = self.pet_birthday.to_alipay_dict()
            else:
                params['pet_birthday'] = self.pet_birthday
        if self.pet_breed_code:
            if hasattr(self.pet_breed_code, 'to_alipay_dict'):
                params['pet_breed_code'] = self.pet_breed_code.to_alipay_dict()
            else:
                params['pet_breed_code'] = self.pet_breed_code
        if self.pet_breed_name:
            if hasattr(self.pet_breed_name, 'to_alipay_dict'):
                params['pet_breed_name'] = self.pet_breed_name.to_alipay_dict()
            else:
                params['pet_breed_name'] = self.pet_breed_name
        if self.pet_face_url:
            if hasattr(self.pet_face_url, 'to_alipay_dict'):
                params['pet_face_url'] = self.pet_face_url.to_alipay_dict()
            else:
                params['pet_face_url'] = self.pet_face_url
        if self.pet_gender:
            if hasattr(self.pet_gender, 'to_alipay_dict'):
                params['pet_gender'] = self.pet_gender.to_alipay_dict()
            else:
                params['pet_gender'] = self.pet_gender
        if self.pet_nick:
            if hasattr(self.pet_nick, 'to_alipay_dict'):
                params['pet_nick'] = self.pet_nick.to_alipay_dict()
            else:
                params['pet_nick'] = self.pet_nick
        if self.pet_no_baby:
            if hasattr(self.pet_no_baby, 'to_alipay_dict'):
                params['pet_no_baby'] = self.pet_no_baby.to_alipay_dict()
            else:
                params['pet_no_baby'] = self.pet_no_baby
        if self.pet_type:
            if hasattr(self.pet_type, 'to_alipay_dict'):
                params['pet_type'] = self.pet_type.to_alipay_dict()
            else:
                params['pet_type'] = self.pet_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsPetOrgprofileCreateModel()
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pet_birthday' in d:
            o.pet_birthday = d['pet_birthday']
        if 'pet_breed_code' in d:
            o.pet_breed_code = d['pet_breed_code']
        if 'pet_breed_name' in d:
            o.pet_breed_name = d['pet_breed_name']
        if 'pet_face_url' in d:
            o.pet_face_url = d['pet_face_url']
        if 'pet_gender' in d:
            o.pet_gender = d['pet_gender']
        if 'pet_nick' in d:
            o.pet_nick = d['pet_nick']
        if 'pet_no_baby' in d:
            o.pet_no_baby = d['pet_no_baby']
        if 'pet_type' in d:
            o.pet_type = d['pet_type']
        return o


