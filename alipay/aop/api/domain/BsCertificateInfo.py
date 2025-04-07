#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BsCertificateInfo(object):

    def __init__(self):
        self._certificate_img = None
        self._certificate_type = None

    @property
    def certificate_img(self):
        return self._certificate_img

    @certificate_img.setter
    def certificate_img(self, value):
        self._certificate_img = value
    @property
    def certificate_type(self):
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, value):
        self._certificate_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_img:
            if hasattr(self.certificate_img, 'to_alipay_dict'):
                params['certificate_img'] = self.certificate_img.to_alipay_dict()
            else:
                params['certificate_img'] = self.certificate_img
        if self.certificate_type:
            if hasattr(self.certificate_type, 'to_alipay_dict'):
                params['certificate_type'] = self.certificate_type.to_alipay_dict()
            else:
                params['certificate_type'] = self.certificate_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BsCertificateInfo()
        if 'certificate_img' in d:
            o.certificate_img = d['certificate_img']
        if 'certificate_type' in d:
            o.certificate_type = d['certificate_type']
        return o


