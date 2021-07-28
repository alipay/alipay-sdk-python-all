#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HealthCard(object):

    def __init__(self):
        self._birthday = None
        self._cert_no = None
        self._health_card_no = None
        self._name = None
        self._sex = None

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def health_card_no(self):
        return self._health_card_no

    @health_card_no.setter
    def health_card_no(self, value):
        self._health_card_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value


    def to_alipay_dict(self):
        params = dict()
        if self.birthday:
            if hasattr(self.birthday, 'to_alipay_dict'):
                params['birthday'] = self.birthday.to_alipay_dict()
            else:
                params['birthday'] = self.birthday
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.health_card_no:
            if hasattr(self.health_card_no, 'to_alipay_dict'):
                params['health_card_no'] = self.health_card_no.to_alipay_dict()
            else:
                params['health_card_no'] = self.health_card_no
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.sex:
            if hasattr(self.sex, 'to_alipay_dict'):
                params['sex'] = self.sex.to_alipay_dict()
            else:
                params['sex'] = self.sex
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HealthCard()
        if 'birthday' in d:
            o.birthday = d['birthday']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'health_card_no' in d:
            o.health_card_no = d['health_card_no']
        if 'name' in d:
            o.name = d['name']
        if 'sex' in d:
            o.sex = d['sex']
        return o


