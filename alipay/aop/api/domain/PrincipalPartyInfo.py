#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrincipalPartyInfo(object):

    def __init__(self):
        self._principal_account_no = None
        self._principal_cert_no = None
        self._principal_name = None

    @property
    def principal_account_no(self):
        return self._principal_account_no

    @principal_account_no.setter
    def principal_account_no(self, value):
        self._principal_account_no = value
    @property
    def principal_cert_no(self):
        return self._principal_cert_no

    @principal_cert_no.setter
    def principal_cert_no(self, value):
        self._principal_cert_no = value
    @property
    def principal_name(self):
        return self._principal_name

    @principal_name.setter
    def principal_name(self, value):
        self._principal_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.principal_account_no:
            if hasattr(self.principal_account_no, 'to_alipay_dict'):
                params['principal_account_no'] = self.principal_account_no.to_alipay_dict()
            else:
                params['principal_account_no'] = self.principal_account_no
        if self.principal_cert_no:
            if hasattr(self.principal_cert_no, 'to_alipay_dict'):
                params['principal_cert_no'] = self.principal_cert_no.to_alipay_dict()
            else:
                params['principal_cert_no'] = self.principal_cert_no
        if self.principal_name:
            if hasattr(self.principal_name, 'to_alipay_dict'):
                params['principal_name'] = self.principal_name.to_alipay_dict()
            else:
                params['principal_name'] = self.principal_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrincipalPartyInfo()
        if 'principal_account_no' in d:
            o.principal_account_no = d['principal_account_no']
        if 'principal_cert_no' in d:
            o.principal_cert_no = d['principal_cert_no']
        if 'principal_name' in d:
            o.principal_name = d['principal_name']
        return o


