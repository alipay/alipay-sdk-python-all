#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ClerkQuotaRecordQueryOpenResult(object):

    def __init__(self):
        self._change_amount = None
        self._change_time = None
        self._change_type = None
        self._company_clerk_id = None
        self._quota_type = None
        self._remark = None

    @property
    def change_amount(self):
        return self._change_amount

    @change_amount.setter
    def change_amount(self, value):
        self._change_amount = value
    @property
    def change_time(self):
        return self._change_time

    @change_time.setter
    def change_time(self, value):
        self._change_time = value
    @property
    def change_type(self):
        return self._change_type

    @change_type.setter
    def change_type(self, value):
        self._change_type = value
    @property
    def company_clerk_id(self):
        return self._company_clerk_id

    @company_clerk_id.setter
    def company_clerk_id(self, value):
        self._company_clerk_id = value
    @property
    def quota_type(self):
        return self._quota_type

    @quota_type.setter
    def quota_type(self, value):
        self._quota_type = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.change_amount:
            if hasattr(self.change_amount, 'to_alipay_dict'):
                params['change_amount'] = self.change_amount.to_alipay_dict()
            else:
                params['change_amount'] = self.change_amount
        if self.change_time:
            if hasattr(self.change_time, 'to_alipay_dict'):
                params['change_time'] = self.change_time.to_alipay_dict()
            else:
                params['change_time'] = self.change_time
        if self.change_type:
            if hasattr(self.change_type, 'to_alipay_dict'):
                params['change_type'] = self.change_type.to_alipay_dict()
            else:
                params['change_type'] = self.change_type
        if self.company_clerk_id:
            if hasattr(self.company_clerk_id, 'to_alipay_dict'):
                params['company_clerk_id'] = self.company_clerk_id.to_alipay_dict()
            else:
                params['company_clerk_id'] = self.company_clerk_id
        if self.quota_type:
            if hasattr(self.quota_type, 'to_alipay_dict'):
                params['quota_type'] = self.quota_type.to_alipay_dict()
            else:
                params['quota_type'] = self.quota_type
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ClerkQuotaRecordQueryOpenResult()
        if 'change_amount' in d:
            o.change_amount = d['change_amount']
        if 'change_time' in d:
            o.change_time = d['change_time']
        if 'change_type' in d:
            o.change_type = d['change_type']
        if 'company_clerk_id' in d:
            o.company_clerk_id = d['company_clerk_id']
        if 'quota_type' in d:
            o.quota_type = d['quota_type']
        if 'remark' in d:
            o.remark = d['remark']
        return o


