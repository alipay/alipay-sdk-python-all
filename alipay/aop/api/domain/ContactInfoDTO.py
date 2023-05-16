#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContactInfoDTO(object):

    def __init__(self):
        self._contact_name = None
        self._phone_number = None

    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
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
        o = ContactInfoDTO()
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        return o


