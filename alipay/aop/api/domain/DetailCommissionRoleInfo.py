#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LatestCommissionInfo import LatestCommissionInfo


class DetailCommissionRoleInfo(object):

    def __init__(self):
        self._latest_commission = None
        self._role_account_name = None
        self._role_alipay_account = None
        self._role_confirm_url = None
        self._role_level = None
        self._role_rate = None
        self._role_status = None
        self._role_type = None

    @property
    def latest_commission(self):
        return self._latest_commission

    @latest_commission.setter
    def latest_commission(self, value):
        if isinstance(value, LatestCommissionInfo):
            self._latest_commission = value
        else:
            self._latest_commission = LatestCommissionInfo.from_alipay_dict(value)
    @property
    def role_account_name(self):
        return self._role_account_name

    @role_account_name.setter
    def role_account_name(self, value):
        self._role_account_name = value
    @property
    def role_alipay_account(self):
        return self._role_alipay_account

    @role_alipay_account.setter
    def role_alipay_account(self, value):
        self._role_alipay_account = value
    @property
    def role_confirm_url(self):
        return self._role_confirm_url

    @role_confirm_url.setter
    def role_confirm_url(self, value):
        self._role_confirm_url = value
    @property
    def role_level(self):
        return self._role_level

    @role_level.setter
    def role_level(self, value):
        self._role_level = value
    @property
    def role_rate(self):
        return self._role_rate

    @role_rate.setter
    def role_rate(self, value):
        self._role_rate = value
    @property
    def role_status(self):
        return self._role_status

    @role_status.setter
    def role_status(self, value):
        self._role_status = value
    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.latest_commission:
            if hasattr(self.latest_commission, 'to_alipay_dict'):
                params['latest_commission'] = self.latest_commission.to_alipay_dict()
            else:
                params['latest_commission'] = self.latest_commission
        if self.role_account_name:
            if hasattr(self.role_account_name, 'to_alipay_dict'):
                params['role_account_name'] = self.role_account_name.to_alipay_dict()
            else:
                params['role_account_name'] = self.role_account_name
        if self.role_alipay_account:
            if hasattr(self.role_alipay_account, 'to_alipay_dict'):
                params['role_alipay_account'] = self.role_alipay_account.to_alipay_dict()
            else:
                params['role_alipay_account'] = self.role_alipay_account
        if self.role_confirm_url:
            if hasattr(self.role_confirm_url, 'to_alipay_dict'):
                params['role_confirm_url'] = self.role_confirm_url.to_alipay_dict()
            else:
                params['role_confirm_url'] = self.role_confirm_url
        if self.role_level:
            if hasattr(self.role_level, 'to_alipay_dict'):
                params['role_level'] = self.role_level.to_alipay_dict()
            else:
                params['role_level'] = self.role_level
        if self.role_rate:
            if hasattr(self.role_rate, 'to_alipay_dict'):
                params['role_rate'] = self.role_rate.to_alipay_dict()
            else:
                params['role_rate'] = self.role_rate
        if self.role_status:
            if hasattr(self.role_status, 'to_alipay_dict'):
                params['role_status'] = self.role_status.to_alipay_dict()
            else:
                params['role_status'] = self.role_status
        if self.role_type:
            if hasattr(self.role_type, 'to_alipay_dict'):
                params['role_type'] = self.role_type.to_alipay_dict()
            else:
                params['role_type'] = self.role_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DetailCommissionRoleInfo()
        if 'latest_commission' in d:
            o.latest_commission = d['latest_commission']
        if 'role_account_name' in d:
            o.role_account_name = d['role_account_name']
        if 'role_alipay_account' in d:
            o.role_alipay_account = d['role_alipay_account']
        if 'role_confirm_url' in d:
            o.role_confirm_url = d['role_confirm_url']
        if 'role_level' in d:
            o.role_level = d['role_level']
        if 'role_rate' in d:
            o.role_rate = d['role_rate']
        if 'role_status' in d:
            o.role_status = d['role_status']
        if 'role_type' in d:
            o.role_type = d['role_type']
        return o


