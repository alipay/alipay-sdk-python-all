#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WalletExternalAccount(object):

    def __init__(self):
        self._external_account_no = None
        self._external_account_type = None
        self._status = None

    @property
    def external_account_no(self):
        return self._external_account_no

    @external_account_no.setter
    def external_account_no(self, value):
        self._external_account_no = value
    @property
    def external_account_type(self):
        return self._external_account_type

    @external_account_type.setter
    def external_account_type(self, value):
        self._external_account_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_account_no:
            if hasattr(self.external_account_no, 'to_alipay_dict'):
                params['external_account_no'] = self.external_account_no.to_alipay_dict()
            else:
                params['external_account_no'] = self.external_account_no
        if self.external_account_type:
            if hasattr(self.external_account_type, 'to_alipay_dict'):
                params['external_account_type'] = self.external_account_type.to_alipay_dict()
            else:
                params['external_account_type'] = self.external_account_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WalletExternalAccount()
        if 'external_account_no' in d:
            o.external_account_no = d['external_account_no']
        if 'external_account_type' in d:
            o.external_account_type = d['external_account_type']
        if 'status' in d:
            o.status = d['status']
        return o


