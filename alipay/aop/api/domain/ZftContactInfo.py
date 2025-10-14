#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZftContactInfo(object):

    def __init__(self):
        self._email = None
        self._id_card_no = None
        self._mobile = None
        self._name = None
        self._phone = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def id_card_no(self):
        return self._id_card_no

    @id_card_no.setter
    def id_card_no(self, value):
        self._id_card_no = value
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
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.id_card_no:
            if hasattr(self.id_card_no, 'to_alipay_dict'):
                params['id_card_no'] = self.id_card_no.to_alipay_dict()
            else:
                params['id_card_no'] = self.id_card_no
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
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZftContactInfo()
        if 'email' in d:
            o.email = d['email']
        if 'id_card_no' in d:
            o.id_card_no = d['id_card_no']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        if 'phone' in d:
            o.phone = d['phone']
        return o


