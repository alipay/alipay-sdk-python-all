#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PolicyPersonInfo(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._name = None
        self._person_type = None
        self._phone = None
        self._relation_to_holder = None

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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def person_type(self):
        return self._person_type

    @person_type.setter
    def person_type(self, value):
        self._person_type = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def relation_to_holder(self):
        return self._relation_to_holder

    @relation_to_holder.setter
    def relation_to_holder(self, value):
        self._relation_to_holder = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.person_type:
            if hasattr(self.person_type, 'to_alipay_dict'):
                params['person_type'] = self.person_type.to_alipay_dict()
            else:
                params['person_type'] = self.person_type
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.relation_to_holder:
            if hasattr(self.relation_to_holder, 'to_alipay_dict'):
                params['relation_to_holder'] = self.relation_to_holder.to_alipay_dict()
            else:
                params['relation_to_holder'] = self.relation_to_holder
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PolicyPersonInfo()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'name' in d:
            o.name = d['name']
        if 'person_type' in d:
            o.person_type = d['person_type']
        if 'phone' in d:
            o.phone = d['phone']
        if 'relation_to_holder' in d:
            o.relation_to_holder = d['relation_to_holder']
        return o


