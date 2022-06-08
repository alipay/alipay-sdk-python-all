#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LabelValue import LabelValue


class RightsFormItemValues(object):

    def __init__(self):
        self._crn = None
        self._email = None
        self._ep_name = None
        self._legal_person = None
        self._other_fields = None
        self._phone = None
        self._submit_time = None
        self._user_id = None

    @property
    def crn(self):
        return self._crn

    @crn.setter
    def crn(self, value):
        self._crn = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def legal_person(self):
        return self._legal_person

    @legal_person.setter
    def legal_person(self, value):
        self._legal_person = value
    @property
    def other_fields(self):
        return self._other_fields

    @other_fields.setter
    def other_fields(self, value):
        if isinstance(value, list):
            self._other_fields = list()
            for i in value:
                if isinstance(i, LabelValue):
                    self._other_fields.append(i)
                else:
                    self._other_fields.append(LabelValue.from_alipay_dict(i))
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def submit_time(self):
        return self._submit_time

    @submit_time.setter
    def submit_time(self, value):
        self._submit_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.crn:
            if hasattr(self.crn, 'to_alipay_dict'):
                params['crn'] = self.crn.to_alipay_dict()
            else:
                params['crn'] = self.crn
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.legal_person:
            if hasattr(self.legal_person, 'to_alipay_dict'):
                params['legal_person'] = self.legal_person.to_alipay_dict()
            else:
                params['legal_person'] = self.legal_person
        if self.other_fields:
            if isinstance(self.other_fields, list):
                for i in range(0, len(self.other_fields)):
                    element = self.other_fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_fields[i] = element.to_alipay_dict()
            if hasattr(self.other_fields, 'to_alipay_dict'):
                params['other_fields'] = self.other_fields.to_alipay_dict()
            else:
                params['other_fields'] = self.other_fields
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.submit_time:
            if hasattr(self.submit_time, 'to_alipay_dict'):
                params['submit_time'] = self.submit_time.to_alipay_dict()
            else:
                params['submit_time'] = self.submit_time
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
        o = RightsFormItemValues()
        if 'crn' in d:
            o.crn = d['crn']
        if 'email' in d:
            o.email = d['email']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'legal_person' in d:
            o.legal_person = d['legal_person']
        if 'other_fields' in d:
            o.other_fields = d['other_fields']
        if 'phone' in d:
            o.phone = d['phone']
        if 'submit_time' in d:
            o.submit_time = d['submit_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


