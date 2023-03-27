#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrincipalInfoDTO(object):

    def __init__(self):
        self._identity = None
        self._identity_name = None
        self._identity_type = None

    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def identity_name(self):
        return self._identity_name

    @identity_name.setter
    def identity_name(self, value):
        self._identity_name = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.identity_name:
            if hasattr(self.identity_name, 'to_alipay_dict'):
                params['identity_name'] = self.identity_name.to_alipay_dict()
            else:
                params['identity_name'] = self.identity_name
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrincipalInfoDTO()
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_name' in d:
            o.identity_name = d['identity_name']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        return o


