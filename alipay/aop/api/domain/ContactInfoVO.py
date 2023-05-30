#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContactInfoVO(object):

    def __init__(self):
        self._contact_name = None
        self._encryption_content = None
        self._phone_number = None

    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def encryption_content(self):
        return self._encryption_content

    @encryption_content.setter
    def encryption_content(self, value):
        self._encryption_content = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.encryption_content:
            if hasattr(self.encryption_content, 'to_alipay_dict'):
                params['encryption_content'] = self.encryption_content.to_alipay_dict()
            else:
                params['encryption_content'] = self.encryption_content
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContactInfoVO()
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'encryption_content' in d:
            o.encryption_content = d['encryption_content']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        return o


