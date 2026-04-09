#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdIssuerVcconfigQueryModel(object):

    def __init__(self):
        self._credential_type = None
        self._issuer_did = None

    @property
    def credential_type(self):
        return self._credential_type

    @credential_type.setter
    def credential_type(self, value):
        self._credential_type = value
    @property
    def issuer_did(self):
        return self._issuer_did

    @issuer_did.setter
    def issuer_did(self, value):
        self._issuer_did = value


    def to_alipay_dict(self):
        params = dict()
        if self.credential_type:
            if hasattr(self.credential_type, 'to_alipay_dict'):
                params['credential_type'] = self.credential_type.to_alipay_dict()
            else:
                params['credential_type'] = self.credential_type
        if self.issuer_did:
            if hasattr(self.issuer_did, 'to_alipay_dict'):
                params['issuer_did'] = self.issuer_did.to_alipay_dict()
            else:
                params['issuer_did'] = self.issuer_did
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdIssuerVcconfigQueryModel()
        if 'credential_type' in d:
            o.credential_type = d['credential_type']
        if 'issuer_did' in d:
            o.issuer_did = d['issuer_did']
        return o


