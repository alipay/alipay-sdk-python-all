#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InboundContactDetail(object):

    def __init__(self):
        self._contact_name = None
        self._occupation_decision = None
        self._phone_number = None

    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def occupation_decision(self):
        return self._occupation_decision

    @occupation_decision.setter
    def occupation_decision(self, value):
        self._occupation_decision = value
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
        if self.occupation_decision:
            if hasattr(self.occupation_decision, 'to_alipay_dict'):
                params['occupation_decision'] = self.occupation_decision.to_alipay_dict()
            else:
                params['occupation_decision'] = self.occupation_decision
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
        o = InboundContactDetail()
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'occupation_decision' in d:
            o.occupation_decision = d['occupation_decision']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        return o


