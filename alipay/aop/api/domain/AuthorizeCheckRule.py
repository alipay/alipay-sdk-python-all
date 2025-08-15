#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AuthorizeCheckRule(object):

    def __init__(self):
        self._enterprise_cert_no = None
        self._partner_user_type_limit = None
        self._principal_user_type_limit = None

    @property
    def enterprise_cert_no(self):
        return self._enterprise_cert_no

    @enterprise_cert_no.setter
    def enterprise_cert_no(self, value):
        self._enterprise_cert_no = value
    @property
    def partner_user_type_limit(self):
        return self._partner_user_type_limit

    @partner_user_type_limit.setter
    def partner_user_type_limit(self, value):
        self._partner_user_type_limit = value
    @property
    def principal_user_type_limit(self):
        return self._principal_user_type_limit

    @principal_user_type_limit.setter
    def principal_user_type_limit(self, value):
        self._principal_user_type_limit = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_cert_no:
            if hasattr(self.enterprise_cert_no, 'to_alipay_dict'):
                params['enterprise_cert_no'] = self.enterprise_cert_no.to_alipay_dict()
            else:
                params['enterprise_cert_no'] = self.enterprise_cert_no
        if self.partner_user_type_limit:
            if hasattr(self.partner_user_type_limit, 'to_alipay_dict'):
                params['partner_user_type_limit'] = self.partner_user_type_limit.to_alipay_dict()
            else:
                params['partner_user_type_limit'] = self.partner_user_type_limit
        if self.principal_user_type_limit:
            if hasattr(self.principal_user_type_limit, 'to_alipay_dict'):
                params['principal_user_type_limit'] = self.principal_user_type_limit.to_alipay_dict()
            else:
                params['principal_user_type_limit'] = self.principal_user_type_limit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthorizeCheckRule()
        if 'enterprise_cert_no' in d:
            o.enterprise_cert_no = d['enterprise_cert_no']
        if 'partner_user_type_limit' in d:
            o.partner_user_type_limit = d['partner_user_type_limit']
        if 'principal_user_type_limit' in d:
            o.principal_user_type_limit = d['principal_user_type_limit']
        return o


