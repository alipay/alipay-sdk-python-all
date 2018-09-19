#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Person import Person
from alipay.aop.api.domain.Person import Person


class Injured(object):

    def __init__(self):
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._damage_type = None
        self._injured_identity = None
        self._medical_assessor = None
        self._medical_surveyor = None
        self._mobile_no = None

    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def damage_type(self):
        return self._damage_type

    @damage_type.setter
    def damage_type(self, value):
        self._damage_type = value
    @property
    def injured_identity(self):
        return self._injured_identity

    @injured_identity.setter
    def injured_identity(self, value):
        self._injured_identity = value
    @property
    def medical_assessor(self):
        return self._medical_assessor

    @medical_assessor.setter
    def medical_assessor(self, value):
        if isinstance(value, Person):
            self._medical_assessor = value
        else:
            self._medical_assessor = Person.from_alipay_dict(value)
    @property
    def medical_surveyor(self):
        return self._medical_surveyor

    @medical_surveyor.setter
    def medical_surveyor(self, value):
        if isinstance(value, Person):
            self._medical_surveyor = value
        else:
            self._medical_surveyor = Person.from_alipay_dict(value)
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.damage_type:
            if hasattr(self.damage_type, 'to_alipay_dict'):
                params['damage_type'] = self.damage_type.to_alipay_dict()
            else:
                params['damage_type'] = self.damage_type
        if self.injured_identity:
            if hasattr(self.injured_identity, 'to_alipay_dict'):
                params['injured_identity'] = self.injured_identity.to_alipay_dict()
            else:
                params['injured_identity'] = self.injured_identity
        if self.medical_assessor:
            if hasattr(self.medical_assessor, 'to_alipay_dict'):
                params['medical_assessor'] = self.medical_assessor.to_alipay_dict()
            else:
                params['medical_assessor'] = self.medical_assessor
        if self.medical_surveyor:
            if hasattr(self.medical_surveyor, 'to_alipay_dict'):
                params['medical_surveyor'] = self.medical_surveyor.to_alipay_dict()
            else:
                params['medical_surveyor'] = self.medical_surveyor
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Injured()
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'damage_type' in d:
            o.damage_type = d['damage_type']
        if 'injured_identity' in d:
            o.injured_identity = d['injured_identity']
        if 'medical_assessor' in d:
            o.medical_assessor = d['medical_assessor']
        if 'medical_surveyor' in d:
            o.medical_surveyor = d['medical_surveyor']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        return o


