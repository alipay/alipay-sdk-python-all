#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditUserBankcardBindModel(object):

    def __init__(self):
        self._account_name = None
        self._admin_type = None
        self._admin_user_id = None
        self._bankcard_no = None
        self._cert_no = None
        self._cert_type = None
        self._fip_code = None
        self._ip_id = None
        self._ip_role_id = None
        self._purpose = None
        self._request_id = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def admin_type(self):
        return self._admin_type

    @admin_type.setter
    def admin_type(self, value):
        self._admin_type = value
    @property
    def admin_user_id(self):
        return self._admin_user_id

    @admin_user_id.setter
    def admin_user_id(self, value):
        self._admin_user_id = value
    @property
    def bankcard_no(self):
        return self._bankcard_no

    @bankcard_no.setter
    def bankcard_no(self, value):
        self._bankcard_no = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def fip_code(self):
        return self._fip_code

    @fip_code.setter
    def fip_code(self, value):
        self._fip_code = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def purpose(self):
        return self._purpose

    @purpose.setter
    def purpose(self, value):
        self._purpose = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.admin_type:
            if hasattr(self.admin_type, 'to_alipay_dict'):
                params['admin_type'] = self.admin_type.to_alipay_dict()
            else:
                params['admin_type'] = self.admin_type
        if self.admin_user_id:
            if hasattr(self.admin_user_id, 'to_alipay_dict'):
                params['admin_user_id'] = self.admin_user_id.to_alipay_dict()
            else:
                params['admin_user_id'] = self.admin_user_id
        if self.bankcard_no:
            if hasattr(self.bankcard_no, 'to_alipay_dict'):
                params['bankcard_no'] = self.bankcard_no.to_alipay_dict()
            else:
                params['bankcard_no'] = self.bankcard_no
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.fip_code:
            if hasattr(self.fip_code, 'to_alipay_dict'):
                params['fip_code'] = self.fip_code.to_alipay_dict()
            else:
                params['fip_code'] = self.fip_code
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.purpose:
            if hasattr(self.purpose, 'to_alipay_dict'):
                params['purpose'] = self.purpose.to_alipay_dict()
            else:
                params['purpose'] = self.purpose
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditUserBankcardBindModel()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'admin_type' in d:
            o.admin_type = d['admin_type']
        if 'admin_user_id' in d:
            o.admin_user_id = d['admin_user_id']
        if 'bankcard_no' in d:
            o.bankcard_no = d['bankcard_no']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'fip_code' in d:
            o.fip_code = d['fip_code']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'purpose' in d:
            o.purpose = d['purpose']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


