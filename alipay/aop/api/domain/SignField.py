#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Signer import Signer


class SignField(object):

    def __init__(self):
        self._auto_execute = None
        self._signer = None
        self._struct_key = None

    @property
    def auto_execute(self):
        return self._auto_execute

    @auto_execute.setter
    def auto_execute(self, value):
        self._auto_execute = value
    @property
    def signer(self):
        return self._signer

    @signer.setter
    def signer(self, value):
        if isinstance(value, Signer):
            self._signer = value
        else:
            self._signer = Signer.from_alipay_dict(value)
    @property
    def struct_key(self):
        return self._struct_key

    @struct_key.setter
    def struct_key(self, value):
        self._struct_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.auto_execute:
            if hasattr(self.auto_execute, 'to_alipay_dict'):
                params['auto_execute'] = self.auto_execute.to_alipay_dict()
            else:
                params['auto_execute'] = self.auto_execute
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
        o = SignField()
        if 'auto_execute' in d:
            o.auto_execute = d['auto_execute']
        if 'signer' in d:
            o.signer = d['signer']
        if 'struct_key' in d:
            o.struct_key = d['struct_key']
        return o


