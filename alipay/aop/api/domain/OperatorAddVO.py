#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperatorContactVO import OperatorContactVO


class OperatorAddVO(object):

    def __init__(self):
        self._biz_type = None
        self._contacts = None
        self._logon_id = None
        self._logon_id_type = None
        self._logon_password = None
        self._main_ip_role_id = None
        self._main_ip_role_type = None
        self._name = None
        self._nick_name = None
        self._tenant_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def contacts(self):
        return self._contacts

    @contacts.setter
    def contacts(self, value):
        if isinstance(value, list):
            self._contacts = list()
            for i in value:
                if isinstance(i, OperatorContactVO):
                    self._contacts.append(i)
                else:
                    self._contacts.append(OperatorContactVO.from_alipay_dict(i))
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def logon_id_type(self):
        return self._logon_id_type

    @logon_id_type.setter
    def logon_id_type(self, value):
        self._logon_id_type = value
    @property
    def logon_password(self):
        return self._logon_password

    @logon_password.setter
    def logon_password(self, value):
        self._logon_password = value
    @property
    def main_ip_role_id(self):
        return self._main_ip_role_id

    @main_ip_role_id.setter
    def main_ip_role_id(self, value):
        self._main_ip_role_id = value
    @property
    def main_ip_role_type(self):
        return self._main_ip_role_type

    @main_ip_role_type.setter
    def main_ip_role_type(self, value):
        self._main_ip_role_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.contacts:
            if isinstance(self.contacts, list):
                for i in range(0, len(self.contacts)):
                    element = self.contacts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contacts[i] = element.to_alipay_dict()
            if hasattr(self.contacts, 'to_alipay_dict'):
                params['contacts'] = self.contacts.to_alipay_dict()
            else:
                params['contacts'] = self.contacts
        if self.logon_id:
            if hasattr(self.logon_id, 'to_alipay_dict'):
                params['logon_id'] = self.logon_id.to_alipay_dict()
            else:
                params['logon_id'] = self.logon_id
        if self.logon_id_type:
            if hasattr(self.logon_id_type, 'to_alipay_dict'):
                params['logon_id_type'] = self.logon_id_type.to_alipay_dict()
            else:
                params['logon_id_type'] = self.logon_id_type
        if self.logon_password:
            if hasattr(self.logon_password, 'to_alipay_dict'):
                params['logon_password'] = self.logon_password.to_alipay_dict()
            else:
                params['logon_password'] = self.logon_password
        if self.main_ip_role_id:
            if hasattr(self.main_ip_role_id, 'to_alipay_dict'):
                params['main_ip_role_id'] = self.main_ip_role_id.to_alipay_dict()
            else:
                params['main_ip_role_id'] = self.main_ip_role_id
        if self.main_ip_role_type:
            if hasattr(self.main_ip_role_type, 'to_alipay_dict'):
                params['main_ip_role_type'] = self.main_ip_role_type.to_alipay_dict()
            else:
                params['main_ip_role_type'] = self.main_ip_role_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OperatorAddVO()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'contacts' in d:
            o.contacts = d['contacts']
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'logon_id_type' in d:
            o.logon_id_type = d['logon_id_type']
        if 'logon_password' in d:
            o.logon_password = d['logon_password']
        if 'main_ip_role_id' in d:
            o.main_ip_role_id = d['main_ip_role_id']
        if 'main_ip_role_type' in d:
            o.main_ip_role_type = d['main_ip_role_type']
        if 'name' in d:
            o.name = d['name']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


