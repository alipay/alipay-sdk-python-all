#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReferenceId import ReferenceId


class AnttechBlockchainDefinSaasAccountQueryModel(object):

    def __init__(self):
        self._account_status = None
        self._out_member_id = None
        self._platform_member_id = None

    @property
    def account_status(self):
        return self._account_status

    @account_status.setter
    def account_status(self, value):
        self._account_status = value
    @property
    def out_member_id(self):
        return self._out_member_id

    @out_member_id.setter
    def out_member_id(self, value):
        if isinstance(value, ReferenceId):
            self._out_member_id = value
        else:
            self._out_member_id = ReferenceId.from_alipay_dict(value)
    @property
    def platform_member_id(self):
        return self._platform_member_id

    @platform_member_id.setter
    def platform_member_id(self, value):
        self._platform_member_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_status:
            if hasattr(self.account_status, 'to_alipay_dict'):
                params['account_status'] = self.account_status.to_alipay_dict()
            else:
                params['account_status'] = self.account_status
        if self.out_member_id:
            if hasattr(self.out_member_id, 'to_alipay_dict'):
                params['out_member_id'] = self.out_member_id.to_alipay_dict()
            else:
                params['out_member_id'] = self.out_member_id
        if self.platform_member_id:
            if hasattr(self.platform_member_id, 'to_alipay_dict'):
                params['platform_member_id'] = self.platform_member_id.to_alipay_dict()
            else:
                params['platform_member_id'] = self.platform_member_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinSaasAccountQueryModel()
        if 'account_status' in d:
            o.account_status = d['account_status']
        if 'out_member_id' in d:
            o.out_member_id = d['out_member_id']
        if 'platform_member_id' in d:
            o.platform_member_id = d['platform_member_id']
        return o


