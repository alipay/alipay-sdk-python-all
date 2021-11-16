#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PaymentAddress import PaymentAddress


class Shipping(object):

    def __init__(self):
        self._receiver_address = None
        self._receiver_email = None
        self._receiver_name = None
        self._receiver_phone_no = None

    @property
    def receiver_address(self):
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, value):
        if isinstance(value, PaymentAddress):
            self._receiver_address = value
        else:
            self._receiver_address = PaymentAddress.from_alipay_dict(value)
    @property
    def receiver_email(self):
        return self._receiver_email

    @receiver_email.setter
    def receiver_email(self, value):
        self._receiver_email = value
    @property
    def receiver_name(self):
        return self._receiver_name

    @receiver_name.setter
    def receiver_name(self, value):
        self._receiver_name = value
    @property
    def receiver_phone_no(self):
        return self._receiver_phone_no

    @receiver_phone_no.setter
    def receiver_phone_no(self, value):
        self._receiver_phone_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.receiver_address:
            if hasattr(self.receiver_address, 'to_alipay_dict'):
                params['receiver_address'] = self.receiver_address.to_alipay_dict()
            else:
                params['receiver_address'] = self.receiver_address
        if self.receiver_email:
            if hasattr(self.receiver_email, 'to_alipay_dict'):
                params['receiver_email'] = self.receiver_email.to_alipay_dict()
            else:
                params['receiver_email'] = self.receiver_email
        if self.receiver_name:
            if hasattr(self.receiver_name, 'to_alipay_dict'):
                params['receiver_name'] = self.receiver_name.to_alipay_dict()
            else:
                params['receiver_name'] = self.receiver_name
        if self.receiver_phone_no:
            if hasattr(self.receiver_phone_no, 'to_alipay_dict'):
                params['receiver_phone_no'] = self.receiver_phone_no.to_alipay_dict()
            else:
                params['receiver_phone_no'] = self.receiver_phone_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Shipping()
        if 'receiver_address' in d:
            o.receiver_address = d['receiver_address']
        if 'receiver_email' in d:
            o.receiver_email = d['receiver_email']
        if 'receiver_name' in d:
            o.receiver_name = d['receiver_name']
        if 'receiver_phone_no' in d:
            o.receiver_phone_no = d['receiver_phone_no']
        return o


