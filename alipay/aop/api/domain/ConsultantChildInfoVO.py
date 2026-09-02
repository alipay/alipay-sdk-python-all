#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsultantChildInfoVO(object):

    def __init__(self):
        self._birth_date = None
        self._gender = None
        self._phone = None
        self._profile_id = None
        self._profile_name = None

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def profile_id(self):
        return self._profile_id

    @profile_id.setter
    def profile_id(self, value):
        self._profile_id = value
    @property
    def profile_name(self):
        return self._profile_name

    @profile_name.setter
    def profile_name(self, value):
        self._profile_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.birth_date:
            if hasattr(self.birth_date, 'to_alipay_dict'):
                params['birth_date'] = self.birth_date.to_alipay_dict()
            else:
                params['birth_date'] = self.birth_date
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.profile_id:
            if hasattr(self.profile_id, 'to_alipay_dict'):
                params['profile_id'] = self.profile_id.to_alipay_dict()
            else:
                params['profile_id'] = self.profile_id
        if self.profile_name:
            if hasattr(self.profile_name, 'to_alipay_dict'):
                params['profile_name'] = self.profile_name.to_alipay_dict()
            else:
                params['profile_name'] = self.profile_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsultantChildInfoVO()
        if 'birth_date' in d:
            o.birth_date = d['birth_date']
        if 'gender' in d:
            o.gender = d['gender']
        if 'phone' in d:
            o.phone = d['phone']
        if 'profile_id' in d:
            o.profile_id = d['profile_id']
        if 'profile_name' in d:
            o.profile_name = d['profile_name']
        return o


