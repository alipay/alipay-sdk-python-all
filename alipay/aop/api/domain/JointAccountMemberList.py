#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JointAccountQuotaDTO import JointAccountQuotaDTO


class JointAccountMemberList(object):

    def __init__(self):
        self._account_quota = None
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
        o = JointAccountMemberList()
        if 'account_quota' in d:
            o.account_quota = d['account_quota']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


