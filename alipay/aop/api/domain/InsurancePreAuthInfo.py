#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsurancePreAuthInfo(object):

    def __init__(self):
        self._apply_time = None
        self._pre_auth_quota = None

    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def pre_auth_quota(self):
        return self._pre_auth_quota

    @pre_auth_quota.setter
    def pre_auth_quota(self, value):
        self._pre_auth_quota = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.pre_auth_quota:
            if hasattr(self.pre_auth_quota, 'to_alipay_dict'):
                params['pre_auth_quota'] = self.pre_auth_quota.to_alipay_dict()
            else:
                params['pre_auth_quota'] = self.pre_auth_quota
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsurancePreAuthInfo()
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'pre_auth_quota' in d:
            o.pre_auth_quota = d['pre_auth_quota']
        return o


