#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccPayeeInfo(object):

    def __init__(self):
        self._payee_account = None
        self._payee_name = None

    @property
    def payee_account(self):
        return self._payee_account

    @payee_account.setter
    def payee_account(self, value):
        self._payee_account = value
    @property
    def payee_name(self):
        return self._payee_name

    @payee_name.setter
    def payee_name(self, value):
        self._payee_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.payee_account:
            if hasattr(self.payee_account, 'to_alipay_dict'):
                params['payee_account'] = self.payee_account.to_alipay_dict()
            else:
                params['payee_account'] = self.payee_account
        if self.payee_name:
            if hasattr(self.payee_name, 'to_alipay_dict'):
                params['payee_name'] = self.payee_name.to_alipay_dict()
            else:
                params['payee_name'] = self.payee_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccPayeeInfo()
        if 'payee_account' in d:
            o.payee_account = d['payee_account']
        if 'payee_name' in d:
            o.payee_name = d['payee_name']
        return o


