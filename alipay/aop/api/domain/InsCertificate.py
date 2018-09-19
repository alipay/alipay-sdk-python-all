#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsCertificate(object):

    def __init__(self):
        self._certificate_id = None
        self._certificate_type = None
        self._certificate_value = None

    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def certificate_type(self):
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, value):
        self._certificate_type = value
    @property
    def certificate_value(self):
        return self._certificate_value

    @certificate_value.setter
    def certificate_value(self, value):
        self._certificate_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.certificate_type:
            if hasattr(self.certificate_type, 'to_alipay_dict'):
                params['certificate_type'] = self.certificate_type.to_alipay_dict()
            else:
                params['certificate_type'] = self.certificate_type
        if self.certificate_value:
            if hasattr(self.certificate_value, 'to_alipay_dict'):
                params['certificate_value'] = self.certificate_value.to_alipay_dict()
            else:
                params['certificate_value'] = self.certificate_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsCertificate()
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'certificate_type' in d:
            o.certificate_type = d['certificate_type']
        if 'certificate_value' in d:
            o.certificate_value = d['certificate_value']
        return o


