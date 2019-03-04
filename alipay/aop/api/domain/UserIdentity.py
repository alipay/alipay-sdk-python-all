#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserIdentity(object):

    def __init__(self):
        self._identity = None
        self._issuer = None
        self._type = None

    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def issuer(self):
        return self._issuer

    @issuer.setter
    def issuer(self, value):
        self._issuer = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.issuer:
            if hasattr(self.issuer, 'to_alipay_dict'):
                params['issuer'] = self.issuer.to_alipay_dict()
            else:
                params['issuer'] = self.issuer
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
        o = UserIdentity()
        if 'identity' in d:
            o.identity = d['identity']
        if 'issuer' in d:
            o.issuer = d['issuer']
        if 'type' in d:
            o.type = d['type']
        return o


