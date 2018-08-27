#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContactInfo(object):

    def __init__(self):
        self._email = None
        self._id_card_no = None
        self._mobile = None
        self._name = None
        self._phone = None
        self._tag = None
        self._type = None

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
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        if isinstance(value, list):
            self._tag = list()
            for i in value:
                self._tag.append(i)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


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
        if self.tag:
            if isinstance(self.tag, list):
                for i in range(0, len(self.tag)):
                    element = self.tag[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag[i] = element.to_alipay_dict()
            if hasattr(self.tag, 'to_alipay_dict'):
                params['tag'] = self.tag.to_alipay_dict()
            else:
                params['tag'] = self.tag
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContactInfo()
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
        if 'tag' in d:
            o.tag = d['tag']
        if 'type' in d:
            o.type = d['type']
        return o


