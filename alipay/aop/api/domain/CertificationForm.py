#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertificationForm(object):

    def __init__(self):
        self._certification_no = None
        self._certification_type = None

    @property
    def certification_no(self):
        return self._certification_no

    @certification_no.setter
    def certification_no(self, value):
        self._certification_no = value
    @property
    def certification_type(self):
        return self._certification_type

    @certification_type.setter
    def certification_type(self, value):
        self._certification_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.certification_no:
            if hasattr(self.certification_no, 'to_alipay_dict'):
                params['certification_no'] = self.certification_no.to_alipay_dict()
            else:
                params['certification_no'] = self.certification_no
        if self.certification_type:
            if hasattr(self.certification_type, 'to_alipay_dict'):
                params['certification_type'] = self.certification_type.to_alipay_dict()
            else:
                params['certification_type'] = self.certification_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificationForm()
        if 'certification_no' in d:
            o.certification_no = d['certification_no']
        if 'certification_type' in d:
            o.certification_type = d['certification_type']
        return o


