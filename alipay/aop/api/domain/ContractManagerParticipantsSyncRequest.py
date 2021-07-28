#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContractManagerParticipantsSyncRequest(object):

    def __init__(self):
        self._name = None
        self._principal_name = None
        self._principal_type = None
        self._role = None
        self._sign_status = None
        self._sign_time = None
        self._user_ids = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def principal_name(self):
        return self._principal_name

    @principal_name.setter
    def principal_name(self, value):
        self._principal_name = value
    @property
    def principal_type(self):
        return self._principal_type

    @principal_type.setter
    def principal_type(self, value):
        self._principal_type = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value
    @property
    def user_ids(self):
        return self._user_ids

    @user_ids.setter
    def user_ids(self, value):
        if isinstance(value, list):
            self._user_ids = list()
            for i in value:
                self._user_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.principal_name:
            if hasattr(self.principal_name, 'to_alipay_dict'):
                params['principal_name'] = self.principal_name.to_alipay_dict()
            else:
                params['principal_name'] = self.principal_name
        if self.principal_type:
            if hasattr(self.principal_type, 'to_alipay_dict'):
                params['principal_type'] = self.principal_type.to_alipay_dict()
            else:
                params['principal_type'] = self.principal_type
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.sign_status:
            if hasattr(self.sign_status, 'to_alipay_dict'):
                params['sign_status'] = self.sign_status.to_alipay_dict()
            else:
                params['sign_status'] = self.sign_status
        if self.sign_time:
            if hasattr(self.sign_time, 'to_alipay_dict'):
                params['sign_time'] = self.sign_time.to_alipay_dict()
            else:
                params['sign_time'] = self.sign_time
        if self.user_ids:
            if isinstance(self.user_ids, list):
                for i in range(0, len(self.user_ids)):
                    element = self.user_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_ids[i] = element.to_alipay_dict()
            if hasattr(self.user_ids, 'to_alipay_dict'):
                params['user_ids'] = self.user_ids.to_alipay_dict()
            else:
                params['user_ids'] = self.user_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractManagerParticipantsSyncRequest()
        if 'name' in d:
            o.name = d['name']
        if 'principal_name' in d:
            o.principal_name = d['principal_name']
        if 'principal_type' in d:
            o.principal_type = d['principal_type']
        if 'role' in d:
            o.role = d['role']
        if 'sign_status' in d:
            o.sign_status = d['sign_status']
        if 'sign_time' in d:
            o.sign_time = d['sign_time']
        if 'user_ids' in d:
            o.user_ids = d['user_ids']
        return o


