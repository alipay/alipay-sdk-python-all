#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GFAOpenAPIParticipantInfo(object):

    def __init__(self):
        self._account_no = None
        self._account_type = None
        self._inst_code = None
        self._ip_role_id = None
        self._properties = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, value):
        self._properties = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.properties:
            if hasattr(self.properties, 'to_alipay_dict'):
                params['properties'] = self.properties.to_alipay_dict()
            else:
                params['properties'] = self.properties
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GFAOpenAPIParticipantInfo()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'properties' in d:
            o.properties = d['properties']
        return o


