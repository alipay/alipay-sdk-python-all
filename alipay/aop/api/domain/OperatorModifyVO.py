#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperatorContactVO import OperatorContactVO


class OperatorModifyVO(object):

    def __init__(self):
        self._contacts = None
        self._name = None
        self._role_codes = None

    @property
    def contacts(self):
        return self._contacts

    @contacts.setter
    def contacts(self, value):
        if isinstance(value, list):
            self._contacts = list()
            for i in value:
                if isinstance(i, OperatorContactVO):
                    self._contacts.append(i)
                else:
                    self._contacts.append(OperatorContactVO.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def role_codes(self):
        return self._role_codes

    @role_codes.setter
    def role_codes(self, value):
        if isinstance(value, list):
            self._role_codes = list()
            for i in value:
                self._role_codes.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.contacts:
            if isinstance(self.contacts, list):
                for i in range(0, len(self.contacts)):
                    element = self.contacts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contacts[i] = element.to_alipay_dict()
            if hasattr(self.contacts, 'to_alipay_dict'):
                params['contacts'] = self.contacts.to_alipay_dict()
            else:
                params['contacts'] = self.contacts
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.role_codes:
            if isinstance(self.role_codes, list):
                for i in range(0, len(self.role_codes)):
                    element = self.role_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.role_codes[i] = element.to_alipay_dict()
            if hasattr(self.role_codes, 'to_alipay_dict'):
                params['role_codes'] = self.role_codes.to_alipay_dict()
            else:
                params['role_codes'] = self.role_codes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OperatorModifyVO()
        if 'contacts' in d:
            o.contacts = d['contacts']
        if 'name' in d:
            o.name = d['name']
        if 'role_codes' in d:
            o.role_codes = d['role_codes']
        return o


