#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InstAllocationQuotaVO(object):

    def __init__(self):
        self._account_no = None
        self._account_type = None
        self._active = None
        self._effective_time = None
        self._expire_time = None
        self._memo = None
        self._quota_mode = None
        self._quota_value = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value
    @property
    def effective_time(self):
        return self._effective_time

    @effective_time.setter
    def effective_time(self, value):
        self._effective_time = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def quota_mode(self):
        return self._quota_mode

    @quota_mode.setter
    def quota_mode(self, value):
        self._quota_mode = value
    @property
    def quota_value(self):
        return self._quota_value

    @quota_value.setter
    def quota_value(self, value):
        self._quota_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.active:
            if hasattr(self.active, 'to_alipay_dict'):
                params['active'] = self.active.to_alipay_dict()
            else:
                params['active'] = self.active
        if self.effective_time:
            if hasattr(self.effective_time, 'to_alipay_dict'):
                params['effective_time'] = self.effective_time.to_alipay_dict()
            else:
                params['effective_time'] = self.effective_time
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.quota_mode:
            if hasattr(self.quota_mode, 'to_alipay_dict'):
                params['quota_mode'] = self.quota_mode.to_alipay_dict()
            else:
                params['quota_mode'] = self.quota_mode
        if self.quota_value:
            if hasattr(self.quota_value, 'to_alipay_dict'):
                params['quota_value'] = self.quota_value.to_alipay_dict()
            else:
                params['quota_value'] = self.quota_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstAllocationQuotaVO()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'active' in d:
            o.active = d['active']
        if 'effective_time' in d:
            o.effective_time = d['effective_time']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'memo' in d:
            o.memo = d['memo']
        if 'quota_mode' in d:
            o.quota_mode = d['quota_mode']
        if 'quota_value' in d:
            o.quota_value = d['quota_value']
        return o


