#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PlatformPrescriptionStatusExtInfo(object):

    def __init__(self):
        self._audit_fail_reason = None
        self._audit_pharmacist_name = None
        self._audit_time = None
        self._out_audit_pharmacist_id = None

    @property
    def audit_fail_reason(self):
        return self._audit_fail_reason

    @audit_fail_reason.setter
    def audit_fail_reason(self, value):
        self._audit_fail_reason = value
    @property
    def audit_pharmacist_name(self):
        return self._audit_pharmacist_name

    @audit_pharmacist_name.setter
    def audit_pharmacist_name(self, value):
        self._audit_pharmacist_name = value
    @property
    def audit_time(self):
        return self._audit_time

    @audit_time.setter
    def audit_time(self, value):
        self._audit_time = value
    @property
    def out_audit_pharmacist_id(self):
        return self._out_audit_pharmacist_id

    @out_audit_pharmacist_id.setter
    def out_audit_pharmacist_id(self, value):
        self._out_audit_pharmacist_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_fail_reason:
            if hasattr(self.audit_fail_reason, 'to_alipay_dict'):
                params['audit_fail_reason'] = self.audit_fail_reason.to_alipay_dict()
            else:
                params['audit_fail_reason'] = self.audit_fail_reason
        if self.audit_pharmacist_name:
            if hasattr(self.audit_pharmacist_name, 'to_alipay_dict'):
                params['audit_pharmacist_name'] = self.audit_pharmacist_name.to_alipay_dict()
            else:
                params['audit_pharmacist_name'] = self.audit_pharmacist_name
        if self.audit_time:
            if hasattr(self.audit_time, 'to_alipay_dict'):
                params['audit_time'] = self.audit_time.to_alipay_dict()
            else:
                params['audit_time'] = self.audit_time
        if self.out_audit_pharmacist_id:
            if hasattr(self.out_audit_pharmacist_id, 'to_alipay_dict'):
                params['out_audit_pharmacist_id'] = self.out_audit_pharmacist_id.to_alipay_dict()
            else:
                params['out_audit_pharmacist_id'] = self.out_audit_pharmacist_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PlatformPrescriptionStatusExtInfo()
        if 'audit_fail_reason' in d:
            o.audit_fail_reason = d['audit_fail_reason']
        if 'audit_pharmacist_name' in d:
            o.audit_pharmacist_name = d['audit_pharmacist_name']
        if 'audit_time' in d:
            o.audit_time = d['audit_time']
        if 'out_audit_pharmacist_id' in d:
            o.out_audit_pharmacist_id = d['out_audit_pharmacist_id']
        return o


