#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JointAccountQuotaDTO import JointAccountQuotaDTO


class JointAccountMemberRespDTO(object):

    def __init__(self):
        self._account_quota = None
        self._logon_id = None
        self._name = None
        self._status = None
        self._user_id = None

    @property
    def account_quota(self):
        return self._account_quota

    @account_quota.setter
    def account_quota(self, value):
        if isinstance(value, list):
            self._account_quota = list()
            for i in value:
                if isinstance(i, JointAccountQuotaDTO):
                    self._account_quota.append(i)
                else:
                    self._account_quota.append(JointAccountQuotaDTO.from_alipay_dict(i))
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_quota:
            if isinstance(self.account_quota, list):
                for i in range(0, len(self.account_quota)):
                    element = self.account_quota[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.account_quota[i] = element.to_alipay_dict()
            if hasattr(self.account_quota, 'to_alipay_dict'):
                params['account_quota'] = self.account_quota.to_alipay_dict()
            else:
                params['account_quota'] = self.account_quota
        if self.logon_id:
            if hasattr(self.logon_id, 'to_alipay_dict'):
                params['logon_id'] = self.logon_id.to_alipay_dict()
            else:
                params['logon_id'] = self.logon_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JointAccountMemberRespDTO()
        if 'account_quota' in d:
            o.account_quota = d['account_quota']
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'name' in d:
            o.name = d['name']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


