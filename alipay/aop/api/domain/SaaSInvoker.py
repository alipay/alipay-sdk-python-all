#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SaaSInvoker(object):

    def __init__(self):
        self._aliyun_user_id = None
        self._invoker_type = None
        self._tenant = None
        self._tenant_id = None
        self._user = None
        self._user_type = None

    @property
    def aliyun_user_id(self):
        return self._aliyun_user_id

    @aliyun_user_id.setter
    def aliyun_user_id(self, value):
        self._aliyun_user_id = value
    @property
    def invoker_type(self):
        return self._invoker_type

    @invoker_type.setter
    def invoker_type(self, value):
        self._invoker_type = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.aliyun_user_id:
            if hasattr(self.aliyun_user_id, 'to_alipay_dict'):
                params['aliyun_user_id'] = self.aliyun_user_id.to_alipay_dict()
            else:
                params['aliyun_user_id'] = self.aliyun_user_id
        if self.invoker_type:
            if hasattr(self.invoker_type, 'to_alipay_dict'):
                params['invoker_type'] = self.invoker_type.to_alipay_dict()
            else:
                params['invoker_type'] = self.invoker_type
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.user:
            if hasattr(self.user, 'to_alipay_dict'):
                params['user'] = self.user.to_alipay_dict()
            else:
                params['user'] = self.user
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SaaSInvoker()
        if 'aliyun_user_id' in d:
            o.aliyun_user_id = d['aliyun_user_id']
        if 'invoker_type' in d:
            o.invoker_type = d['invoker_type']
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'user' in d:
            o.user = d['user']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


