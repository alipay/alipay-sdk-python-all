#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TransferCredential(object):

    def __init__(self):
        self._credential_no = None
        self._credential_type = None

    @property
    def credential_no(self):
        return self._credential_no

    @credential_no.setter
    def credential_no(self, value):
        self._credential_no = value
    @property
    def credential_type(self):
        return self._credential_type

    @credential_type.setter
    def credential_type(self, value):
        self._credential_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.credential_no:
            if hasattr(self.credential_no, 'to_alipay_dict'):
                params['credential_no'] = self.credential_no.to_alipay_dict()
            else:
                params['credential_no'] = self.credential_no
        if self.credential_type:
            if hasattr(self.credential_type, 'to_alipay_dict'):
                params['credential_type'] = self.credential_type.to_alipay_dict()
            else:
                params['credential_type'] = self.credential_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransferCredential()
        if 'credential_no' in d:
            o.credential_no = d['credential_no']
        if 'credential_type' in d:
            o.credential_type = d['credential_type']
        return o


