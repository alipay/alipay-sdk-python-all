#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CloudResumeCertificateInfo(object):

    def __init__(self):
        self._certificate_name = None

    @property
    def certificate_name(self):
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, value):
        self._certificate_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_name:
            if hasattr(self.certificate_name, 'to_alipay_dict'):
                params['certificate_name'] = self.certificate_name.to_alipay_dict()
            else:
                params['certificate_name'] = self.certificate_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CloudResumeCertificateInfo()
        if 'certificate_name' in d:
            o.certificate_name = d['certificate_name']
        return o


