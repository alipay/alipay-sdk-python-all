#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceExpensecontrolQuotaDeleteModel(object):

    def __init__(self):
        self._enterprise_id = None
        self._issue_batch_id = None
        self._quota_id = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def issue_batch_id(self):
        return self._issue_batch_id

    @issue_batch_id.setter
    def issue_batch_id(self, value):
        self._issue_batch_id = value
    @property
    def quota_id(self):
        return self._quota_id

    @quota_id.setter
    def quota_id(self, value):
        self._quota_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.issue_batch_id:
            if hasattr(self.issue_batch_id, 'to_alipay_dict'):
                params['issue_batch_id'] = self.issue_batch_id.to_alipay_dict()
            else:
                params['issue_batch_id'] = self.issue_batch_id
        if self.quota_id:
            if hasattr(self.quota_id, 'to_alipay_dict'):
                params['quota_id'] = self.quota_id.to_alipay_dict()
            else:
                params['quota_id'] = self.quota_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceExpensecontrolQuotaDeleteModel()
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'issue_batch_id' in d:
            o.issue_batch_id = d['issue_batch_id']
        if 'quota_id' in d:
            o.quota_id = d['quota_id']
        return o


