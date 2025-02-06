#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbasePassportCreateModel(object):

    def __init__(self):
        self._credential = None
        self._email = None
        self._entity_role_type = None
        self._mobile_phone = None

    @property
    def credential(self):
        return self._credential

    @credential.setter
    def credential(self, value):
        self._credential = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def entity_role_type(self):
        return self._entity_role_type

    @entity_role_type.setter
    def entity_role_type(self, value):
        self._entity_role_type = value
    @property
    def mobile_phone(self):
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        self._mobile_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.credential:
            if hasattr(self.credential, 'to_alipay_dict'):
                params['credential'] = self.credential.to_alipay_dict()
            else:
                params['credential'] = self.credential
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.entity_role_type:
            if hasattr(self.entity_role_type, 'to_alipay_dict'):
                params['entity_role_type'] = self.entity_role_type.to_alipay_dict()
            else:
                params['entity_role_type'] = self.entity_role_type
        if self.mobile_phone:
            if hasattr(self.mobile_phone, 'to_alipay_dict'):
                params['mobile_phone'] = self.mobile_phone.to_alipay_dict()
            else:
                params['mobile_phone'] = self.mobile_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbasePassportCreateModel()
        if 'credential' in d:
            o.credential = d['credential']
        if 'email' in d:
            o.email = d['email']
        if 'entity_role_type' in d:
            o.entity_role_type = d['entity_role_type']
        if 'mobile_phone' in d:
            o.mobile_phone = d['mobile_phone']
        return o


