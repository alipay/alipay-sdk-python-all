#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OutOperator(object):

    def __init__(self):
        self._authed_role_codes = None
        self._contact_email = None
        self._logon_name = None
        self._operator_id = None
        self._owner_id = None

    @property
    def authed_role_codes(self):
        return self._authed_role_codes

    @authed_role_codes.setter
    def authed_role_codes(self, value):
        if isinstance(value, list):
            self._authed_role_codes = list()
            for i in value:
                self._authed_role_codes.append(i)
    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def logon_name(self):
        return self._logon_name

    @logon_name.setter
    def logon_name(self, value):
        self._logon_name = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.authed_role_codes:
            if isinstance(self.authed_role_codes, list):
                for i in range(0, len(self.authed_role_codes)):
                    element = self.authed_role_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.authed_role_codes[i] = element.to_alipay_dict()
            if hasattr(self.authed_role_codes, 'to_alipay_dict'):
                params['authed_role_codes'] = self.authed_role_codes.to_alipay_dict()
            else:
                params['authed_role_codes'] = self.authed_role_codes
        if self.contact_email:
            if hasattr(self.contact_email, 'to_alipay_dict'):
                params['contact_email'] = self.contact_email.to_alipay_dict()
            else:
                params['contact_email'] = self.contact_email
        if self.logon_name:
            if hasattr(self.logon_name, 'to_alipay_dict'):
                params['logon_name'] = self.logon_name.to_alipay_dict()
            else:
                params['logon_name'] = self.logon_name
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OutOperator()
        if 'authed_role_codes' in d:
            o.authed_role_codes = d['authed_role_codes']
        if 'contact_email' in d:
            o.contact_email = d['contact_email']
        if 'logon_name' in d:
            o.logon_name = d['logon_name']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        return o


