#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftTenantidFansidQueryModel(object):

    def __init__(self):
        self._tenant_user_account = None

    @property
    def tenant_user_account(self):
        return self._tenant_user_account

    @tenant_user_account.setter
    def tenant_user_account(self, value):
        self._tenant_user_account = value


    def to_alipay_dict(self):
        params = dict()
        if self.tenant_user_account:
            if hasattr(self.tenant_user_account, 'to_alipay_dict'):
                params['tenant_user_account'] = self.tenant_user_account.to_alipay_dict()
            else:
                params['tenant_user_account'] = self.tenant_user_account
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftTenantidFansidQueryModel()
        if 'tenant_user_account' in d:
            o.tenant_user_account = d['tenant_user_account']
        return o


