#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TuitionISVStudentInfoDTO(object):

    def __init__(self):
        self._email = None
        self._entrance_date = None
        self._first_name = None
        self._identity_card_number = None
        self._last_name = None
        self._student_name = None
        self._student_number = None
        self._student_phone_number = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def entrance_date(self):
        return self._entrance_date

    @entrance_date.setter
    def entrance_date(self, value):
        self._entrance_date = value
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value
    @property
    def identity_card_number(self):
        return self._identity_card_number

    @identity_card_number.setter
    def identity_card_number(self, value):
        self._identity_card_number = value
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value
    @property
    def student_name(self):
        return self._student_name

    @student_name.setter
    def student_name(self, value):
        self._student_name = value
    @property
    def student_number(self):
        return self._student_number

    @student_number.setter
    def student_number(self, value):
        self._student_number = value
    @property
    def student_phone_number(self):
        return self._student_phone_number

    @student_phone_number.setter
    def student_phone_number(self, value):
        self._student_phone_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.entrance_date:
            if hasattr(self.entrance_date, 'to_alipay_dict'):
                params['entrance_date'] = self.entrance_date.to_alipay_dict()
            else:
                params['entrance_date'] = self.entrance_date
        if self.first_name:
            if hasattr(self.first_name, 'to_alipay_dict'):
                params['first_name'] = self.first_name.to_alipay_dict()
            else:
                params['first_name'] = self.first_name
        if self.identity_card_number:
            if hasattr(self.identity_card_number, 'to_alipay_dict'):
                params['identity_card_number'] = self.identity_card_number.to_alipay_dict()
            else:
                params['identity_card_number'] = self.identity_card_number
        if self.last_name:
            if hasattr(self.last_name, 'to_alipay_dict'):
                params['last_name'] = self.last_name.to_alipay_dict()
            else:
                params['last_name'] = self.last_name
        if self.student_name:
            if hasattr(self.student_name, 'to_alipay_dict'):
                params['student_name'] = self.student_name.to_alipay_dict()
            else:
                params['student_name'] = self.student_name
        if self.student_number:
            if hasattr(self.student_number, 'to_alipay_dict'):
                params['student_number'] = self.student_number.to_alipay_dict()
            else:
                params['student_number'] = self.student_number
        if self.student_phone_number:
            if hasattr(self.student_phone_number, 'to_alipay_dict'):
                params['student_phone_number'] = self.student_phone_number.to_alipay_dict()
            else:
                params['student_phone_number'] = self.student_phone_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TuitionISVStudentInfoDTO()
        if 'email' in d:
            o.email = d['email']
        if 'entrance_date' in d:
            o.entrance_date = d['entrance_date']
        if 'first_name' in d:
            o.first_name = d['first_name']
        if 'identity_card_number' in d:
            o.identity_card_number = d['identity_card_number']
        if 'last_name' in d:
            o.last_name = d['last_name']
        if 'student_name' in d:
            o.student_name = d['student_name']
        if 'student_number' in d:
            o.student_number = d['student_number']
        if 'student_phone_number' in d:
            o.student_phone_number = d['student_phone_number']
        return o


