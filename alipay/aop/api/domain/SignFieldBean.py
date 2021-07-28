#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SignerBean import SignerBean


class SignFieldBean(object):

    def __init__(self):
        self._sign_field_type = None
        self._signer = None
        self._struct_key = None

    @property
    def sign_field_type(self):
        return self._sign_field_type

    @sign_field_type.setter
    def sign_field_type(self, value):
        self._sign_field_type = value
    @property
    def signer(self):
        return self._signer

    @signer.setter
    def signer(self, value):
        if isinstance(value, SignerBean):
            self._signer = value
        else:
            self._signer = SignerBean.from_alipay_dict(value)
    @property
    def struct_key(self):
        return self._struct_key

    @struct_key.setter
    def struct_key(self, value):
        self._struct_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.sign_field_type:
            if hasattr(self.sign_field_type, 'to_alipay_dict'):
                params['sign_field_type'] = self.sign_field_type.to_alipay_dict()
            else:
                params['sign_field_type'] = self.sign_field_type
        if self.signer:
            if hasattr(self.signer, 'to_alipay_dict'):
                params['signer'] = self.signer.to_alipay_dict()
            else:
                params['signer'] = self.signer
        if self.struct_key:
            if hasattr(self.struct_key, 'to_alipay_dict'):
                params['struct_key'] = self.struct_key.to_alipay_dict()
            else:
                params['struct_key'] = self.struct_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignFieldBean()
        if 'sign_field_type' in d:
            o.sign_field_type = d['sign_field_type']
        if 'signer' in d:
            o.signer = d['signer']
        if 'struct_key' in d:
            o.struct_key = d['struct_key']
        return o


