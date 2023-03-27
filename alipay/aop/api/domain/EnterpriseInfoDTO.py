#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EnterpriseInfoDTO(object):

    def __init__(self):
        self._account_id = None
        self._activate = None
        self._auth_level = None
        self._auth_status = None
        self._auth_time = None
        self._enterprise_alias = None
        self._enterprise_code = None
        self._enterprise_email = None
        self._enterprise_id = None
        self._enterprise_name = None
        self._gmt_create = None
        self._gmt_modified = None
        self._iot_group_id = None
        self._iot_logic_group_id = None
        self._platform_code = None
        self._platform_out_id = None
        self._sign_status = None
        self._status = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def activate(self):
        return self._activate

    @activate.setter
    def activate(self, value):
        self._activate = value
    @property
    def auth_level(self):
        return self._auth_level

    @auth_level.setter
    def auth_level(self, value):
        self._auth_level = value
    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value
    @property
    def auth_time(self):
        return self._auth_time

    @auth_time.setter
    def auth_time(self, value):
        self._auth_time = value
    @property
    def enterprise_alias(self):
        return self._enterprise_alias

    @enterprise_alias.setter
    def enterprise_alias(self, value):
        self._enterprise_alias = value
    @property
    def enterprise_code(self):
        return self._enterprise_code

    @enterprise_code.setter
    def enterprise_code(self, value):
        self._enterprise_code = value
    @property
    def enterprise_email(self):
        return self._enterprise_email

    @enterprise_email.setter
    def enterprise_email(self, value):
        self._enterprise_email = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def iot_group_id(self):
        return self._iot_group_id

    @iot_group_id.setter
    def iot_group_id(self, value):
        self._iot_group_id = value
    @property
    def iot_logic_group_id(self):
        return self._iot_logic_group_id

    @iot_logic_group_id.setter
    def iot_logic_group_id(self, value):
        self._iot_logic_group_id = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def platform_out_id(self):
        return self._platform_out_id

    @platform_out_id.setter
    def platform_out_id(self, value):
        self._platform_out_id = value
    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.activate:
            if hasattr(self.activate, 'to_alipay_dict'):
                params['activate'] = self.activate.to_alipay_dict()
            else:
                params['activate'] = self.activate
        if self.auth_level:
            if hasattr(self.auth_level, 'to_alipay_dict'):
                params['auth_level'] = self.auth_level.to_alipay_dict()
            else:
                params['auth_level'] = self.auth_level
        if self.auth_status:
            if hasattr(self.auth_status, 'to_alipay_dict'):
                params['auth_status'] = self.auth_status.to_alipay_dict()
            else:
                params['auth_status'] = self.auth_status
        if self.auth_time:
            if hasattr(self.auth_time, 'to_alipay_dict'):
                params['auth_time'] = self.auth_time.to_alipay_dict()
            else:
                params['auth_time'] = self.auth_time
        if self.enterprise_alias:
            if hasattr(self.enterprise_alias, 'to_alipay_dict'):
                params['enterprise_alias'] = self.enterprise_alias.to_alipay_dict()
            else:
                params['enterprise_alias'] = self.enterprise_alias
        if self.enterprise_code:
            if hasattr(self.enterprise_code, 'to_alipay_dict'):
                params['enterprise_code'] = self.enterprise_code.to_alipay_dict()
            else:
                params['enterprise_code'] = self.enterprise_code
        if self.enterprise_email:
            if hasattr(self.enterprise_email, 'to_alipay_dict'):
                params['enterprise_email'] = self.enterprise_email.to_alipay_dict()
            else:
                params['enterprise_email'] = self.enterprise_email
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = self.enterprise_name.to_alipay_dict()
            else:
                params['enterprise_name'] = self.enterprise_name
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.iot_group_id:
            if hasattr(self.iot_group_id, 'to_alipay_dict'):
                params['iot_group_id'] = self.iot_group_id.to_alipay_dict()
            else:
                params['iot_group_id'] = self.iot_group_id
        if self.iot_logic_group_id:
            if hasattr(self.iot_logic_group_id, 'to_alipay_dict'):
                params['iot_logic_group_id'] = self.iot_logic_group_id.to_alipay_dict()
            else:
                params['iot_logic_group_id'] = self.iot_logic_group_id
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.platform_out_id:
            if hasattr(self.platform_out_id, 'to_alipay_dict'):
                params['platform_out_id'] = self.platform_out_id.to_alipay_dict()
            else:
                params['platform_out_id'] = self.platform_out_id
        if self.sign_status:
            if hasattr(self.sign_status, 'to_alipay_dict'):
                params['sign_status'] = self.sign_status.to_alipay_dict()
            else:
                params['sign_status'] = self.sign_status
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
        o = EnterpriseInfoDTO()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'activate' in d:
            o.activate = d['activate']
        if 'auth_level' in d:
            o.auth_level = d['auth_level']
        if 'auth_status' in d:
            o.auth_status = d['auth_status']
        if 'auth_time' in d:
            o.auth_time = d['auth_time']
        if 'enterprise_alias' in d:
            o.enterprise_alias = d['enterprise_alias']
        if 'enterprise_code' in d:
            o.enterprise_code = d['enterprise_code']
        if 'enterprise_email' in d:
            o.enterprise_email = d['enterprise_email']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'enterprise_name' in d:
            o.enterprise_name = d['enterprise_name']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'iot_group_id' in d:
            o.iot_group_id = d['iot_group_id']
        if 'iot_logic_group_id' in d:
            o.iot_logic_group_id = d['iot_logic_group_id']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'platform_out_id' in d:
            o.platform_out_id = d['platform_out_id']
        if 'sign_status' in d:
            o.sign_status = d['sign_status']
        if 'status' in d:
            o.status = d['status']
        return o


