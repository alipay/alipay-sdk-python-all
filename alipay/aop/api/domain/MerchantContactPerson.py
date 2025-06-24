#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantCertificateInfo import MerchantCertificateInfo


class MerchantContactPerson(object):

    def __init__(self):
        self._certificate_info = None
        self._name = None
        self._type = None

    @property
    def certificate_info(self):
        return self._certificate_info

    @certificate_info.setter
    def certificate_info(self, value):
        if isinstance(value, MerchantCertificateInfo):
            self._certificate_info = value
        else:
            self._certificate_info = MerchantCertificateInfo.from_alipay_dict(value)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_info:
            if hasattr(self.certificate_info, 'to_alipay_dict'):
                params['certificate_info'] = self.certificate_info.to_alipay_dict()
            else:
                params['certificate_info'] = self.certificate_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
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
        o = MerchantContactPerson()
        if 'certificate_info' in d:
            o.certificate_info = d['certificate_info']
        if 'name' in d:
            o.name = d['name']
        if 'type' in d:
            o.type = d['type']
        return o


