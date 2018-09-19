#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MemberShip(object):

    def __init__(self):
        self._bank_card_no = None
        self._cert_no = None
        self._email = None
        self._mac = None
        self._mobile_phone_no = None

    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def mac(self):
        return self._mac

    @mac.setter
    def mac(self, value):
        self._mac = value
    @property
    def mobile_phone_no(self):
        return self._mobile_phone_no

    @mobile_phone_no.setter
    def mobile_phone_no(self, value):
        self._mobile_phone_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_card_no:
            if hasattr(self.bank_card_no, 'to_alipay_dict'):
                params['bank_card_no'] = self.bank_card_no.to_alipay_dict()
            else:
                params['bank_card_no'] = self.bank_card_no
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.mac:
            if hasattr(self.mac, 'to_alipay_dict'):
                params['mac'] = self.mac.to_alipay_dict()
            else:
                params['mac'] = self.mac
        if self.mobile_phone_no:
            if hasattr(self.mobile_phone_no, 'to_alipay_dict'):
                params['mobile_phone_no'] = self.mobile_phone_no.to_alipay_dict()
            else:
                params['mobile_phone_no'] = self.mobile_phone_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberShip()
        if 'bank_card_no' in d:
            o.bank_card_no = d['bank_card_no']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'email' in d:
            o.email = d['email']
        if 'mac' in d:
            o.mac = d['mac']
        if 'mobile_phone_no' in d:
            o.mobile_phone_no = d['mobile_phone_no']
        return o


