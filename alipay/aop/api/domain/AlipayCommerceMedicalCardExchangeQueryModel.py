#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalCardExchangeQueryModel(object):

    def __init__(self):
        self._card_no = None
        self._member_code = None
        self._phone = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def member_code(self):
        return self._member_code

    @member_code.setter
    def member_code(self, value):
        self._member_code = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.member_code:
            if hasattr(self.member_code, 'to_alipay_dict'):
                params['member_code'] = self.member_code.to_alipay_dict()
            else:
                params['member_code'] = self.member_code
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
        o = AlipayCommerceMedicalCardExchangeQueryModel()
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'member_code' in d:
            o.member_code = d['member_code']
        if 'phone' in d:
            o.phone = d['phone']
        return o


