#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertificateObjects(object):

    def __init__(self):
        self._authority = None
        self._certificate_code = None
        self._name = None
        self._profession = None
        self._type = None

    @property
    def authority(self):
        return self._authority

    @authority.setter
    def authority(self, value):
        self._authority = value
    @property
    def certificate_code(self):
        return self._certificate_code

    @certificate_code.setter
    def certificate_code(self, value):
        self._certificate_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, value):
        self._profession = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.authority:
            if hasattr(self.authority, 'to_alipay_dict'):
                params['authority'] = self.authority.to_alipay_dict()
            else:
                params['authority'] = self.authority
        if self.certificate_code:
            if hasattr(self.certificate_code, 'to_alipay_dict'):
                params['certificate_code'] = self.certificate_code.to_alipay_dict()
            else:
                params['certificate_code'] = self.certificate_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.profession:
            if hasattr(self.profession, 'to_alipay_dict'):
                params['profession'] = self.profession.to_alipay_dict()
            else:
                params['profession'] = self.profession
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificateObjects()
        if 'authority' in d:
            o.authority = d['authority']
        if 'certificate_code' in d:
            o.certificate_code = d['certificate_code']
        if 'name' in d:
            o.name = d['name']
        if 'profession' in d:
            o.profession = d['profession']
        if 'type' in d:
            o.type = d['type']
        return o


