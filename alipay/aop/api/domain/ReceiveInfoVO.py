#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReceiveInfoVO(object):

    def __init__(self):
        self._mail_address = None
        self._mail_name = None
        self._mail_phone = None
        self._receive_email = None

    @property
    def mail_address(self):
        return self._mail_address

    @mail_address.setter
    def mail_address(self, value):
        self._mail_address = value
    @property
    def mail_name(self):
        return self._mail_name

    @mail_name.setter
    def mail_name(self, value):
        self._mail_name = value
    @property
    def mail_phone(self):
        return self._mail_phone

    @mail_phone.setter
    def mail_phone(self, value):
        self._mail_phone = value
    @property
    def receive_email(self):
        return self._receive_email

    @receive_email.setter
    def receive_email(self, value):
        self._receive_email = value


    def to_alipay_dict(self):
        params = dict()
        if self.mail_address:
            if hasattr(self.mail_address, 'to_alipay_dict'):
                params['mail_address'] = self.mail_address.to_alipay_dict()
            else:
                params['mail_address'] = self.mail_address
        if self.mail_name:
            if hasattr(self.mail_name, 'to_alipay_dict'):
                params['mail_name'] = self.mail_name.to_alipay_dict()
            else:
                params['mail_name'] = self.mail_name
        if self.mail_phone:
            if hasattr(self.mail_phone, 'to_alipay_dict'):
                params['mail_phone'] = self.mail_phone.to_alipay_dict()
            else:
                params['mail_phone'] = self.mail_phone
        if self.receive_email:
            if hasattr(self.receive_email, 'to_alipay_dict'):
                params['receive_email'] = self.receive_email.to_alipay_dict()
            else:
                params['receive_email'] = self.receive_email
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReceiveInfoVO()
        if 'mail_address' in d:
            o.mail_address = d['mail_address']
        if 'mail_name' in d:
            o.mail_name = d['mail_name']
        if 'mail_phone' in d:
            o.mail_phone = d['mail_phone']
        if 'receive_email' in d:
            o.receive_email = d['receive_email']
        return o


