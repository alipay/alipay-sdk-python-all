#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AntArchiveIdentityCertificate import AntArchiveIdentityCertificate


class AlipayUserAntarchiveCustrelationAddModel(object):

    def __init__(self):
        self._cust_id = None
        self._identity_certificate = None

    @property
    def cust_id(self):
        return self._cust_id

    @cust_id.setter
    def cust_id(self, value):
        self._cust_id = value
    @property
    def identity_certificate(self):
        return self._identity_certificate

    @identity_certificate.setter
    def identity_certificate(self, value):
        if isinstance(value, AntArchiveIdentityCertificate):
            self._identity_certificate = value
        else:
            self._identity_certificate = AntArchiveIdentityCertificate.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.cust_id:
            if hasattr(self.cust_id, 'to_alipay_dict'):
                params['cust_id'] = self.cust_id.to_alipay_dict()
            else:
                params['cust_id'] = self.cust_id
        if self.identity_certificate:
            if hasattr(self.identity_certificate, 'to_alipay_dict'):
                params['identity_certificate'] = self.identity_certificate.to_alipay_dict()
            else:
                params['identity_certificate'] = self.identity_certificate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAntarchiveCustrelationAddModel()
        if 'cust_id' in d:
            o.cust_id = d['cust_id']
        if 'identity_certificate' in d:
            o.identity_certificate = d['identity_certificate']
        return o


