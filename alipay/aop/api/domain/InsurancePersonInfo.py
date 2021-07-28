#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsurancePersonInfo(object):

    def __init__(self):
        self._card_code = None
        self._card_type = None
        self._contact_info = None
        self._name = None

    @property
    def card_code(self):
        return self._card_code

    @card_code.setter
    def card_code(self, value):
        self._card_code = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        self._contact_info = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_code:
            if hasattr(self.card_code, 'to_alipay_dict'):
                params['card_code'] = self.card_code.to_alipay_dict()
            else:
                params['card_code'] = self.card_code
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.contact_info:
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsurancePersonInfo()
        if 'card_code' in d:
            o.card_code = d['card_code']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'name' in d:
            o.name = d['name']
        return o


