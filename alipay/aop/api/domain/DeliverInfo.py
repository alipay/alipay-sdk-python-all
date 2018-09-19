#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliverInfo(object):

    def __init__(self):
        self._recipients_address = None
        self._recipients_address_code = None
        self._recipients_name = None
        self._recipients_phone = None

    @property
    def recipients_address(self):
        return self._recipients_address

    @recipients_address.setter
    def recipients_address(self, value):
        self._recipients_address = value
    @property
    def recipients_address_code(self):
        return self._recipients_address_code

    @recipients_address_code.setter
    def recipients_address_code(self, value):
        self._recipients_address_code = value
    @property
    def recipients_name(self):
        return self._recipients_name

    @recipients_name.setter
    def recipients_name(self, value):
        self._recipients_name = value
    @property
    def recipients_phone(self):
        return self._recipients_phone

    @recipients_phone.setter
    def recipients_phone(self, value):
        self._recipients_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.recipients_address:
            if hasattr(self.recipients_address, 'to_alipay_dict'):
                params['recipients_address'] = self.recipients_address.to_alipay_dict()
            else:
                params['recipients_address'] = self.recipients_address
        if self.recipients_address_code:
            if hasattr(self.recipients_address_code, 'to_alipay_dict'):
                params['recipients_address_code'] = self.recipients_address_code.to_alipay_dict()
            else:
                params['recipients_address_code'] = self.recipients_address_code
        if self.recipients_name:
            if hasattr(self.recipients_name, 'to_alipay_dict'):
                params['recipients_name'] = self.recipients_name.to_alipay_dict()
            else:
                params['recipients_name'] = self.recipients_name
        if self.recipients_phone:
            if hasattr(self.recipients_phone, 'to_alipay_dict'):
                params['recipients_phone'] = self.recipients_phone.to_alipay_dict()
            else:
                params['recipients_phone'] = self.recipients_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliverInfo()
        if 'recipients_address' in d:
            o.recipients_address = d['recipients_address']
        if 'recipients_address_code' in d:
            o.recipients_address_code = d['recipients_address_code']
        if 'recipients_name' in d:
            o.recipients_name = d['recipients_name']
        if 'recipients_phone' in d:
            o.recipients_phone = d['recipients_phone']
        return o


