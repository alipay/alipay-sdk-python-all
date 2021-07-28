#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LogisticsAccountInfo(object):

    def __init__(self):
        self._audit_desc = None
        self._logistics_account_id = None
        self._logistics_account_status = None
        self._pid = None

    @property
    def audit_desc(self):
        return self._audit_desc

    @audit_desc.setter
    def audit_desc(self, value):
        self._audit_desc = value
    @property
    def logistics_account_id(self):
        return self._logistics_account_id

    @logistics_account_id.setter
    def logistics_account_id(self, value):
        self._logistics_account_id = value
    @property
    def logistics_account_status(self):
        return self._logistics_account_status

    @logistics_account_status.setter
    def logistics_account_status(self, value):
        self._logistics_account_status = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_desc:
            if hasattr(self.audit_desc, 'to_alipay_dict'):
                params['audit_desc'] = self.audit_desc.to_alipay_dict()
            else:
                params['audit_desc'] = self.audit_desc
        if self.logistics_account_id:
            if hasattr(self.logistics_account_id, 'to_alipay_dict'):
                params['logistics_account_id'] = self.logistics_account_id.to_alipay_dict()
            else:
                params['logistics_account_id'] = self.logistics_account_id
        if self.logistics_account_status:
            if hasattr(self.logistics_account_status, 'to_alipay_dict'):
                params['logistics_account_status'] = self.logistics_account_status.to_alipay_dict()
            else:
                params['logistics_account_status'] = self.logistics_account_status
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsAccountInfo()
        if 'audit_desc' in d:
            o.audit_desc = d['audit_desc']
        if 'logistics_account_id' in d:
            o.logistics_account_id = d['logistics_account_id']
        if 'logistics_account_status' in d:
            o.logistics_account_status = d['logistics_account_status']
        if 'pid' in d:
            o.pid = d['pid']
        return o


