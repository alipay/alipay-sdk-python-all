#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsurancePreAuthInfo(object):

    def __init__(self):
        self._apply_time = None
        self._main_pre_auth = None
        self._pre_auth_no = None
        self._pre_auth_quota = None
        self._sub_pre_auth_no = None

    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def main_pre_auth(self):
        return self._main_pre_auth

    @main_pre_auth.setter
    def main_pre_auth(self, value):
        self._main_pre_auth = value
    @property
    def pre_auth_no(self):
        return self._pre_auth_no

    @pre_auth_no.setter
    def pre_auth_no(self, value):
        self._pre_auth_no = value
    @property
    def pre_auth_quota(self):
        return self._pre_auth_quota

    @pre_auth_quota.setter
    def pre_auth_quota(self, value):
        self._pre_auth_quota = value
    @property
    def sub_pre_auth_no(self):
        return self._sub_pre_auth_no

    @sub_pre_auth_no.setter
    def sub_pre_auth_no(self, value):
        self._sub_pre_auth_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.main_pre_auth:
            if hasattr(self.main_pre_auth, 'to_alipay_dict'):
                params['main_pre_auth'] = self.main_pre_auth.to_alipay_dict()
            else:
                params['main_pre_auth'] = self.main_pre_auth
        if self.pre_auth_no:
            if hasattr(self.pre_auth_no, 'to_alipay_dict'):
                params['pre_auth_no'] = self.pre_auth_no.to_alipay_dict()
            else:
                params['pre_auth_no'] = self.pre_auth_no
        if self.pre_auth_quota:
            if hasattr(self.pre_auth_quota, 'to_alipay_dict'):
                params['pre_auth_quota'] = self.pre_auth_quota.to_alipay_dict()
            else:
                params['pre_auth_quota'] = self.pre_auth_quota
        if self.sub_pre_auth_no:
            if hasattr(self.sub_pre_auth_no, 'to_alipay_dict'):
                params['sub_pre_auth_no'] = self.sub_pre_auth_no.to_alipay_dict()
            else:
                params['sub_pre_auth_no'] = self.sub_pre_auth_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsurancePreAuthInfo()
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'main_pre_auth' in d:
            o.main_pre_auth = d['main_pre_auth']
        if 'pre_auth_no' in d:
            o.pre_auth_no = d['pre_auth_no']
        if 'pre_auth_quota' in d:
            o.pre_auth_quota = d['pre_auth_quota']
        if 'sub_pre_auth_no' in d:
            o.sub_pre_auth_no = d['sub_pre_auth_no']
        return o


