#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Org import Org


class SignerBean(object):

    def __init__(self):
        self._email = None
        self._id_number = None
        self._id_type = None
        self._mobile = None
        self._name = None
        self._org = None
        self._third_party_user_id = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
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
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def org(self):
        return self._org

    @org.setter
    def org(self, value):
        if isinstance(value, Org):
            self._org = value
        else:
            self._org = Org.from_alipay_dict(value)
    @property
    def third_party_user_id(self):
        return self._third_party_user_id

    @third_party_user_id.setter
    def third_party_user_id(self, value):
        self._third_party_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
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
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.org:
            if hasattr(self.org, 'to_alipay_dict'):
                params['org'] = self.org.to_alipay_dict()
            else:
                params['org'] = self.org
        if self.third_party_user_id:
            if hasattr(self.third_party_user_id, 'to_alipay_dict'):
                params['third_party_user_id'] = self.third_party_user_id.to_alipay_dict()
            else:
                params['third_party_user_id'] = self.third_party_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignerBean()
        if 'email' in d:
            o.email = d['email']
        if 'id_number' in d:
            o.id_number = d['id_number']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        if 'org' in d:
            o.org = d['org']
        if 'third_party_user_id' in d:
            o.third_party_user_id = d['third_party_user_id']
        return o


