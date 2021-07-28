#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertificateInfo(object):

    def __init__(self):
        self._certificate_name = None
        self._certificate_number = None

    @property
    def certificate_name(self):
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, value):
        self._certificate_name = value
    @property
    def certificate_number(self):
        return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, value):
        self._certificate_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_name:
            if hasattr(self.certificate_name, 'to_alipay_dict'):
                params['certificate_name'] = self.certificate_name.to_alipay_dict()
            else:
                params['certificate_name'] = self.certificate_name
        if self.certificate_number:
            if hasattr(self.certificate_number, 'to_alipay_dict'):
                params['certificate_number'] = self.certificate_number.to_alipay_dict()
            else:
                params['certificate_number'] = self.certificate_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificateInfo()
        if 'certificate_name' in d:
            o.certificate_name = d['certificate_name']
        if 'certificate_number' in d:
            o.certificate_number = d['certificate_number']
        return o


