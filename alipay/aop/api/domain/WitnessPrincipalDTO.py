#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WitnessPrincipalDTO(object):

    def __init__(self):
        self._account_no = None
        self._principal_id = None
        self._principal_type = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def principal_type(self):
        return self._principal_type

    @principal_type.setter
    def principal_type(self, value):
        self._principal_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.principal_type:
            if hasattr(self.principal_type, 'to_alipay_dict'):
                params['principal_type'] = self.principal_type.to_alipay_dict()
            else:
                params['principal_type'] = self.principal_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WitnessPrincipalDTO()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'principal_type' in d:
            o.principal_type = d['principal_type']
        return o


